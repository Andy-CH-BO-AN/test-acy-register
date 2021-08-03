import time
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
import random

url = 'https://acy.com/en/open-live-account'
edge_path = EdgeChromiumDriverManager().install()
driver = webdriver.Edge(edge_path)
driver.get(url)


# 定位參數
class Keyword:
    country_list = ['China', 'Taiwan']
    select_language_box = '/html/body/div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]'
    select_language_name = '//*[@id="gatsby-focus-wrapper"]/div[1]/div[2]/div[2]/div[2]/div[2]/div/*/p[text() = ' \
                           '"English"] '
    select_language_confirm = '/html/body/div[1]/div[1]/div[1]/div[2]/div[3]/a'
    account_type_box = '/html/body/div[1]/div[1]/div/div/div[1]/div/div/div/div/div[2]/div/div/div[' \
                       '2]/div/div/form/div[1]/div/div/div[1] '
    account_type_personal = '/html/body/div[1]/div[1]/div/div/div[1]/div/div/div/div/div[2]/div/div/div[' \
                            '2]/div/div/form/div[1]/div/div/div[2]/div/li[1] '
    country_name_box = '//*[@id="gatsby-focus-wrapper"]/div/div/div[1]/div/div/div/div/div[2]/div/div/div[' \
                       '2]/div/div/form/div[2]/div/div/div/div/div[1]/div '
    select_country = f'//*[@id="liWrapper"]/*[text()="{random.choice(country_list)}"]'


def register():
    for i in range(2):
        print(i)
        time.sleep(3)
        driver.find_element_by_xpath(Keyword.select_language_box).click()
        driver.find_element_by_xpath(Keyword.select_language_name).click()
        driver.find_element_by_xpath(Keyword.select_language_confirm).click()
    # select account type
    driver.find_element_by_xpath(Keyword.account_type_box).click()
    driver.find_element_by_xpath(Keyword.account_type_personal).click()
    # select country
    driver.find_element_by_xpath(Keyword.country_name_box).click()
    driver.find_element_by_xpath(Keyword.select_country).click()


if __name__ == '__main__':
    register()
