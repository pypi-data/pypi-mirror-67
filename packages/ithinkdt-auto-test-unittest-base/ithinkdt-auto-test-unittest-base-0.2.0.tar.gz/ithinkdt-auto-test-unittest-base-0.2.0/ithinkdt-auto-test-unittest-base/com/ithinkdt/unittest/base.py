# 封装基本方法，包括元素查找，元素定位
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Base(object):

    def __init__(self, driver: webdriver, timeout=10):
        self.driver = driver
        self.timeout = timeout

    def find_element(self, by: str, location: str) -> WebElement:
        """
        find element by location
        :param by: xpath, name, id ...
        :param location:  //*[name = 'add']
        :return: WebElement
        :Usage:
            locator = ('xpath', //*[@id='location'])
            element = driver.find_element(*locator)
        """
        by = by.lower()
        wait = WebDriverWait(self.driver, self.timeout)
        element = wait.until(lambda driver: driver.find_element(by, location))
        return element

    def find_elements(self, by: str, location: str) -> list:
        """
        find elements by location
        :param by: xpath, name, id ...
        :param location: //*[name = 'add']
        :return:
        """
        by = by.lower()
        wait = WebDriverWait(self.driver, self.timeout)
        elements = wait.until(lambda driver: driver.find_elements(by, location))
        return elements

    def is_element_exist(self, by: str, location: str)->bool:
        """
        if element is exist return true else return false
         :param by: xpath, name, id ...
        :param location:  //*[name = 'add']
        :return: bool
        """
        self.timeout = 10
        by.lower()
        try:
            wait = WebDriverWait(self.driver, self.timeout)
            wait.until(ec.visibility_of_element_located((by, location)))
        except (NoSuchElementException, TimeoutException):
            return False
        return True

    def is_clickable(self, by: str, location: str):
        """
        if element is klickable return true else return false
        :param by:
        :param location:
        :return: bool
        """
        by.lower()
        wait = WebDriverWait(self.driver, self.timeout)
        element = wait.until(ec.element_to_be_clickable((by, location)))
        return element

    def click(self, by: str, location: str):
        """
        单个元素进行点击，
        :param by:
        :param location:
        :return:
        """
        by.lower()
        wait = WebDriverWait(self.driver, self.timeout)
        element = wait.until(ec.visibility_of_element_located((by, location)))
        element.click()

    # 当加上@property属性后，可以直接按照访问属性的方式去访问方法，即去掉方法名后面的（）
    # 页面中调用时，该被调用的方法（base文件内）若加上@property属性，则self.get_alert_text
    # @property
    def is_alert_switch_to_it(self):
        """
        当为alert弹框时，采用这个方法 但是项目中是div弹框，不是alert
        :return:
        """
        self.timeout = 10
        wait = WebDriverWait(self.driver, self.timeout)
        alert = wait.until(ec.alert_is_present())
        return alert

