# ui/section_forms/schedule_form.py
from PyQt6.QtWidgets import (
    QVBoxLayout,
    QFormLayout,
    QGroupBox,
    QTextEdit,
    QSpinBox,
    QHBoxLayout,
    QWidget,
    QLabel,
    QTimeEdit,
)
from PyQt6.QtCore import QTime
from ui.section_forms.base_form import BaseForm


class ScheduleForm(BaseForm):
    """Form for editing schedule and arrival policy"""

    def init_ui(self):
        # Main layout
        main_layout = QVBoxLayout()

        # Create a group box for arrival times
        arrival_group = QGroupBox("Arrival and Setup")
        arrival_layout = QFormLayout()

        # Create arrival time fields
        arrival_widget = QWidget()
        arrival_hbox = QHBoxLayout(arrival_widget)
        arrival_hbox.setContentsMargins(0, 0, 0, 0)

        self.arrival_minutes_before = QSpinBox()
        self.arrival_minutes_before.setRange(15, 120)
        self.arrival_minutes_before.setValue(30)
        self.arrival_minutes_before.setSingleStep(5)
        self.arrival_minutes_before.setSuffix(" minutes before performance")

        arrival_hbox.addWidget(self.arrival_minutes_before)
        arrival_hbox.addStretch()

        # Setup time field
        setup_widget = QWidget()
        setup_hbox = QHBoxLayout(setup_widget)
        setup_hbox.setContentsMargins(0, 0, 0, 0)

        self.setup_minutes = QSpinBox()
        self.setup_minutes.setRange(5, 60)
        self.setup_minutes.setValue(15)
        self.setup_minutes.setSingleStep(5)
        self.setup_minutes.setSuffix(" minutes")

        setup_hbox.addWidget(self.setup_minutes)
        setup_hbox.addStretch()

        # Add fields to arrival layout
        arrival_layout.addRow("Performer Arrival:", arrival_widget)
        arrival_layout.addRow("Setup Time Required:", setup_widget)

        arrival_group.setLayout(arrival_layout)

        # Create a group box for late arrival policy
        late_group = QGroupBox("Late Arrival Policy")
        late_layout = QVBoxLayout()

        # Create late arrival policy field
        self.late_policy_edit = QTextEdit()
        self.late_policy_edit.setPlaceholderText("Enter policy for late arrivals")
        self.late_policy_edit.setText(
            "Performance fees are based on the agreed time and material costs.\n"
            "If the Client is late, Performer will accommodate if it doesn't interfere with other obligations.\n"
            "The full fee remains due even if performance is shortened at Client's request.\n"
            "If Performer arrives late, time will be made up if mutually agreed.\n"
            "Performer will wait 15 minutes past scheduled start time before considering it canceled per "
            "the cancellation policy."
        )

        late_layout.addWidget(self.late_policy_edit)
        late_group.setLayout(late_layout)

        # Create a group box for schedule changes
        changes_group = QGroupBox("Schedule Changes")
        changes_layout = QVBoxLayout()

        # Create schedule changes policy field
        self.changes_policy_edit = QTextEdit()
        self.changes_policy_edit.setPlaceholderText("Enter policy for schedule changes")
        self.changes_policy_edit.setText(
            "Any changes to the performance date or time must be communicated as soon as possible.\n"
            "Changes requested within 48 hours of the event are subject to performer availability.\n"
            "If a change cannot be accommodated, the original agreement remains in effect or cancellation "
            "policies will apply."
        )

        changes_layout.addWidget(self.changes_policy_edit)
        changes_group.setLayout(changes_layout)

        # Add the group boxes to the main layout
        main_layout.addWidget(arrival_group)
        main_layout.addWidget(late_group)
        main_layout.addWidget(changes_group)

        # Set the layout for this widget
        self.setLayout(main_layout)

        # Load initial data if available
        self.load_from_contract()

    def update_contract(self):
        # Update the contract with data from the form
        self.contract.schedule.arrival_minutes_before = (
            self.arrival_minutes_before.value()
        )
        self.contract.schedule.setup_minutes = self.setup_minutes.value()
        self.contract.schedule.late_policy = self.late_policy_edit.toPlainText()
        self.contract.schedule.changes_policy = self.changes_policy_edit.toPlainText()

    def load_from_contract(self):
        # Update form fields with data from the contract
        self.arrival_minutes_before.setValue(
            self.contract.schedule.arrival_minutes_before
        )
        self.setup_minutes.setValue(self.contract.schedule.setup_minutes)
        self.late_policy_edit.setText(self.contract.schedule.late_policy)
        self.changes_policy_edit.setText(self.contract.schedule.changes_policy)
