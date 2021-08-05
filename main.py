import time
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
import random

url = 'https://acy.com/en/open-live-account'
edge_path = EdgeChromiumDriverManager().install()
driver = webdriver.Edge(edge_path)
driver.get(url)
driver.maximize_window()


class Locator:
    """
    locators
    """
    country_list = ['China', 'Taiwan']
    select_language_box = '/html/body/div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]'
    select_language_name = '//*[@id="gatsby-focus-wrapper"]/div[1]/div[2]/div[2]/div[2]/div[2]/div/*/p[text() = ' \
                           '"English"] '
    select_language_confirm = '/html/body/div[1]/div[1]/div[1]/div[2]/div[3]/a'
    select_account_type_box = '//*[@id="gatsby-focus-wrapper"]/div/div/div[1]/div/div/div/div/div[2]/div/div/div[' \
                              '2]/div/div/form/div[1]/div/div '
    select_account_type_personal = '/html/body/div[1]/div[1]/div/div/div[1]/div/div/div/div/div[2]/div/div/div[' \
                                   '2]/div/div/form/div[1]/div/div/div[2]/div/li[1] '
    select_country_name_box = '//*[@id="gatsby-focus-wrapper"]/div/div/div[1]/div/div/div/div/div[2]/div/div/div[' \
                              '2]/div/div/form/div[2]/div/div/div/div/div[1]/div '
    select_country = f'//*[@id="liWrapper"]/*[text()="{random.choice(country_list)}"]'
    select_title_box = '/html/body/div[1]/div[1]/div/div/div[1]/div/div/div/div/div[2]/div/div/div[2]/div/div/form/div[' \
                       '3]/div/div/div[1] '
    # css selector
    select_title = f'li[data-testid="title{random.randint(0, 4)}"]'
    input_first_name = '/html/body/div[1]/div[1]/div/div/div[1]/div/div/div/div/div[2]/div/div/div[' \
                       '2]/div/div/form/div[4]/div/input '
    input_middle_name = '/html/body/div[1]/div[1]/div/div/div[1]/div/div/div/div/div[2]/div/div/div[' \
                        '2]/div/div/form/div[5]/div/input '
    input_last_name = '/html/body/div[1]/div[1]/div/div/div[1]/div/div/div/div/div[2]/div/div/div[' \
                      '2]/div/div/form/div[6]/div/input '
    input_email = '/html/body/div[1]/div[1]/div/div/div[1]/div/div/div/div/div[2]/div/div/div[2]/div/div/form/div[' \
                  '7]/div/input '
    select_country_code_box = '//*[@id="gatsby-focus-wrapper"]/div/div/div[1]/div/div/div/div/div[2]/div/div/div[' \
                              '2]/div/div/form/div[8]/div[1]/div/div[1]/div '
    # css selector
    select_country_code = f'li[data-testid="undefined{random.randint(0, 241)}"]'
    input_phone_number = '//*[@id="gatsby-focus-wrapper"]/div/div/div[1]/div/div/div/div/div[2]/div/div/div[' \
                         '2]/div/div/form/div[8]/div[1]/div/div[2]/div/div/input '
    button_get_otp_code = '/html/body/div[1]/div[1]/div/div/div[1]/div/div/div/div/div[2]/div/div/div[' \
                          '2]/div/div/form/div[8]/div[2]/div/div/div[1]/button '
    input_otp_code = '/html/body/div[1]/div[1]/div/div/div[1]/div/div/div/div/div[2]/div/div/div[2]/div/div/form/div[' \
                     '8]/div[2]/div/div/div[2]/div/div/input '
    button_next_page = '/html/body/div[1]/div[1]/div/div/div[1]/div/div/div/div/div[2]/div/div/div[' \
                       '2]/div/div/form/button '
    select_gender_box = ''


def register_personal_detail():
    WebDriverWait(driver, 5, 0.5). \
        until(ec.element_to_be_clickable((By.XPATH, Locator.select_language_confirm)))
    # select language box
    driver.find_element_by_xpath(Locator.select_language_box).click()
    driver.find_element_by_xpath(Locator.select_language_name).click()
    driver.find_element_by_xpath(Locator.select_language_confirm).click()
    # select account type
    driver.find_element_by_xpath(Locator.select_account_type_box).click()
    driver.find_element_by_xpath(Locator.select_account_type_personal).click()
    # select country
    driver.find_element_by_xpath(Locator.select_country_name_box).click()
    driver.find_element_by_xpath(Locator.select_country).click()
    # select title
    driver.find_element_by_xpath(Locator.select_title_box).click()
    driver.find_element_by_css_selector(Locator.select_title).click()
    # input first name
    driver.find_element_by_xpath(Locator.input_first_name).clear()
    driver.find_element_by_xpath(Locator.input_first_name).send_keys('first name')
    # input middle name
    driver.find_element_by_xpath(Locator.input_middle_name).clear()
    driver.find_element_by_xpath(Locator.input_middle_name).send_keys('middle name')
    # input last name
    driver.find_element_by_xpath(Locator.input_last_name).clear()
    driver.find_element_by_xpath(Locator.input_last_name).send_keys('last name')
    # input email
    driver.find_element_by_xpath(Locator.input_email).clear()
    driver.find_element_by_xpath(Locator.input_email).send_keys(f'a{random.randint(0, 1000)}a@a.com')
    # hover on country code box
    hover = ActionChains(driver).move_to_element(driver.find_element_by_xpath(Locator.select_country_code_box))
    hover.perform()
    # select country code
    driver.find_element_by_xpath(Locator.select_country_code_box).click()
    driver.find_element_by_css_selector(Locator.select_country_code).click()
    # input phone number
    driver.find_element_by_xpath(Locator.input_phone_number).send_keys(random.randint(100000000, 999999999))
    # get code
    driver.find_element_by_xpath(Locator.button_get_otp_code).click()
    # input opt code
    driver.find_element_by_xpath(Locator.input_otp_code).send_keys(random.randint(100000000, 999999999))
    # wait next button clickable
    WebDriverWait(driver, 5, 0.5). \
        until(ec.element_to_be_clickable((By.XPATH, Locator.button_next_page)))
    # click next button to next page
    driver.find_element_by_xpath(Locator.button_next_page).click()


def register_about_you():
    pass


def register_investment():
    pass


def register_experience():
    pass


def register_terms_and_conditions():
    pass


def confirm_ID():
    pass


if __name__ == '__main__':
    register_personal_detail()
    register_about_you()
