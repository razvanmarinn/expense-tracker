"""This module contains the Exporter class and its subclasses."""
from abc import ABC, abstractmethod
from fpdf import FPDF
from dtos.accounts_dto import AccountDTO


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
        self.pdf.set_font('Arial', size=12)
        self.pdf.set_text_color(0,0,255)
        self.pdf.set_fill_color(255,255,0)
        self.pdf.cell(200, 10, txt="Account name: " + AccountDTO.account_uuid, ln=1, align="C",fill=True)
        self.pdf.cell(200, 10, txt="Account balance: " + str(AccountDTO.balance), ln=1, align="C",fill=True)
        self.pdf.cell(200, 10, txt="Transactions: ", ln=1, align="C")
        self.pdf.set_draw_color(255, 0, 0)
        self.pdf.set_line_width(1)
        self.pdf.line(20, 40, 190, 40)
        self.pdf.set_text_color(255,0,0)
        for transaction in AccountDTO.transactions:
            self.pdf.cell(200, 10, txt= str(transaction), ln=1, align="C")

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
        self.csv += "Account name: " + AccountDTO.account_uuid + "\n"
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
