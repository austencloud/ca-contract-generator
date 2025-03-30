# ui/section_forms/safety_form.py
from PyQt6.QtWidgets import (
    QVBoxLayout,
    QGroupBox,
    QTextEdit,
    QCheckBox,
    QHBoxLayout,
    QFormLayout,
    QLabel,
)
from ui.section_forms.base_form import BaseForm


class SafetyForm(BaseForm):
    """Form for editing health and safety policies"""

    def init_ui(self):
        # Main layout
        main_layout = QVBoxLayout()

        # Create a group box for general safety policy
        general_group = QGroupBox("General Safety Policy")
        general_layout = QVBoxLayout()

        # Create general safety policy field
        self.general_safety_edit = QTextEdit()
        self.general_safety_edit.setPlaceholderText(
            "Enter general health and safety policy"
        )
        self.general_safety_edit.setText(
            "Both parties agree to uphold safety as a priority.\n"
            "The Producer may modify or cancel the performance if conditions are unsafe.\n"
            "Full payment remains due if the Client is responsible for unsafe conditions."
        )

        general_layout.addWidget(self.general_safety_edit)
        general_group.setLayout(general_layout)

        # Create a group box for specific safety requirements
        specific_group = QGroupBox("Specific Safety Requirements")
        specific_layout = QVBoxLayout()

        # Create specific safety requirements field
        self.specific_safety_edit = QTextEdit()
        self.specific_safety_edit.setPlaceholderText(
            "Enter any specific safety requirements for this performance"
        )
        self.specific_safety_edit.setText(
            "• Performance area must be free of obstacles and hazards.\n"
            "• If outdoors, performance will be modified or canceled in case of rain, strong winds, or extreme temperatures.\n"
            "• Performer reserves the right to refuse any activities deemed unsafe.\n"
            "• Audience must maintain a safe distance from performer on stilts.\n"
            "• Performer must have access to water and rest breaks as needed."
        )

        specific_layout.addWidget(self.specific_safety_edit)
        specific_group.setLayout(specific_layout)

        # Create a group box for liability
        liability_group = QGroupBox("Liability and Insurance")
        liability_layout = QVBoxLayout()

        # Create liability section field
        self.liability_edit = QTextEdit()
        self.liability_edit.setPlaceholderText("Enter liability and insurance terms")
        self.liability_edit.setText(
            "The Producer maintains appropriate liability insurance coverage for performance activities.\n\n"
            "Client acknowledges that performance arts carry inherent risks. Client agrees to indemnify and hold "
            "harmless the Producer and Performer from any claims, losses, or damages arising from the performance, "
            "except those caused by willful misconduct or gross negligence of the Producer or Performer.\n\n"
            "Each party shall be responsible for their own negligent acts or omissions."
        )

        liability_layout.addWidget(self.liability_edit)
        liability_group.setLayout(liability_layout)

        # Add the group boxes to the main layout
        main_layout.addWidget(general_group)
        main_layout.addWidget(specific_group)
        main_layout.addWidget(liability_group)

        # Set the layout for this widget
        self.setLayout(main_layout)

        # Load initial data if available
        self.load_from_contract()

    def update_contract(self):
        # Update the contract with data from the form
        self.contract.safety.general_safety_policy = (
            self.general_safety_edit.toPlainText()
        )
        self.contract.safety.specific_requirements = (
            self.specific_safety_edit.toPlainText()
        )
        self.contract.safety.liability_terms = self.liability_edit.toPlainText()

    def load_from_contract(self):
        # Update form fields with data from the contract
        self.general_safety_edit.setText(self.contract.safety.general_safety_policy)
        self.specific_safety_edit.setText(self.contract.safety.specific_requirements)
        self.liability_edit.setText(self.contract.safety.liability_terms)
