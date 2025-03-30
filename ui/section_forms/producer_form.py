# ui/section_forms/producer_form.py
from PyQt6.QtWidgets import QLabel, QLineEdit, QVBoxLayout, QFormLayout, QGroupBox
from ui.section_forms.base_form import BaseForm


class ProducerForm(BaseForm):
    """Form for editing producer information"""

    def init_ui(self):
        # Main layout
        main_layout = QVBoxLayout()

        # Create a group box
        group_box = QGroupBox("Producer Information")
        form_layout = QFormLayout()

        # Create form fields
        self.name_edit = QLineEdit()
        self.name_edit.setPlaceholderText("Producer's full name")

        self.company_edit = QLineEdit()
        self.company_edit.setPlaceholderText("Production company name")

        self.phone_edit = QLineEdit()
        self.phone_edit.setPlaceholderText("Format: 123-456-7890")
        self.phone_edit.setInputMask("999-999-9999;_")

        self.email_edit = QLineEdit()
        self.email_edit.setPlaceholderText("producer@example.com")

        # Add fields to form layout
        form_layout.addRow("Name:", self.name_edit)
        form_layout.addRow("Company:", self.company_edit)
        form_layout.addRow("Phone:", self.phone_edit)
        form_layout.addRow("Email:", self.email_edit)

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
        self.contract.producer.name = self.name_edit.text()
        self.contract.producer.company = self.company_edit.text()
        self.contract.producer.phone = self.phone_edit.text()
        self.contract.producer.email = self.email_edit.text()

    def load_from_contract(self):
        # Update form fields with data from the contract
        self.name_edit.setText(self.contract.producer.name)
        self.company_edit.setText(self.contract.producer.company)
        self.phone_edit.setText(self.contract.producer.phone)
        self.email_edit.setText(self.contract.producer.email)
