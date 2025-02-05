from pytest import raises
from pydantic import ValidationError

import app
from .test_data import TEST_CASES, RECEIPTS_WITH_BAD_DATA, RECEIPTS_WITH_INCOMPLETE_DATA


# TODO: always more tests...


def _test_receipt_points(payload, expected):
    receipt = app.Receipt(**payload)
    assert receipt.points == expected


def test_receipt_points():
    for test_case in TEST_CASES:
        payload = test_case["payload"]
        expected = test_case["expected"]
        _test_receipt_points(payload, expected)


def _test_incomplete_receipts(payload):
    with raises(ValidationError):
        receipt = app.Receipt(**payload)


def test_incomplete_receipts():
    for incomplete_receipt in RECEIPTS_WITH_INCOMPLETE_DATA:
        _test_incomplete_receipts(incomplete_receipt)


def _test_bad_receipts(payload):
    with raises(ValidationError):
        receipt = app.Receipt(**payload)


def test_bad_receipts():
    for bad_receipt in RECEIPTS_WITH_BAD_DATA:
        _test_bad_receipts(bad_receipt)
