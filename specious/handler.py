import os
import sys
from datetime import datetime
from io import BytesIO
from pathlib import Path
from PIL import Image

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
# options.debugger_address = "127.0.0.1:9222"
# options.add_argument('--headless')
options.add_argument('--disable-gpu')


def test_tng():
    driver = webdriver.Chrome("chromedriver.exe", options=options)
    driver.get("http://172.23.16.3:7000/login")
    driver.maximize_window()
    driver.find_element_by_id("j_username").send_keys("26301")
    driver.find_element_by_name("j_password").send_keys("8835622")
    driver.find_element_by_name("Submit").click()
    driver.set_page_load_timeout(30)
    driver.find_element_by_partial_link_text("htms-op-ui-automation-test").click()
    driver.find_element_by_link_text("Allure Report").click()

    allure_report = driver.get_screenshot_as_png()
    ###
    allure_bytes = Image.open(BytesIO(allure_report))

    summary = driver.find_element_by_xpath("//*[@data-id='summary']")
    trend = driver.find_element_by_css_selector(".history-trend")
    report = driver.find_element_by_css_selector(".app__content")

    s_x, s_y = summary.location.values()
    height = summary.size.get("height")
    width = summary.size.get("width")
    summary_pic = allure_bytes.crop((s_x, s_y, s_x + width, s_y + height))
    summary_pic.save('summary.png')

    r_x, r_y = report.location.values()
    height = report.size.get("height")
    width = report.size.get("width")
    report_pic = allure_bytes.crop((r_x, r_y, r_x + width, r_y + height))
    report_pic.save('report.png')

    driver.quit()
