import os

from pathlib import Path

from PIL.Image import Image
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


def select_lg(driver: WebDriver, lg: str):
    """选择Allure报告语言
    :param driver:
    :param lg: en, ru, zh...
    :return:
    """
    driver.find_element_by_css_selector(".side-nav__item button").click()
    driver.find_element_by_css_selector(f"[data-id='{lg}']").click()


current = Path(".").resolve()


def clear(name: str):
    """清理历史数据"""
    absolute = current / Path(f'{name}.png')
    if absolute.exists():
        os.remove(str(absolute))
    return str(absolute)


def png(name: str, element: WebElement, binary: Image) -> str[Path]:
    """根据该图片对应页面元素及整个页面截图二进制数据获取指定元素图片
    :param name:
    :param element:
    :param binary:
    :return:
    """
    absolute = clear(name)
    x, y = element.location.values()
    height = element.size.get("height")
    width = element.size.get("width")
    pic = binary.crop((x, y, x + width, y + height))
    pic.save(absolute)
    return absolute


class Graphs:
    def __init__(self, binary: Image, driver: WebDriver, language: str = "zh"):
        self.driver = driver
        self.binary = binary
        self.driver.find_element_by_css_selector("[data-tooltip='Graphs']").click()
        select_lg(self.driver, lg=language)

    def status(self, name: str = "status"):
        status = self.driver.find_element_by_css_selector("[data-id='status-chart']")
        return png(name, status, self.binary)

    def trend(self, name: str = "trend"):
        trend = self.driver.find_element_by_css_selector("[data-id='history-trend']")
        return png(name, trend, self.binary)
