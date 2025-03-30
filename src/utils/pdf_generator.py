# utils/pdf_generator.py
import os
import tempfile
from PyQt6.QtGui import QPageSize
from PyQt6.QtCore import QUrl, QEventLoop, QMarginsF
from PyQt6.QtWidgets import QApplication, QMessageBox
from PyQt6.QtWebEngineCore import QWebEngineSettings
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtPrintSupport import QPrinter

from utils.html_generator import generate_html_contract


def generate_pdf(contract, output_path, theme_name):
    """Generate a PDF contract and save it to the specified path"""

    # Create temporary HTML file
    with tempfile.NamedTemporaryFile(suffix=".html", delete=False) as temp_file:
        html_content = generate_html_contract(contract, theme_name)
        temp_file.write(html_content.encode("utf-8"))
        temp_html_path = temp_file.name

    try:
        # Set up printer
        printer = QPrinter(QPrinter.PrinterMode.HighResolution)
        printer.setOutputFormat(QPrinter.OutputFormat.PdfFormat)
        printer.setOutputFileName(output_path)
        printer.setPageSize(QPageSize(QPageSize.PageSizeId.A4))
        
        # Create QMarginsF object for margins
        margin_points = 15 * 2.83  # Convert mm to points
        margins = QMarginsF(margin_points, margin_points, margin_points, margin_points)
        printer.setPageMargins(margins)

        # Create web engine view
        view = QWebEngineView()
        view.settings().setAttribute(
            QWebEngineSettings.WebAttribute.JavascriptEnabled, True
        )
        view.settings().setAttribute(
            QWebEngineSettings.WebAttribute.LocalContentCanAccessFileUrls, True
        )
        view.settings().setAttribute(
            QWebEngineSettings.WebAttribute.PrintElementBackgrounds, True
        )

        # Set up event loop for synchronous loading
        loop = QEventLoop()
        view.loadFinished.connect(loop.quit)

        # Load the HTML file
        view.load(QUrl.fromLocalFile(temp_html_path))
        loop.exec()  # Wait until page is loaded

        # Try to generate PDF using the newer API first
        try:
            # Create a proper QPageLayout object
            from PyQt6.QtGui import QPageLayout
            page_layout = QPageLayout(
                QPageSize(QPageSize.PageSizeId.A4),
                QPageLayout.Orientation.Portrait,
                margins
            )
            
            # Use printToPdf with the proper layout
            def callback(pdf_data):
                if pdf_data:
                    with open(output_path, 'wb') as f:
                        f.write(pdf_data)
                    print(f"PDF saved to {output_path}")
                else:
                    print("Failed to generate PDF data")
                loop.quit()
            
            view.page().printToPdf(callback, page_layout)
            loop.exec()  # Wait for the callback
            
        except (AttributeError, TypeError) as e:
            print(f"Error with printToPdf: {e}")
            try:
                # Try the older print method as fallback
                view.page().print(printer, lambda success: loop.quit())
                loop.exec()  # Wait until printing is done
            except AttributeError:
                raise Exception("PDF generation is not supported with this version of PyQt6.")

    finally:
        # Clean up temporary file
        os.unlink(temp_html_path)