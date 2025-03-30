# ui/section_forms/base_form.py
from PyQt6.QtWidgets import QWidget

class BaseForm(QWidget):
    """Base class for all section forms"""
    
    def __init__(self, contract):
        super().__init__()
        self.contract = contract
        self.init_ui()
    
    def init_ui(self):
        """Initialize the UI components - to be implemented by subclasses"""
        pass
    
    def update_contract(self):
        """Update the contract with data from the form - to be implemented by subclasses"""
        pass
    
    def load_from_contract(self):
        """Load data from the contract to the form - to be implemented by subclasses"""
        pass