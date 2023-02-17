"""Test module for the application."""
import os
from pathlib import Path
from unittest.mock import MagicMock
import pytest
from general.export import PdfExport, CsvExport
from src.dtos.accounts_dto import AccountDTO
from src.controllers.login_controller import LoginController


@pytest.fixture
def account_dto():
    """Fixture for the account dto"""
    return AccountDTO("test", 1, "test", 100, [])


@pytest.fixture
def login_controller():
    """Fixture for the login controller"""
    view_mock = MagicMock()
    return LoginController(view_mock)


def test_pdf_exporter(account_dto):
    """Test the pdf exporter"""
    pdf_export = PdfExport()
    pdf_export.create(account_dto, "test.pdf")
    path = Path('./test.pdf')
    assert path.is_file() is True
    os.remove("test.pdf")


def test_csv_exporter(account_dto):
    """Test the csv exporter"""
    csv_export = CsvExport()
    csv_export.create(account_dto, "test.csv")
    path = Path('./test.csv')
    assert path.is_file() is True
    os.remove("test.csv")


def test_csv_exporter_with_wrong_path(account_dto):
    """Test the csv exporter with a wrong path"""
    csv_export = CsvExport()
    csv_export.create(account_dto, "test.csv")
    path = Path('./tesht.csv')
    assert path.is_file() is False
    os.remove("test.csv")
