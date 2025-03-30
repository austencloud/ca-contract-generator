# ui/section_forms/cancellation_form.py
from PyQt6.QtWidgets import (
    QVBoxLayout,
    QFormLayout,
    QGroupBox,
    QTextEdit,
    QSpinBox,
    QCheckBox,
    QComboBox,
    QLabel,
)
from ui.section_forms.base_form import BaseForm


class CancellationForm(BaseForm):
    """Form for editing cancellation policy"""

    def init_ui(self):
        # Main layout
        main_layout = QVBoxLayout()

        # Create a group box for client cancellation
        client_group = QGroupBox("Client Cancellation")
        client_layout = QVBoxLayout()

        # Client cancellation policy
        self.client_policy_edit = QTextEdit()
        self.client_policy_edit.setPlaceholderText(
            "Enter policy for client cancellations"
        )
        self.client_policy_edit.setText(
            "All payments are non-refundable.\n"
            "If Client cancels, Cirque Aflame will offer a backup date at no extra charge, subject to availability.\n"
            "If the backup date is not suitable, deposit may be applied to a future event within 12 months."
        )

        client_layout.addWidget(self.client_policy_edit)
        client_group.setLayout(client_layout)

        # Create a group box for producer cancellation
        producer_group = QGroupBox("Producer Cancellation")
        producer_layout = QVBoxLayout()

        # Producer cancellation policy
        self.producer_policy_edit = QTextEdit()
        self.producer_policy_edit.setPlaceholderText(
            "Enter policy for producer cancellations"
        )
        self.producer_policy_edit.setText(
            "If the Producer cancels, a full refund will be provided or payment may be applied toward rescheduling."
        )

        producer_layout.addWidget(self.producer_policy_edit)
        producer_group.setLayout(producer_layout)

        # Create a group box for force majeure
        force_group = QGroupBox("Force Majeure")
        force_layout = QVBoxLayout()

        # Force majeure policy
        self.force_majeure_edit = QTextEdit()
        self.force_majeure_edit.setPlaceholderText(
            "Enter policy for cancellations due to force majeure"
        )
        self.force_majeure_edit.setText(
            "Neither party shall be liable for failure to perform due to events beyond their reasonable control, "
            "including but not limited to: natural disasters, severe weather, civil unrest, pandemics, government "
            "restrictions, or other similar circumstances.\n\n"
            "In such cases, parties shall work together to reschedule the performance or find an equitable solution."
        )

        force_layout.addWidget(self.force_majeure_edit)
        force_group.setLayout(force_layout)

        # Add the group boxes to the main layout
        main_layout.addWidget(client_group)
        main_layout.addWidget(producer_group)
        main_layout.addWidget(force_group)

        # Set the layout for this widget
        self.setLayout(main_layout)

        # Load initial data if available
        self.load_from_contract()

    def update_contract(self):
        # Update the contract with data from the form
        self.contract.cancellation.client_policy = self.client_policy_edit.toPlainText()
        self.contract.cancellation.producer_policy = (
            self.producer_policy_edit.toPlainText()
        )
        self.contract.cancellation.force_majeure = self.force_majeure_edit.toPlainText()

    def load_from_contract(self):
        # Update form fields with data from the contract
        self.client_policy_edit.setText(self.contract.cancellation.client_policy)
        self.producer_policy_edit.setText(self.contract.cancellation.producer_policy)
        self.force_majeure_edit.setText(self.contract.cancellation.force_majeure)
