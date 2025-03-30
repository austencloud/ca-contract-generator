# ui/main_window.py
from PyQt6.QtWidgets import (
    QMainWindow,
    QTabWidget,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
    QFileDialog,
    QMessageBox,
    QLabel,
    QComboBox,
)
from PyQt6.QtCore import Qt, QSettings
from PyQt6.QtGui import QIcon, QAction

from ui.section_forms.client_form import ClientForm
from ui.section_forms.producer_form import ProducerForm
from ui.section_forms.event_form import EventForm
from ui.section_forms.fees_form import FeesForm
from ui.section_forms.services_form import ServicesForm
from ui.section_forms.cancellation_form import CancellationForm
from ui.section_forms.schedule_form import ScheduleForm
from ui.section_forms.obligations_form import ObligationsForm
from ui.section_forms.safety_form import SafetyForm

from models.contract import Contract
from utils.pdf_generator import generate_pdf
from utils.themes import get_available_themes


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.contract = Contract()
        self.settings = QSettings("CirqueAflame", "ContractGenerator")
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Contract Generator")
        self.setGeometry(100, 100, 900, 700)

        # Create menu bar
        self.create_menu_bar()

        # Create status bar
        self.statusBar().showMessage("Ready")

        # Main layout
        main_widget = QWidget()
        main_layout = QVBoxLayout(main_widget)

        # Theme selector
        theme_layout = QHBoxLayout()
        theme_layout.addWidget(QLabel("Contract Theme:"))
        self.theme_selector = QComboBox()
        self.theme_selector.addItems(get_available_themes())
        self.theme_selector.currentTextChanged.connect(self.on_theme_changed)
        theme_layout.addWidget(self.theme_selector)
        theme_layout.addStretch()
        main_layout.addLayout(theme_layout)

        # Create tab widget for different sections
        self.tab_widget = QTabWidget()

        # Create forms for each section
        self.client_form = ClientForm(self.contract)
        self.producer_form = ProducerForm(self.contract)
        self.event_form = EventForm(self.contract)
        self.fees_form = FeesForm(self.contract)
        self.services_form = ServicesForm(self.contract)
        self.cancellation_form = CancellationForm(self.contract)
        self.schedule_form = ScheduleForm(self.contract)
        self.obligations_form = ObligationsForm(self.contract)
        self.safety_form = SafetyForm(self.contract)

        # Add forms to tabs
        self.tab_widget.addTab(self.client_form, "Client")
        self.tab_widget.addTab(self.producer_form, "Producer")
        self.tab_widget.addTab(self.event_form, "Event Details")
        self.tab_widget.addTab(self.fees_form, "Fees")
        self.tab_widget.addTab(self.services_form, "Services")
        self.tab_widget.addTab(self.cancellation_form, "Cancellation")
        self.tab_widget.addTab(self.schedule_form, "Schedule")
        self.tab_widget.addTab(self.obligations_form, "Obligations")
        self.tab_widget.addTab(self.safety_form, "Health & Safety")

        main_layout.addWidget(self.tab_widget)

        # Button layout
        button_layout = QHBoxLayout()

        # Buttons
        self.preview_button = QPushButton("Preview Contract")
        self.preview_button.setIcon(QIcon.fromTheme("document-print-preview"))
        self.generate_button = QPushButton("Generate PDF")
        self.generate_button.setIcon(QIcon.fromTheme("document-save-as"))
        self.save_button = QPushButton("Save Contract Data")
        self.save_button.setIcon(QIcon.fromTheme("document-save"))
        self.load_button = QPushButton("Load Contract Data")
        self.load_button.setIcon(QIcon.fromTheme("document-open"))

        # Add buttons to layout
        button_layout.addWidget(self.preview_button)
        button_layout.addWidget(self.generate_button)
        button_layout.addWidget(self.save_button)
        button_layout.addWidget(self.load_button)

        # Connect signals
        self.preview_button.clicked.connect(self.preview_contract)
        self.generate_button.clicked.connect(self.generate_contract)
        self.save_button.clicked.connect(self.save_contract)
        self.load_button.clicked.connect(self.load_contract)

        main_layout.addLayout(button_layout)

        # Set main widget
        self.setCentralWidget(main_widget)

        # Load last session settings
        self.load_settings()

    def create_menu_bar(self):
        menubar = self.menuBar()

        # File menu
        file_menu = menubar.addMenu("&File")

        new_action = QAction("&New Contract", self)
        new_action.setShortcut("Ctrl+N")
        new_action.triggered.connect(self.new_contract)
        file_menu.addAction(new_action)

        open_action = QAction("&Open...", self)
        open_action.setShortcut("Ctrl+O")
        open_action.triggered.connect(self.load_contract)
        file_menu.addAction(open_action)

        save_action = QAction("&Save", self)
        save_action.setShortcut("Ctrl+S")
        save_action.triggered.connect(self.save_contract)
        file_menu.addAction(save_action)

        save_as_action = QAction("Save &As...", self)
        save_as_action.setShortcut("Ctrl+Shift+S")
        save_as_action.triggered.connect(self.save_contract_as)
        file_menu.addAction(save_as_action)

        file_menu.addSeparator()

        preview_action = QAction("Pre&view", self)
        preview_action.setShortcut("Ctrl+P")
        preview_action.triggered.connect(self.preview_contract)
        file_menu.addAction(preview_action)

        export_action = QAction("&Export to PDF...", self)
        export_action.setShortcut("Ctrl+E")
        export_action.triggered.connect(self.generate_contract)
        file_menu.addAction(export_action)

        file_menu.addSeparator()

        exit_action = QAction("E&xit", self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        # Help menu
        help_menu = menubar.addMenu("&Help")

        about_action = QAction("&About", self)
        about_action.triggered.connect(self.show_about)
        help_menu.addAction(about_action)

    def new_contract(self):
        # Confirm with user
        reply = QMessageBox.question(
            self,
            "New Contract",
            "Are you sure you want to create a new contract? Unsaved changes will be lost.",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No,
        )

        if reply == QMessageBox.StandardButton.Yes:
            # Reset contract to default values
            self.contract = Contract()

            # Update all forms with default data
            self.update_forms_from_contract()

            # Update status
            self.statusBar().showMessage("New contract created")

    def preview_contract(self):
        # Update contract from all forms
        self.update_contract_from_forms()

        # Generate HTML preview
        from utils.preview_window import PreviewWindow

        preview = PreviewWindow(self.contract, self.theme_selector.currentText())
        preview.exec()

    def generate_contract(self):
        # Update contract from all forms
        self.update_contract_from_forms()

        # Open file dialog to select save location
        file_path, _ = QFileDialog.getSaveFileName(
            self, "Save PDF Contract", "", "PDF Files (*.pdf)"
        )

        if file_path:
            # Generate and save PDF
            try:
                generate_pdf(
                    self.contract, file_path, self.theme_selector.currentText()
                )
                self.statusBar().showMessage(f"PDF saved to {file_path}")

                # Ask if user wants to open the PDF
                reply = QMessageBox.question(
                    self,
                    "Open PDF",
                    "PDF created successfully. Would you like to open it?",
                    QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                )

                if reply == QMessageBox.StandardButton.Yes:
                    import os
                    import platform

                    if platform.system() == "Windows":
                        os.startfile(file_path)
                    elif platform.system() == "Darwin":  # macOS
                        import subprocess

                        subprocess.call(("open", file_path))
                    else:  # Linux
                        import subprocess

                        subprocess.call(("xdg-open", file_path))
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to generate PDF: {str(e)}")

    def save_contract(self):
        # Check if we have a saved path
        saved_path = self.settings.value("last_save_path")

        if saved_path:
            # Update contract from all forms
            self.update_contract_from_forms()

            # Save contract data to the existing path
            try:
                self.contract.save_to_file(saved_path)
                self.statusBar().showMessage(f"Contract saved to {saved_path}")
            except Exception as e:
                QMessageBox.critical(
                    self, "Error", f"Failed to save contract: {str(e)}"
                )
        else:
            # No saved path, use save as
            self.save_contract_as()

    def save_contract_as(self):
        # Update contract from all forms
        self.update_contract_from_forms()

        # Open file dialog to select save location
        file_path, _ = QFileDialog.getSaveFileName(
            self, "Save Contract Data", "", "JSON Files (*.json)"
        )

        if file_path:
            # Save contract data
            try:
                self.contract.save_to_file(file_path)
                # Save the path for future use
                self.settings.setValue("last_save_path", file_path)
                self.statusBar().showMessage(f"Contract saved to {file_path}")
            except Exception as e:
                QMessageBox.critical(
                    self, "Error", f"Failed to save contract: {str(e)}"
                )

    def load_contract(self):
        # Open file dialog to select file
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Load Contract Data", "", "JSON Files (*.json)"
        )

        if file_path:
            # Load contract data
            try:
                self.contract.load_from_file(file_path)

                # Update all forms with loaded data
                self.update_forms_from_contract()

                # Save the path for future use
                self.settings.setValue("last_save_path", file_path)

                self.statusBar().showMessage(f"Contract loaded from {file_path}")
            except Exception as e:
                QMessageBox.critical(
                    self, "Error", f"Failed to load contract: {str(e)}"
                )

    def update_contract_from_forms(self):
        # Update the contract object with data from all forms
        self.client_form.update_contract()
        self.producer_form.update_contract()
        self.event_form.update_contract()
        self.fees_form.update_contract()
        self.services_form.update_contract()
        self.cancellation_form.update_contract()
        self.schedule_form.update_contract()
        self.obligations_form.update_contract()
        self.safety_form.update_contract()

    def update_forms_from_contract(self):
        # Update all forms with data from the contract
        self.client_form.load_from_contract()
        self.producer_form.load_from_contract()
        self.event_form.load_from_contract()
        self.fees_form.load_from_contract()
        self.services_form.load_from_contract()
        self.cancellation_form.load_from_contract()
        self.schedule_form.load_from_contract()
        self.obligations_form.load_from_contract()
        self.safety_form.load_from_contract()

    def on_theme_changed(self, theme_name):
        # Save the selected theme
        self.settings.setValue("selected_theme", theme_name)
        self.statusBar().showMessage(f"Theme changed to {theme_name}")

    def show_about(self):
        QMessageBox.about(
            self,
            "About Contract Generator",
            "Contract Generator v1.0\n\n"
            "A tool for generating professional performance contracts.\n\n"
            "© 2025 Cirque Aflame",
        )

    def load_settings(self):
        # Load last selected theme
        last_theme = self.settings.value("selected_theme")
        if last_theme and last_theme in get_available_themes():
            index = self.theme_selector.findText(last_theme)
            if index >= 0:
                self.theme_selector.setCurrentIndex(index)

    def closeEvent(self, event):
        # Save settings before closing
        self.settings.sync()
        event.accept()
