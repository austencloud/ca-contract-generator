# ui/section_forms/obligations_form.py
from PyQt6.QtWidgets import QVBoxLayout, QGroupBox, QTextEdit, QLabel
from ui.section_forms.base_form import BaseForm


class ObligationsForm(BaseForm):
    """Form for editing obligations of both parties"""

    def init_ui(self):
        # Main layout
        main_layout = QVBoxLayout()

        # Create a group box for producer obligations
        producer_group = QGroupBox("Producer Obligations")
        producer_layout = QVBoxLayout()

        # Create producer obligations field
        self.producer_obligations_edit = QTextEdit()
        self.producer_obligations_edit.setPlaceholderText(
            "Enter obligations for the producer/performer"
        )
        self.producer_obligations_edit.setText(
            "• Will ensure timely preparation and optimal performance delivery.\n"
            "• Will maintain confidentiality of Client information.\n"
            "• Will arrive with all necessary performance equipment and costumes.\n"
            "• May substitute another Cirque Aflame performer with Client's consent, if needed.\n"
            "• Will maintain professional conduct throughout the engagement.\n"
            "• Will collaborate with venue staff to ensure smooth integration."
        )

        producer_layout.addWidget(self.producer_obligations_edit)
        producer_group.setLayout(producer_layout)

        # Create a group box for client obligations
        client_group = QGroupBox("Client Obligations")
        client_layout = QVBoxLayout()

        # Create client obligations field
        self.client_obligations_edit = QTextEdit()
        self.client_obligations_edit.setPlaceholderText(
            "Enter obligations for the client"
        )
        self.client_obligations_edit.setText(
            "• Will ensure a safe and hazard-free area for performance.\n"
            "• Will adhere to all terms and event setup responsibilities.\n"
            "• Will provide accurate information regarding venue, audience, and technical requirements.\n"
            "• Will ensure adequate space for performance and setup.\n"
            "• Will ensure that the venue permits the type of performance contracted.\n"
            "• Will inform Performer of any special circumstances that may affect the performance."
        )

        client_layout.addWidget(self.client_obligations_edit)
        client_group.setLayout(client_layout)

        # Create a group box for venue requirements
        venue_group = QGroupBox("Venue and Technical Requirements")
        venue_layout = QVBoxLayout()

        # Create venue requirements field
        self.venue_requirements_edit = QTextEdit()
        self.venue_requirements_edit.setPlaceholderText(
            "Enter any specific venue or technical requirements"
        )
        self.venue_requirements_edit.setText(
            "• Performance area must have sufficient ceiling height for stilt walking (minimum 10 feet).\n"
            "• Floor surface must be smooth, level, and free of debris, cracks, or uneven surfaces.\n"
            "• A secure changing area must be provided for the Performer.\n"
            "• Adequate lighting for safe performance.\n"
            "• If outdoors, a covered area must be available in case of inclement weather."
        )

        venue_layout.addWidget(self.venue_requirements_edit)
        venue_group.setLayout(venue_layout)

        # Add the group boxes to the main layout
        main_layout.addWidget(producer_group)
        main_layout.addWidget(client_group)
        main_layout.addWidget(venue_group)

        # Set the layout for this widget
        self.setLayout(main_layout)

        # Load initial data if available
        self.load_from_contract()

    def update_contract(self):
        # Update the contract with data from the form
        self.contract.obligations.producer_obligations = (
            self.producer_obligations_edit.toPlainText()
        )
        self.contract.obligations.client_obligations = (
            self.client_obligations_edit.toPlainText()
        )
        self.contract.obligations.venue_requirements = (
            self.venue_requirements_edit.toPlainText()
        )

    def load_from_contract(self):
        # Update form fields with data from the contract
        self.producer_obligations_edit.setText(
            self.contract.obligations.producer_obligations
        )
        self.client_obligations_edit.setText(
            self.contract.obligations.client_obligations
        )
        self.venue_requirements_edit.setText(
            self.contract.obligations.venue_requirements
        )
