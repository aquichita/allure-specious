# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from pathlib import Path

from specious.reports import allure_email_handler


from pathlib import Path

result = Path(".").resolve().parent
allure_email_handler(
    results_dir=result.joinpath("allure-results"),
    allure_config=dict(
        protocol="http", host="", port="", task=""
    ),
    email_config=dict(
        sender="",
        pwd="",
        host="smtphm.qiye.163.com",
        port=465,
        smtp_ssl=True,
        address="",
        subject="HTMS AUTOMATED REPORT",
    ),
)

