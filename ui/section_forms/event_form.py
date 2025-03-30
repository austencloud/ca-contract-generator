# ui/section_forms/event_form.py
from PyQt6.QtWidgets import (
    QLabel,
    QLineEdit,
    QVBoxLayout,
    QFormLayout,
    QGroupBox,
    QDateEdit,
    QDateTimeEdit,
)
from PyQt6.QtCore import QDate, Qt
from ui.section_forms.base_form import BaseForm


class EventForm(BaseForm):
    """Form for editing event details and contract header"""

    def init_ui(self):
        # Main layout
        main_layout = QVBoxLayout()

        # Create a group box for contract information
        contract_group = QGroupBox("Contract Information")
        contract_layout = QFormLayout()

        # Create form fields for contract
        self.title_edit = QLineEdit()
        self.title_edit.setPlaceholderText(
            "e.g., Caribbean Dance Performance Agreement"
        )

        self.subtitle_edit = QLineEdit()
        self.subtitle_edit.setPlaceholderText(
            "e.g., Official Contract for Live Performance Services"
        )

        self.effective_date_edit = QDateEdit()
        self.effective_date_edit.setCalendarPopup(True)
        self.effective_date_edit.setDate(QDate.currentDate())
        self.effective_date_edit.setDisplayFormat("MMMM d, yyyy")

        # Add fields to contract layout
        contract_layout.addRow("Contract Title:", self.title_edit)
        contract_layout.addRow("Contract Subtitle:", self.subtitle_edit)
        contract_layout.addRow("Effective Date:", self.effective_date_edit)

        # Set the form layout for the contract group
        contract_group.setLayout(contract_layout)

        # Create a group box for event details
        event_group = QGroupBox("Event Details")
        event_layout = QFormLayout()

        # Create form fields for event
        self.location_edit = QLineEdit()
        self.location_edit.setPlaceholderText(
            "e.g., Harold Washington Social Security Center, Chicago, IL"
        )

        self.event_date_edit = QDateEdit()
        self.event_date_edit.setCalendarPopup(True)
        self.event_date_edit.setDate(
            QDate.currentDate().addDays(14)
        )  # Default to two weeks from now
        self.event_date_edit.setDisplayFormat("MMMM d, yyyy")

        self.performer_name_edit = QLineEdit()
        self.performer_name_edit.setPlaceholderText("e.g., Robert Bershadsky")

        # Add fields to event layout
        event_layout.addRow("Location:", self.location_edit)
        event_layout.addRow("Event Date:", self.event_date_edit)
        event_layout.addRow("Performer Name:", self.performer_name_edit)

        # Set the form layout for the event group
        event_group.setLayout(event_layout)

        # Add the group boxes to the main layout
        main_layout.addWidget(contract_group)
        main_layout.addWidget(event_group)

        # Add stretch to push the form to the top
        main_layout.addStretch()

        # Set the layout for this widget
        self.setLayout(main_layout)

        # Load initial data if available
        self.load_from_contract()

    def update_contract(self):
        # Update the contract with data from the form
        self.contract.title = self.title_edit.text()
        self.contract.subtitle = self.subtitle_edit.text()
        self.contract.effective_date = self.effective_date_edit.date().toString(
            "MMMM d, yyyy"
        )
        self.contract.event.location = self.location_edit.text()
        self.contract.event.date = self.event_date_edit.date().toString("MMMM d, yyyy")
        self.contract.performer_name = self.performer_name_edit.text()

    def load_from_contract(self):
        # Update form fields with data from the contract
        self.title_edit.setText(self.contract.title)
        self.subtitle_edit.setText(self.contract.subtitle)

        # Parse date string if available for effective date
        if self.contract.effective_date:
            try:
                date = QDate.fromString(self.contract.effective_date, "MMMM d, yyyy")
                if date.isValid():
                    self.effective_date_edit.setDate(date)
            except:
                pass

        self.location_edit.setText(self.contract.event.location)

        # Parse date string if available for event date
        if self.contract.event.date:
            try:
                date = QDate.fromString(self.contract.event.date, "MMMM d, yyyy")
                if date.isValid():
                    self.event_date_edit.setDate(date)
            except:
                pass

        self.performer_name_edit.setText(self.contract.performer_name)
