"""Test dcat validation."""
from data_catalog_dcat_validator import dcat_validator
import pytest

from contextlib import contextmanager


@contextmanager
def not_raises(ExpectedException):
    try:
        yield

    except ExpectedException as error:
        raise AssertionError(f"Raised exception {error} when it should not!")

    except Exception as error:
        raise AssertionError(f"An unexpected exception {error} raised.")


metadata = {
    "title": "Zimbabwe Regional Geochemical Survey.",
    "description": "During the period 1982-86 a team of geologists ...",
    "identifier": "9df8df51-63db-37a8-e044-0003ba9b0d98",
    "landingPage": "http://some.source.url.com",
    "issued": "2012-05-10",
    "modified": "2012-05-10T21:04",
    "language": ["en", "es", "ca"],
    "keyword": [
        "exploration",
        "geochemical-exploration",
        "geochemical-maps",
        "geochemistry",
        "geology",
        "nercddc",
        "regional-geology",
    ],
    "publisher": {"name": "Geological Society", "mbox": "info@gs.org"},
    "distribution": [
        {
            "accessURL": "http://www.bgs.ac.uk/gbase/geochemcd/home.html",
            "byteSize": 235,
            "description": "Resource locator",
            "format": "text/html",
            "title": "",
        }
    ],
}


def test_metadata_validation() -> None:
    """Test metadata validation."""
    ds = dcat_validator.Dataset(metadata)
    errors = ds.validate()
    assert len(errors) == 2


def test_string_validator_good_input() -> None:
    """Test string validation of valid input."""
    validator = dcat_validator.StringValidator()
    validator.validate("test")


def test_string_validator_bad_input() -> None:
    """Test string validation raise error for bad input."""
    validator = dcat_validator.StringValidator()
    with pytest.raises(Exception):
        validator.validate(22)


def test_int_validator_good_input() -> None:
    """Test integer validation of valid input."""
    validator = dcat_validator.IntValidator()
    validator.validate(22)


def test_int_validator_bad_input() -> None:
    """Test integer validation raise error for bad input."""
    validator = dcat_validator.IntValidator()
    with pytest.raises(Exception):
        validator.validate("test")


def test_date_validator_good_input() -> None:
    """Test date validation of valid input."""
    validator = dcat_validator.DateValidator()
    validator.validate("1970-01-01")


def test_date_validator_bad_input() -> None:
    """Test date validation raise error for bad input."""
    validator = dcat_validator.DateValidator()
    with pytest.raises(Exception):
        validator.validate("Not a date")


def test_email_validator_good_input() -> None:
    """Test email validation of valid input"""
    validator = dcat_validator.EmailValidator()
    validator.validate("test.test@test.test")


def test_email_validator_bad_input() -> None:
    """Test email validation of valid input"""
    validator = dcat_validator.EmailValidator()
    with pytest.raises(Exception):
        validator.validate("test")
