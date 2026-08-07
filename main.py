import os
import random
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

import Locators


DEFAULT_URL = "https://acycn.com/en/open-live-account"
TRUTHY_VALUES = {"1", "true", "yes", "on"}


def _env_flag(name, default=False):
    value = os.getenv(name)
    if value is None:
        return default
    return value.strip().lower() in TRUTHY_VALUES


def create_driver():
    """Create either a local Chrome driver or a remote Selenium driver."""
    remote_url = os.getenv("REMOTE_WEBDRIVER_URL")
    options = webdriver.ChromeOptions()

    if remote_url:
        return webdriver.Remote(command_executor=remote_url, options=options)

    service = Service(ChromeDriverManager().install())
    return webdriver.Chrome(service=service, options=options)


class Register:
    """Drive the ACY registration flow with one owned WebDriver session."""

    def __init__(self, driver=None, timeout=10, url=None, skip_language_selection=None):
        self.driver = driver or create_driver()
        self.timeout = timeout
        self.wait = WebDriverWait(self.driver, timeout, poll_frequency=0.5)
        self.url = url or os.getenv("ACY_REGISTER_URL", DEFAULT_URL)
        self.skip_language_selection = (
            _env_flag("SKIP_LANGUAGE_SELECTION")
            if skip_language_selection is None
            else skip_language_selection
        )

    def open(self):
        self.driver.get(self.url)
        self.driver.maximize_window()

    # Backwards-compatible alias for the original API.
    def main(self):
        self.open()

    def _wait_clickable(self, by, locator, timeout=None):
        wait = self.wait if timeout is None else WebDriverWait(self.driver, timeout, poll_frequency=0.5)
        return wait.until(EC.element_to_be_clickable((by, locator)))

    def _wait_visible(self, by, locator, timeout=None):
        wait = self.wait if timeout is None else WebDriverWait(self.driver, timeout, poll_frequency=0.5)
        return wait.until(EC.visibility_of_element_located((by, locator)))

    def _click(self, by, locator):
        self.driver.find_element(by, locator).click()

    def _type(self, by, locator, value, clear=False):
        element = self.driver.find_element(by, locator)
        if clear:
            element.clear()
        element.send_keys(value)

    def _select_dropdown(self, box_by, box_locator, option_by, option_locator):
        self._click(box_by, box_locator)
        self._click(option_by, option_locator)

    def select_language(self):
        self._wait_clickable(By.XPATH, Locators.PersonalDetail.select_language_confirm, timeout=5)
        self._click(By.XPATH, Locators.PersonalDetail.select_language_box)
        self._click(By.XPATH, Locators.PersonalDetail.select_language_name)
        self._click(By.XPATH, Locators.PersonalDetail.select_language_confirm)

    def personal_detail(self):
        if not self.skip_language_selection:
            self.select_language()

        self._wait_clickable(By.XPATH, Locators.PersonalDetail.select_account_type_box, timeout=5)
        self._select_dropdown(
            By.XPATH,
            Locators.PersonalDetail.select_account_type_box,
            By.XPATH,
            Locators.PersonalDetail.select_account_type_personal,
        )
        self._select_dropdown(
            By.XPATH,
            Locators.PersonalDetail.select_country_name_box,
            By.CSS_SELECTOR,
            Locators.PersonalDetail.select_country,
        )
        self._select_dropdown(
            By.XPATH,
            Locators.PersonalDetail.select_title_box,
            By.CSS_SELECTOR,
            Locators.PersonalDetail.select_title,
        )

        self._type(By.XPATH, Locators.PersonalDetail.input_first_name, "first name", clear=True)
        self._type(By.XPATH, Locators.PersonalDetail.input_middle_name, "middle name", clear=True)
        self._type(By.XPATH, Locators.PersonalDetail.input_last_name, "last name", clear=True)
        self._type(
            By.XPATH,
            Locators.PersonalDetail.input_email,
            f"a{random.randint(0, 1000)}a@a.com",
            clear=True,
        )

        country_code_box = self.driver.find_element(By.XPATH, Locators.PersonalDetail.select_country_code_box)
        ActionChains(self.driver).move_to_element(country_code_box).perform()
        self._select_dropdown(
            By.XPATH,
            Locators.PersonalDetail.select_country_code_box,
            By.CSS_SELECTOR,
            Locators.PersonalDetail.select_country_code,
        )
        self._type(
            By.XPATH,
            Locators.PersonalDetail.input_phone_number,
            random.randint(100000000, 999999999),
        )
        self._click(By.XPATH, Locators.PersonalDetail.button_get_otp_code)
        self._type(
            By.XPATH,
            Locators.PersonalDetail.input_otp_code,
            random.randint(100000000, 999999999),
        )
        self._wait_clickable(By.XPATH, Locators.PersonalDetail.button_next_page, timeout=5).click()

    def about_you(self):
        self._wait_visible(By.XPATH, Locators.AboutYou.input_zip_code)
        self._select_dropdown(
            By.XPATH,
            Locators.AboutYou.select_gender_box,
            By.CSS_SELECTOR,
            Locators.AboutYou.select_gender,
        )
        self._select_dropdown(
            By.XPATH,
            Locators.AboutYou.select_birth_year_box,
            By.CSS_SELECTOR,
            Locators.AboutYou.select_birth_year,
        )
        self._select_dropdown(
            By.XPATH,
            Locators.AboutYou.select_birth_month_box,
            By.CSS_SELECTOR,
            Locators.AboutYou.select_birth_month,
        )
        self._select_dropdown(
            By.XPATH,
            Locators.AboutYou.select_birth_day_box,
            By.CSS_SELECTOR,
            Locators.AboutYou.select_birth_day,
        )
        self._type(By.XPATH, Locators.AboutYou.input_photo_id_number, random.randint(100, 1000000))
        self._type(By.XPATH, Locators.AboutYou.input_residential_address, "Bennelong Point, Sydney")
        self._type(By.XPATH, Locators.AboutYou.input_city, "Nueve York")
        self._type(By.XPATH, Locators.AboutYou.input_state, "Mars")
        self._type(By.XPATH, Locators.AboutYou.input_zip_code, random.randint(100, 200000))
        self._wait_clickable(By.XPATH, Locators.AboutYou.button_next_page, timeout=5).click()

    def investment(self):
        self._wait_visible(By.XPATH, Locators.Investment.url_account_type)
        dropdowns = (
            (Locators.Investment.select_employment_box, Locators.Investment.select_employment),
            (Locators.Investment.select_occupation_box, Locators.Investment.select_occupation),
            (Locators.Investment.select_industry_box, Locators.Investment.select_industry),
            (Locators.Investment.select_annual_income_box, Locators.Investment.select_annual_income),
            (
                Locators.Investment.select_total_amount_of_investment_box,
                Locators.Investment.select_total_amount_of_investment,
            ),
            (Locators.Investment.select_trading_platform_box, Locators.Investment.select_trading_platform),
            (Locators.Investment.select_funding_currency_box, Locators.Investment.select_funding_currency),
            (Locators.Investment.select_account_types_box, Locators.Investment.select_account_types),
            (Locators.Investment.select_leverage_box, Locators.Investment.select_leverage),
        )

        for box_locator, option_locator in dropdowns:
            self._click(By.XPATH, box_locator)
            self._wait_visible(By.CSS_SELECTOR, option_locator)
            self._click(By.CSS_SELECTOR, option_locator)

        self._click(By.XPATH, Locators.Investment.button_next_page)

    def experience(self):
        first_page_questions = (
            Locators.Experience.click_first_question,
            Locators.Experience.click_second_question,
            Locators.Experience.click_third_question,
            Locators.Experience.click_fourth_question,
            Locators.Experience.click_fifth_question,
        )
        second_page_questions = (
            Locators.Experience.click_sixth_question,
            Locators.Experience.click_seventh_question,
        )
        remaining_questions = (
            Locators.Experience.click_eighth_question,
            Locators.Experience.click_ninth_question,
            Locators.Experience.click_tenth_question,
        )

        self._wait_visible(By.XPATH, first_page_questions[0])
        for locator in first_page_questions:
            self._click(By.XPATH, locator)
        self._click(By.XPATH, Locators.Experience.button_next_page)

        for locator in second_page_questions:
            self._click(By.XPATH, locator)

        self._wait_clickable(By.XPATH, Locators.Experience.click_eighth_question)
        self.driver.execute_script(Locators.ExecuteJavascript.scroll_down_the_page)
        for locator in remaining_questions:
            self._click(By.XPATH, locator)
        self._click(By.XPATH, Locators.Experience.button_second_next_page)

    def terms_and_conditions(self):
        self._wait_visible(By.XPATH, Locators.TermsAndConditions.title)
        self.driver.execute_script(Locators.ExecuteJavascript.scroll_down_the_page)
        for locator in (
            Locators.TermsAndConditions.click_first_condition,
            Locators.TermsAndConditions.click_second_condition,
            Locators.TermsAndConditions.click_third_condition,
        ):
            self._click(By.XPATH, locator)
        self._click(By.XPATH, Locators.TermsAndConditions.button_next_page)

    def confirm_id(self):
        self._wait_visible(By.XPATH, Locators.ConfirmID.content_id_front)
        test_image_path = str(Path(Locators.ConfirmID.test_image_path).resolve())

        for locator in (
            Locators.ConfirmID.upload_id_front,
            Locators.ConfirmID.upload_id_back,
            Locators.ConfirmID.upload_address,
            Locators.ConfirmID.upload_other_document,
        ):
            self._type(By.XPATH, locator, test_image_path)

        self._click(By.XPATH, Locators.ConfirmID.button_next_page)
        return self._wait_visible(
            By.CSS_SELECTOR,
            Locators.ConfirmID.title_register_successfully,
            timeout=20,
        )

    def close(self):
        if self.driver is not None:
            self.driver.quit()
            self.driver = None

    # Backwards-compatible alias for the original API.
    def close_browser(self):
        self.close()
