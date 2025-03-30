# ui/section_forms/client_form.py
from PyQt6.QtWidgets import (
    QLabel,
    QLineEdit,
    QVBoxLayout,
    QFormLayout,
    QGroupBox,
    QCompleter,
)
from PyQt6.QtCore import Qt
from ui.section_forms.base_form import BaseForm


class ClientForm(BaseForm):
    """Form for editing client information"""

    def init_ui(self):
        # Main layout
        main_layout = QVBoxLayout()

        # Create a group box
        group_box = QGroupBox("Client Information")
        form_layout = QFormLayout()

        # Create form fields
        self.name_edit = QLineEdit()
        self.name_edit.setPlaceholderText("Enter client's full name")

        self.phone_edit = QLineEdit()
        self.phone_edit.setPlaceholderText("Format: 123-456-7890")
        self.phone_edit.setInputMask("999-999-9999;_")

        self.email_edit = QLineEdit()
        self.email_edit.setPlaceholderText("client@example.com")

        self.title_edit = QLineEdit()
        self.title_edit.setPlaceholderText("Client's professional title")

        # Add some common job titles for autocomplete
        job_titles = [
            "Event Planner",
            "Corporate Event Planner",
            "Wedding Planner",
            "Program Director",
            "Producer",
            "Event Coordinator",
            "Marketing Manager",
            "Project Manager",
            "Executive Assistant",
        ]
        completer = QCompleter(job_titles)
        completer.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        self.title_edit.setCompleter(completer)

        # Add fields to form layout
        form_layout.addRow("Name:", self.name_edit)
        form_layout.addRow("Phone:", self.phone_edit)
        form_layout.addRow("Email:", self.email_edit)
        form_layout.addRow("Title:", self.title_edit)

        # Set the form layout for the group box
        group_box.setLayout(form_layout)

        # Add the group box to the main layout
        main_layout.addWidget(group_box)

        # Add stretch to push the form to the top
        main_layout.addStretch()

        # Set the layout for this widget
        self.setLayout(main_layout)

        # Load initial data if available
        self.load_from_contract()

    def update_contract(self):
        # Update the contract with data from the form
        self.contract.client.name = self.name_edit.text()
        self.contract.client.phone = self.phone_edit.text()
        self.contract.client.email = self.email_edit.text()
        self.contract.client.title = self.title_edit.text()

    def load_from_contract(self):
        # Update form fields with data from the contract
        self.name_edit.setText(self.contract.client.name)
        self.phone_edit.setText(self.contract.client.phone)
        self.email_edit.setText(self.contract.client.email)
        self.title_edit.setText(self.contract.client.title)
