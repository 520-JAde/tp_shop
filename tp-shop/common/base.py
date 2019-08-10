from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
# 导入下拉框的包
from selenium.webdriver.support.ui import Select
from appium.webdriver.common.touch_action import TouchAction


def open_mobile():
    """配置手机参数,打开手机"""
    desired_caps = {}
    desired_caps["platformName"] = "android"
    desired_caps["platformVersion"] = "5.1.1"
    desired_caps["deviceName"] = "127.0.0.1:21503"
    desired_caps["appPackage"] = "com.tpshop.malls"
    desired_caps["appActivity"] = ".SPMainActivity"
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    driver = webdriver.Remote ("127.0.0.1:4723/wd/hub", desired_caps)

    return driver


class Base:
    """封装appium的基础操作的类"""

    def __init__(self, driver):
        """绑定手机参数"""
        self.driver = driver
        size = self.driver.get_window_size ()
        self.height = size["height"]
        self.width = size["width"]

    def back_key(self):
        """返回键"""
        self.driver.back ()

    def close_mobile(self):
        """关闭手机"""
        self.driver.quit ()

    def find_element(self, locator, timeout=10):
        """
        查找单个元素的方法,返回的是一个元素
        :param locator: 定位器
        :param timeout: 显式等待的时间
        :return: 返回查找到的元素
        """
        try:
            element = WebDriverWait (self.driver, timeout, 0.1).until (EC.presence_of_element_located (locator))
            return element
        except:
            pass

    def find_elements(self, locator, timeout=10):
        """
        定位多个元素,返回的含有多个元素的列表
        :param locator: 定位器
        :param timeout: 显式等待(定位到你要查找的元素所等待的最大时间)的时间
        :return: 包含多个元素的列表
        """
        try:
            elements = WebDriverWait (self.driver, timeout).until (EC.presence_of_all_elements_located (locator))
            return elements
        except:
            pass

    def click(self, locator, timeout=10):
        """
        封装点击元素的操作
        :param locator: 定位器
        :param timeout: 显式等待的时间
        :return:
        """
        element = self.find_element (locator, timeout)
        element.click ()

    def back(self):
        """点击返回"""
        self.driver.back ()

    def send_keys(self, locator, text, timeout=10):
        """
        封装发送文本的操作
        :param locator: 定位器
        :param text: 要输入的内容
        :param timeout: 显式等待的时间
        :return:
        """
        element = self.find_element (locator, timeout)
        element.clear ()
        element.send_keys (text)

    def tap_tap(self,x,y):
        """坐标定位"""
        TouchAction(self.driver).tap(x=x,y=y).perform()

    def up_slither(self):
        """向上滑动"""
        self.driver.swipe (self.width * 0.2, self.height * 0.9, self.width * 0.2, self.height * 0.2)

    def down_slither(self):
        """向下滑动"""
        self.driver.swipe (self.width * 0.2, self.height * 0.2, self.width * 0.2, self.height * 0.9)

    def left_slither(self):
        """向左滑动"""
        self.driver.swipe (self.width * 0.9, self.height * 0.2, self.width * 0.2, self.height * 0.2)

    def right_slither(self):
        """向右滑动"""
        self.driver.swipe (self.width * 0.2, self.height * 0.2, self.width * 0.9, self.height * 0.2)

    def screenshot(self, file_path):
        """截屏"""
        self.driver.get_screenshot_as_file (file_path)


if __name__ == '__main__':
    driver = open_mobile ()
    base = Base (driver)
    base.up_slither ()
