# ui/section_forms/services_form.py
from PyQt6.QtWidgets import (
    QLabel,
    QLineEdit,
    QVBoxLayout,
    QFormLayout,
    QGroupBox,
    QComboBox,
    QTextEdit,
    QTimeEdit,
    QSpinBox,
    QHBoxLayout,
    QWidget,
    QCheckBox,
)
from PyQt6.QtCore import Qt, QTime
from ui.section_forms.base_form import BaseForm


class ServicesForm(BaseForm):
    """Form for editing services information"""

    def init_ui(self):
        # Main layout
        main_layout = QVBoxLayout()

        # Create a group box for service details
        services_group = QGroupBox("Performance Details")
        services_layout = QFormLayout()

        # Create form fields for services
        self.performance_type_edit = QLineEdit()
        self.performance_type_edit.setPlaceholderText(
            "e.g., Stilt Walker, Dancer, Fire Performance"
        )

        # Create a widget for duration with time selector
        duration_widget = QWidget()
        duration_layout = QHBoxLayout(duration_widget)
        duration_layout.setContentsMargins(0, 0, 0, 0)

        self.duration_minutes = QSpinBox()
        self.duration_minutes.setRange(1, 300)  # 1 minute to 5 hours
        self.duration_minutes.setValue(4)  # Default 4 minutes
        self.duration_minutes.setSuffix(" minutes")

        duration_layout.addWidget(self.duration_minutes)
        duration_layout.addStretch()

        # Create time field with TBD option
        time_widget = QWidget()
        time_layout = QHBoxLayout(time_widget)
        time_layout.setContentsMargins(0, 0, 0, 0)

        self.time_tbd_checkbox = QCheckBox("TBD")
        self.time_tbd_checkbox.setChecked(True)

        self.time_edit = QTimeEdit()
        self.time_edit.setDisplayFormat("h:mm AP")
        self.time_edit.setTime(QTime(18, 0))  # Default 6:00 PM
        self.time_edit.setEnabled(False)

        # Connect checkbox to enable/disable time edit
        self.time_tbd_checkbox.toggled.connect(
            lambda checked: self.time_edit.setEnabled(not checked)
        )

        time_layout.addWidget(self.time_tbd_checkbox)
        time_layout.addWidget(self.time_edit)
        time_layout.addStretch()

        # Costume field
        self.costume_edit = QLineEdit()
        self.costume_edit.setPlaceholderText("e.g., Caribbean-themed stilt costume")

        # Music field with options
        music_widget = QWidget()
        music_layout = QHBoxLayout(music_widget)
        music_layout.setContentsMargins(0, 0, 0, 0)

        self.music_provided_by = QComboBox()
        self.music_provided_by.addItems(
            ["Client", "Performer", "Venue", "None Required"]
        )

        self.music_notes = QLineEdit()
        self.music_notes.setPlaceholderText("Additional notes about music")

        music_layout.addWidget(QLabel("Provided by:"))
        music_layout.addWidget(self.music_provided_by)
        music_layout.addWidget(QLabel("Notes:"))
        music_layout.addWidget(self.music_notes)

        # Additional services description
        self.additional_services_edit = QTextEdit()
        self.additional_services_edit.setPlaceholderText(
            "Describe any additional services or special requests"
        )
        self.additional_services_edit.setMaximumHeight(100)

        # Add fields to services layout
        services_layout.addRow("Performance Type:", self.performance_type_edit)
        services_layout.addRow("Duration:", duration_widget)
        services_layout.addRow("Performance Time:", time_widget)
        services_layout.addRow("Costume:", self.costume_edit)
        services_layout.addRow("Music:", music_widget)
        services_layout.addRow("Additional Services:", self.additional_services_edit)

        # Set the form layout for the services group
        services_group.setLayout(services_layout)

        # Add the group boxes to the main layout
        main_layout.addWidget(services_group)
        main_layout.addStretch()

        # Set the layout for this widget
        self.setLayout(main_layout)

        # Load initial data if available
        self.load_from_contract()

    def update_contract(self):
        # Update the contract with data from the form
        self.contract.services.performance_type = self.performance_type_edit.text()
        self.contract.services.duration_minutes = self.duration_minutes.value()
        self.contract.services.time_tbd = self.time_tbd_checkbox.isChecked()
        self.contract.services.performance_time = (
            self.time_edit.time().toString("h:mm AP")
            if not self.time_tbd_checkbox.isChecked()
            else "TBD"
        )
        self.contract.services.costume = self.costume_edit.text()
        self.contract.services.music_provided_by = self.music_provided_by.currentText()
        self.contract.services.music_notes = self.music_notes.text()
        self.contract.services.additional_services = (
            self.additional_services_edit.toPlainText()
        )

    def load_from_contract(self):
        # Update form fields with data from the contract
        self.performance_type_edit.setText(self.contract.services.performance_type)
        self.duration_minutes.setValue(self.contract.services.duration_minutes)

        self.time_tbd_checkbox.setChecked(self.contract.services.time_tbd)
        if (
            not self.contract.services.time_tbd
            and self.contract.services.performance_time != "TBD"
        ):
            try:
                time = QTime.fromString(
                    self.contract.services.performance_time, "h:mm AP"
                )
                if time.isValid():
                    self.time_edit.setTime(time)
            except:
                pass

        self.costume_edit.setText(self.contract.services.costume)

        # Set music provider if it matches one of our options
        index = self.music_provided_by.findText(
            self.contract.services.music_provided_by
        )
        if index >= 0:
            self.music_provided_by.setCurrentIndex(index)

        self.music_notes.setText(self.contract.services.music_notes)
        self.additional_services_edit.setText(
            self.contract.services.additional_services
        )
