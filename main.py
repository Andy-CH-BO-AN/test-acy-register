import time
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
import random
import Locators
import os


class Register:
    def main(self):
        global driver
        url = 'https://acycn.com/en/open-live-account'
        edge_path = EdgeChromiumDriverManager().install()
        driver = webdriver.Edge(edge_path)
        driver.get(url)
        driver.maximize_window()

    def personal_detail(self):
        WebDriverWait(driver, 5, 0.5). \
            until(ec.element_to_be_clickable((By.XPATH, Locators.PersonalDetail.select_language_confirm)))
        # select language box
        driver.find_element_by_xpath(Locators.PersonalDetail.select_language_box).click()
        driver.find_element_by_xpath(Locators.PersonalDetail.select_language_name).click()
        driver.find_element_by_xpath(Locators.PersonalDetail.select_language_confirm).click()

        WebDriverWait(driver, 5, 0.5). \
            until(ec.element_to_be_clickable((By.XPATH, Locators.PersonalDetail.select_account_type_box)))
        # select account type
        driver.find_element_by_xpath(Locators.PersonalDetail.select_account_type_box).click()
        driver.find_element_by_xpath(Locators.PersonalDetail.select_account_type_personal).click()
        # select country
        driver.find_element_by_xpath(Locators.PersonalDetail.select_country_name_box).click()
        driver.find_element_by_xpath(Locators.PersonalDetail.select_country).click()
        # select title
        driver.find_element_by_xpath(Locators.PersonalDetail.select_title_box).click()
        driver.find_element_by_css_selector(Locators.PersonalDetail.select_title).click()
        # input first name
        driver.find_element_by_xpath(Locators.PersonalDetail.input_first_name).clear()
        driver.find_element_by_xpath(Locators.PersonalDetail.input_first_name).send_keys('first name')
        # input middle name
        driver.find_element_by_xpath(Locators.PersonalDetail.input_middle_name).clear()
        driver.find_element_by_xpath(Locators.PersonalDetail.input_middle_name).send_keys('middle name')
        # input last name
        driver.find_element_by_xpath(Locators.PersonalDetail.input_last_name).clear()
        driver.find_element_by_xpath(Locators.PersonalDetail.input_last_name).send_keys('last name')
        # input email
        driver.find_element_by_xpath(Locators.PersonalDetail.input_email).clear()
        driver.find_element_by_xpath(Locators.PersonalDetail.input_email).send_keys(
            f'a{random.randint(0, 1000)}a@a.com')
        # hover on country code box
        hover = ActionChains(driver). \
            move_to_element(driver.find_element_by_xpath(Locators.PersonalDetail.select_country_code_box))
        hover.perform()
        # select country code
        driver.find_element_by_xpath(Locators.PersonalDetail.select_country_code_box).click()
        driver.find_element_by_css_selector(Locators.PersonalDetail.select_country_code).click()
        # input phone number
        driver.find_element_by_xpath(Locators.PersonalDetail.input_phone_number). \
            send_keys(random.randint(100000000, 999999999))
        # get code
        driver.find_element_by_xpath(Locators.PersonalDetail.button_get_otp_code).click()
        # input opt code
        driver.find_element_by_xpath(Locators.PersonalDetail.input_otp_code).send_keys(
            random.randint(100000000, 999999999))
        # wait next button clickable
        WebDriverWait(driver, 5, 0.5). \
            until(ec.element_to_be_clickable((By.XPATH, Locators.PersonalDetail.button_next_page)))
        # click next button to next page
        driver.find_element_by_xpath(Locators.PersonalDetail.button_next_page).click()

    def about_you(self):
        # wait zip code show up
        WebDriverWait(driver, 10, 0.5). \
            until(ec.visibility_of_element_located((By.XPATH, Locators.AboutYou.input_zip_code)))
        # select gender
        driver.find_element_by_xpath(Locators.AboutYou.select_gender_box).click()
        driver.find_element_by_css_selector(Locators.AboutYou.select_gender).click()
        # select birth year
        driver.find_element_by_xpath(Locators.AboutYou.select_birth_year_box).click()
        driver.find_element_by_css_selector(Locators.AboutYou.select_birth_year).click()
        # select birth month
        driver.find_element_by_xpath(Locators.AboutYou.select_birth_month_box).click()
        driver.find_element_by_css_selector(Locators.AboutYou.select_birth_month).click()
        # select birth day
        driver.find_element_by_xpath(Locators.AboutYou.select_birth_day_box).click()
        driver.find_element_by_css_selector(Locators.AboutYou.select_birth_day).click()
        # input photo id number
        driver.find_element_by_xpath(Locators.AboutYou.input_photo_id_number).send_keys(random.randint(100, 1000000))
        # input residential address
        driver.find_element_by_xpath(Locators.AboutYou.input_residential_address).send_keys('Bennelong Point, Sydney')
        # input city
        driver.find_element_by_xpath(Locators.AboutYou.input_city).send_keys('Nueve York')
        # input state
        driver.find_element_by_xpath(Locators.AboutYou.input_state).send_keys('Mars')
        # input zip code
        driver.find_element_by_xpath(Locators.AboutYou.input_zip_code).send_keys(random.randint(100, 200000))
        # wait next button clickable
        WebDriverWait(driver, 5, 0.5). \
            until(ec.element_to_be_clickable((By.XPATH, Locators.AboutYou.button_next_page)))
        # click next button to next page
        driver.find_element_by_xpath(Locators.AboutYou.button_next_page).click()

    def investment(self):
        # wait for account type url shows up
        WebDriverWait(driver, 10, 0.5). \
            until(ec.visibility_of_element_located((By.XPATH, Locators.Investment.url_account_type)))
        # select employment
        driver.find_element_by_xpath(Locators.Investment.select_employment_box).click()
        driver.find_element_by_css_selector(Locators.Investment.select_employment).click()
        # select occupation and wait the drop down box shows up
        driver.find_element_by_xpath(Locators.Investment.select_occupation_box).click()
        WebDriverWait(driver, 10, 0.5). \
            until(ec.visibility_of_element_located((By.CSS_SELECTOR, Locators.Investment.select_occupation)))
        driver.find_element_by_css_selector(Locators.Investment.select_occupation).click()
        # select industry
        driver.find_element_by_xpath(Locators.Investment.select_industry_box).click()
        driver.find_element_by_css_selector(Locators.Investment.select_industry).click()
        # select annual income
        driver.find_element_by_xpath(Locators.Investment.select_annual_income_box).click()
        driver.find_element_by_css_selector(Locators.Investment.select_annual_income).click()
        # select total amount of investment
        driver.find_element_by_xpath(Locators.Investment.select_total_amount_of_investment_box).click()
        driver.find_element_by_css_selector(Locators.Investment.select_total_amount_of_investment).click()
        # select trading platform
        driver.find_element_by_xpath(Locators.Investment.select_trading_platform_box).click()
        driver.find_element_by_css_selector(Locators.Investment.select_trading_platform).click()
        # select funding currency
        driver.find_element_by_xpath(Locators.Investment.select_funding_currency_box).click()
        driver.find_element_by_css_selector(Locators.Investment.select_funding_currency).click()
        # select account types
        driver.find_element_by_xpath(Locators.Investment.select_account_types_box).click()
        driver.find_element_by_css_selector(Locators.Investment.select_account_types).click()
        # select leverage
        driver.find_element_by_xpath(Locators.Investment.select_leverage_box).click()
        driver.find_element_by_css_selector(Locators.Investment.select_leverage).click()
        # select next button to next page
        driver.find_element_by_xpath(Locators.Investment.button_next_page).click()

    def experience(self):
        # wait for the first question shows up
        WebDriverWait(driver, 10, 0.5). \
            until(ec.visibility_of_element_located((By.XPATH, Locators.Experience.click_first_question)))
        # click the first question
        driver.find_element_by_xpath(Locators.Experience.click_first_question).click()
        # click the second question
        driver.find_element_by_xpath(Locators.Experience.click_second_question).click()
        # click the third question
        driver.find_element_by_xpath(Locators.Experience.click_third_question).click()
        # click the fourth question
        driver.find_element_by_xpath(Locators.Experience.click_fourth_question).click()
        # click the fifth question
        driver.find_element_by_xpath(Locators.Experience.click_fifth_question).click()
        # click next button to the second page
        driver.find_element_by_xpath(Locators.Experience.button_next_page).click()
        # click the sixth question
        driver.find_element_by_xpath(Locators.Experience.click_sixth_question).click()
        # click the seventh question
        driver.find_element_by_xpath(Locators.Experience.click_seventh_question).click()
        # wait for the button can be clicked
        WebDriverWait(driver, 10, 0.5). \
            until(ec.element_to_be_clickable((By.XPATH, Locators.Experience.click_eighth_question)))
        # scroll down the page
        driver.execute_script(Locators.ExecuteJavascript.scroll_down_the_page)
        # click the eighth question
        driver.find_element_by_xpath(Locators.Experience.click_eighth_question).click()
        # click the ninth question
        driver.find_element_by_xpath(Locators.Experience.click_ninth_question).click()
        # click the tenth question
        driver.find_element_by_xpath(Locators.Experience.click_tenth_question).click()
        # click next button to the next page
        driver.find_element_by_xpath(Locators.Experience.button_second_next_page).click()

    def terms_and_conditions(self):
        # wait for the title shows up
        WebDriverWait(driver, 10, 0.5). \
            until(ec.visibility_of_element_located((By.XPATH, Locators.TermsAndConditions.title)))
        # scroll down the page
        driver.execute_script(Locators.ExecuteJavascript.scroll_down_the_page)
        # click first condition
        driver.find_element_by_xpath(Locators.TermsAndConditions.click_first_condition).click()
        # click second condition
        driver.find_element_by_xpath(Locators.TermsAndConditions.click_second_condition).click()
        # click third condition
        driver.find_element_by_xpath(Locators.TermsAndConditions.click_third_condition).click()
        # click next button to the next page
        driver.find_element_by_xpath(Locators.TermsAndConditions.button_next_page).click()

    def confirm_id(self):
        # wait for the update id front shows up
        WebDriverWait(driver, 10, 0.5). \
            until(ec.visibility_of_element_located((By.XPATH, Locators.ConfirmID.content_id_front)))
        # get absolute path
        test_image_absolute_path = os.path.abspath(Locators.ConfirmID.test_image_path)
        # update id front
        driver.find_element_by_xpath(Locators.ConfirmID.upload_id_front).send_keys(test_image_absolute_path)
        # update id back
        driver.find_element_by_xpath(Locators.ConfirmID.upload_id_back).send_keys(test_image_absolute_path)
        # update address
        driver.find_element_by_xpath(Locators.ConfirmID.upload_address).send_keys(test_image_absolute_path)
        # update other document
        driver.find_element_by_xpath(Locators.ConfirmID.upload_other_document).send_keys(test_image_absolute_path)
        # click next button to the next page
        driver.find_element_by_xpath(Locators.ConfirmID.button_next_page).click()
