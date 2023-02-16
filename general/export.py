"""This module contains the Exporter class and its subclasses."""
from abc import ABC, abstractmethod
from fpdf import FPDF
from src.dtos.accounts_dto import AccountDTO
from datetime import datetime

class Exporter(ABC):
    """Exporter class"""
    @abstractmethod
    def create(self, AccountDTO: AccountDTO, output: str):
        """Create method"""
    @abstractmethod
    def output(self, name):
        """Output method"""

class PdfExport(Exporter):
    """PdfExport class"""
    def __init__(self):
        self.pdf = FPDF()

    def create(self, AccountDTO: AccountDTO, output: str):
        """Create pdf method"""
        self.pdf.add_page()
        self.pdf.set_font('Times', size=14)
        self.pdf.set_text_color(0,0,0)
        self.pdf.cell(0, 20, txt="Expense tracker", ln=1, align="C")
        self.pdf.cell(0, 10, txt="Account Statement", ln=1, align="C")
        self.pdf.line(10, 40, 200, 40)
        self.pdf.cell(0, 10, txt="", ln=1)
        # Add account details
        self.pdf.set_font('Times', size=12)
        self.pdf.cell(0, 10, txt="Account Name: " + AccountDTO.name, ln=1, align="L")
        self.pdf.cell(0, 10, txt="Account Balance: $" + str(AccountDTO.balance), ln=1, align="L")
        self.pdf.set_line_width(0.5)
        self.pdf.line(10, self.pdf.get_y(), self.pdf.w - 10, self.pdf.get_y())
        # Add transactions
        self.pdf.cell(0, 10, txt="Transactions:", ln=1, align="L")
        self.pdf.set_line_width(0.5)
        self.pdf.line(10, self.pdf.get_y(), self.pdf.w - 10, self.pdf.get_y())
        # Create the heading string
        heading = '{:<8} {:<15} {:<10} {:<15} {:<10} {:<10}'.format("ID", "Name", "Balance", "Date", "Type", "Account_Id")

        # Add the heading to the PDF
        self.pdf.cell(0, 10, txt=heading, ln=1)
        for transaction in AccountDTO.transactions:
            transaction_str = '{:<8} {:<15} {:<10} {:<15} {:<10} {:<10}'.format(*transaction) # Format the transaction
            self.pdf.cell(0, 10, txt=transaction_str, ln=1)
        self.pdf.cell(0, 10, txt="", ln=1)
        # Add footer with date, time, and page number
        self.pdf.line(10, 280, 200, 280) # Add border line above the footer
        self.pdf.cell(0, 10, txt="Generated on: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"), ln=1, align="L")
        self.pdf.cell(0, 10, txt="Page " + str(self.pdf.page_no()), ln=1, align="R")

        self.output(output)

    def set_font(self, font, size):
        """Set font method"""
        self.pdf.set_font(font, size=size)

    def output(self, name):
        """Output method"""
        self.pdf.output(name)

class CsvExport(Exporter):
    """This class contains the controller for the popup window for creating new accounts"""
    def __init__(self):
        self.csv = ""

    def create(self, AccountDTO: AccountDTO, output: str):
        """Create csv method"""
        self.csv += "Account name: " + AccountDTO.name + "\n"
        self.csv += "Account balance: " + str(AccountDTO.balance) + "\n"
        self.csv += "Transactions: " + "\n"
        for transaction in AccountDTO.transactions:
            self.csv += str(transaction) + "\n"
        self.output(output)

    def output(self, name):
        """Output method"""
        with open(name, "a", encoding="UTF8") as file:
            file.write(self.csv)
            file.close()
