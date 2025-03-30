# ui/section_forms/fees_form.py
from PyQt6.QtWidgets import (
    QLabel,
    QLineEdit,
    QVBoxLayout,
    QFormLayout,
    QGroupBox,
    QComboBox,
    QTextEdit,
    QDoubleSpinBox,
    QCheckBox,
    QHBoxLayout,
    QWidget,
)
from PyQt6.QtCore import Qt
from ui.section_forms.base_form import BaseForm


class FeesForm(BaseForm):
    """Form for editing fees information"""

    def init_ui(self):
        # Main layout
        main_layout = QVBoxLayout()

        # Create a group box for fee details
        fees_group = QGroupBox("Fee Details")
        fees_layout = QFormLayout()

        # Create form fields for fees
        self.total_fee_edit = QDoubleSpinBox()
        self.total_fee_edit.setRange(0, 100000)
        self.total_fee_edit.setPrefix("$")
        self.total_fee_edit.setSingleStep(10)
        self.total_fee_edit.setDecimals(2)

        # Create a widget for the deposit amount with a checkbox
        deposit_widget = QWidget()
        deposit_layout = QHBoxLayout(deposit_widget)
        deposit_layout.setContentsMargins(0, 0, 0, 0)

        self.deposit_checkbox = QCheckBox("Require Deposit")
        self.deposit_checkbox.setChecked(True)

        self.deposit_amount_edit = QDoubleSpinBox()
        self.deposit_amount_edit.setRange(0, 100000)
        self.deposit_amount_edit.setPrefix("$")
        self.deposit_amount_edit.setSingleStep(10)
        self.deposit_amount_edit.setDecimals(2)

        # Update deposit amount when total fee changes (50% by default)
        self.total_fee_edit.valueChanged.connect(self.update_deposit_amount)
        self.deposit_checkbox.toggled.connect(self.deposit_amount_edit.setEnabled)

        deposit_layout.addWidget(self.deposit_checkbox)
        deposit_layout.addWidget(self.deposit_amount_edit)

        # Create remaining balance field (calculated automatically)
        self.balance_edit = QDoubleSpinBox()
        self.balance_edit.setRange(0, 100000)
        self.balance_edit.setPrefix("$")
        self.balance_edit.setDecimals(2)
        self.balance_edit.setReadOnly(True)
        self.balance_edit.setButtonSymbols(QDoubleSpinBox.ButtonSymbols.NoButtons)
        self.balance_edit.setStyleSheet("background-color: #f0f0f0;")

        # Connect signals to update balance
        self.total_fee_edit.valueChanged.connect(self.update_balance)
        self.deposit_amount_edit.valueChanged.connect(self.update_balance)
        self.deposit_checkbox.toggled.connect(self.update_balance)

        # Payment methods
        self.payment_methods_edit = QTextEdit()
        self.payment_methods_edit.setPlaceholderText("List accepted payment methods")
        self.payment_methods_edit.setText("Business check, cash, Venmo, or Zelle.")
        self.payment_methods_edit.setMaximumHeight(80)

        # Add fields to fees layout
        fees_layout.addRow("Total Fee:", self.total_fee_edit)
        fees_layout.addRow("Deposit:", deposit_widget)
        fees_layout.addRow("Remaining Balance:", self.balance_edit)
        fees_layout.addRow("Payment Methods:", self.payment_methods_edit)

        # Set the form layout for the fees group
        fees_group.setLayout(fees_layout)

        # Create a group box for payment terms
        terms_group = QGroupBox("Payment Terms")
        terms_layout = QVBoxLayout()

        # Create field for payment terms
        self.payment_terms_edit = QTextEdit()
        self.payment_terms_edit.setPlaceholderText("Enter payment terms and conditions")
        self.payment_terms_edit.setText(
            "A non-refundable deposit is required within 48 hours of signing.\n"
            "Remaining balance is due immediately upon completion of the performance.\n"
            "Payment may also be made in advance.\n"
            "'Completion' is defined as the end of the performance or the moment the "
            "Performer ceases performing due to unforeseen circumstances. Full payment "
            "remains due unless otherwise agreed in writing."
        )

        terms_layout.addWidget(self.payment_terms_edit)

        # Set the layout for the terms group
        terms_group.setLayout(terms_layout)

        # Add the group boxes to the main layout
        main_layout.addWidget(fees_group)
        main_layout.addWidget(terms_group)

        # Set the layout for this widget
        self.setLayout(main_layout)

        # Load initial data if available
        self.load_from_contract()

    def update_deposit_amount(self):
        # Default deposit is 50% of total fee
        if self.deposit_checkbox.isChecked():
            self.deposit_amount_edit.setValue(self.total_fee_edit.value() / 2)

    def update_balance(self):
        # Calculate remaining balance
        if self.deposit_checkbox.isChecked():
            self.balance_edit.setValue(
                self.total_fee_edit.value() - self.deposit_amount_edit.value()
            )
        else:
            self.balance_edit.setValue(self.total_fee_edit.value())

    def update_contract(self):
        # Update the contract with data from the form
        self.contract.fees.total_fee = self.total_fee_edit.value()
        self.contract.fees.requires_deposit = self.deposit_checkbox.isChecked()
        self.contract.fees.deposit_amount = (
            self.deposit_amount_edit.value() if self.deposit_checkbox.isChecked() else 0
        )
        self.contract.fees.balance = self.balance_edit.value()
        self.contract.fees.payment_methods = self.payment_methods_edit.toPlainText()
        self.contract.fees.payment_terms = self.payment_terms_edit.toPlainText()

    def load_from_contract(self):
        # Update form fields with data from the contract
        self.total_fee_edit.setValue(self.contract.fees.total_fee)
        self.deposit_checkbox.setChecked(self.contract.fees.requires_deposit)
        self.deposit_amount_edit.setValue(self.contract.fees.deposit_amount)
        self.deposit_amount_edit.setEnabled(self.contract.fees.requires_deposit)
        self.balance_edit.setValue(self.contract.fees.balance)
        self.payment_methods_edit.setText(self.contract.fees.payment_methods)
        self.payment_terms_edit.setText(self.contract.fees.payment_terms)
