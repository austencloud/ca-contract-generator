# utils/preview_window.py
from PyQt6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QSizePolicy,
    QLabel,
    QSpacerItem,
    QMessageBox,
    QFileDialog,
)
from PyQt6.QtCore import QUrl, QTemporaryFile, QSize, Qt, QMarginsF
from PyQt6.QtGui import QIcon, QPageSize
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWebEngineCore import QWebEngineSettings
from PyQt6.QtPrintSupport import QPrinter, QPrintDialog

from utils.html_generator import generate_html_contract


class PreviewWindow(QDialog):
    """Dialog for previewing the contract"""

    def __init__(self, contract, theme_name, parent=None):
        super().__init__(parent)
        self.contract = contract
        self.theme_name = theme_name
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Contract Preview")
        self.setMinimumSize(800, 600)

        # Main layout
        main_layout = QVBoxLayout(self)

        # Create web view for preview
        self.web_view = QWebEngineView()
        self.web_view.settings().setAttribute(
            QWebEngineSettings.WebAttribute.JavascriptEnabled, True
        )
        self.web_view.settings().setAttribute(
            QWebEngineSettings.WebAttribute.LocalContentCanAccessFileUrls, True
        )

        # Generate HTML contract and load it into the web view
        html_content = generate_html_contract(self.contract, self.theme_name)

        # Load the HTML directly instead of using a temporary file
        self.web_view.setHtml(html_content)

        # Button layout
        button_layout = QHBoxLayout()

        # Add zoom controls
        zoom_layout = QHBoxLayout()
        self.zoom_label = QLabel("Zoom:")

        self.zoom_out_button = QPushButton("-")
        self.zoom_out_button.setMaximumWidth(30)
        self.zoom_out_button.clicked.connect(self.zoom_out)

        self.zoom_reset_button = QPushButton("100%")
        self.zoom_reset_button.setMaximumWidth(60)
        self.zoom_reset_button.clicked.connect(self.zoom_reset)

        self.zoom_in_button = QPushButton("+")
        self.zoom_in_button.setMaximumWidth(30)
        self.zoom_in_button.clicked.connect(self.zoom_in)

        zoom_layout.addWidget(self.zoom_label)
        zoom_layout.addWidget(self.zoom_out_button)
        zoom_layout.addWidget(self.zoom_reset_button)
        zoom_layout.addWidget(self.zoom_in_button)

        # Add print button
        self.print_button = QPushButton("Print")
        self.print_button.setIcon(QIcon.fromTheme("document-print"))
        self.print_button.clicked.connect(self.print_preview)

        # Add save as PDF button
        self.save_pdf_button = QPushButton("Save as PDF")
        self.save_pdf_button.setIcon(QIcon.fromTheme("document-save-as"))
        self.save_pdf_button.clicked.connect(self.save_as_pdf)

        # Add close button
        self.close_button = QPushButton("Close")
        self.close_button.setIcon(QIcon.fromTheme("window-close"))
        self.close_button.clicked.connect(self.close)

        # Add buttons to layout
        button_layout.addLayout(zoom_layout)
        button_layout.addStretch()
        button_layout.addWidget(self.print_button)
        button_layout.addWidget(self.save_pdf_button)
        button_layout.addWidget(self.close_button)

        # Add web view and buttons to main layout
        main_layout.addWidget(self.web_view)
        main_layout.addLayout(button_layout)

        # Set the zoom factor
        self.current_zoom = 1.0

    def zoom_in(self):
        """Zoom in the web view"""
        self.current_zoom += 0.1
        self.web_view.setZoomFactor(self.current_zoom)
        self.zoom_reset_button.setText(f"{int(self.current_zoom * 100)}%")

    def zoom_out(self):
        """Zoom out the web view"""
        if self.current_zoom > 0.2:
            self.current_zoom -= 0.1
            self.web_view.setZoomFactor(self.current_zoom)
            self.zoom_reset_button.setText(f"{int(self.current_zoom * 100)}%")

    def zoom_reset(self):
        """Reset zoom to 100%"""
        self.current_zoom = 1.0
        self.web_view.setZoomFactor(self.current_zoom)
        self.zoom_reset_button.setText("100%")

    def print_preview(self):
        """Print the contract"""
        printer = QPrinter(QPrinter.PrinterMode.HighResolution)

        # Configure printer to print background colors by default
        # Create QMarginsF object for margins (in millimeters)
        margin_points = 15 * 2.83
        margins = QMarginsF(margin_points, margin_points, margin_points, margin_points)
        printer.setPageMargins(margins)

        # Create print dialog
        print_dialog = QPrintDialog(printer, self)
        if print_dialog.exec() == QPrintDialog.DialogCode.Accepted:
            # Print the web view using the newer API approach
            def print_callback(success):
                if not success:
                    QMessageBox.critical(
                        self, "Printing Error", "Failed to print the document."
                    )

            # For printing, we'll just use the old method as it's more directly compatible with QPrinter
            try:
                # Try with the print method
                self.web_view.page().print(printer, print_callback)
            except AttributeError:
                QMessageBox.critical(
                    self,
                    "Printing Error",
                    "Printing is not supported with this version of PyQt6. Try saving as PDF instead.",
                )

    def print_finished(self, success):
        """Callback for print completion"""
        if not success:
            QMessageBox.critical(self, "Printing Error", "Printing failed!")

    def save_as_pdf(self):
        """Save the contract as a PDF file"""
        # Open file dialog for PDF location
        file_path, _ = QFileDialog.getSaveFileName(
            self, "Save Contract as PDF", "", "PDF Files (*.pdf)"
        )

        if file_path:
            # Set up printer
            printer = QPrinter(QPrinter.PrinterMode.HighResolution)
            printer.setOutputFormat(QPrinter.OutputFormat.PdfFormat)
            printer.setOutputFileName(file_path)
            printer.setPageSize(QPageSize(QPageSize.PageSizeId.A4))

            # Create QMarginsF object for margins
            margin_points = 15 * 2.83
            margins = QMarginsF(
                margin_points, margin_points, margin_points, margin_points
            )
            printer.setPageMargins(margins)

            # Try to generate PDF using the newer API approach
            try:
                # Create a proper QPageLayout object
                from PyQt6.QtGui import QPageLayout

                page_layout = QPageLayout(
                    QPageSize(QPageSize.PageSizeId.A4),
                    QPageLayout.Orientation.Portrait,
                    margins,
                )

                # Use printToPdf with proper callback
                def pdf_callback(pdf_data):
                    if pdf_data:
                        with open(file_path, "wb") as f:
                            f.write(pdf_data)
                        QMessageBox.information(
                            self, "PDF Saved", f"PDF saved successfully to {file_path}"
                        )
                    else:
                        QMessageBox.critical(
                            self, "PDF Generation Error", "Failed to generate PDF data"
                        )

                self.web_view.page().printToPdf(pdf_callback, page_layout)
            except (AttributeError, TypeError) as e:
                print(f"Error with printToPdf: {e}")
                try:
                    # Try the older print method as fallback
                    self.web_view.page().print(printer, self.pdf_saved)
                except AttributeError:
                    QMessageBox.critical(
                        self,
                        "PDF Generation Error",
                        "PDF generation is not supported with this version of PyQt6.",
                    )

    def pdf_saved(self, success):
        """Callback for PDF save completion"""
        if success:
            QMessageBox.information(self, "PDF Saved", "PDF saved successfully")
        else:
            QMessageBox.critical(self, "PDF Generation Error", "Failed to save PDF")

    def closeEvent(self, event):
        """Handle dialog close event"""
        event.accept()
