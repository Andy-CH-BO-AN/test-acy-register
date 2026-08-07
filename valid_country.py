from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

import Locators
from main import Register


COUNTRY_COUNT = 248
COUNTRY_ERROR = (
    "/html/body/div[1]/div[1]/div/div/div[1]/div/div/div/div/div[2]/div/div/div[2]/div/div/form/"
    "div[2]/div[2]/span"
)


def find_invalid_countries(register):
    invalid_countries = []

    if not register.skip_language_selection:
        register.select_language()

    register._wait_clickable(By.XPATH, Locators.PersonalDetail.select_account_type_box, timeout=5)

    for country_index in range(COUNTRY_COUNT):
        selector = f'li[data-testid="country{country_index}"]'
        register._click(By.XPATH, Locators.PersonalDetail.select_country_name_box)
        country = register.driver.find_element(By.CSS_SELECTOR, selector)
        country_name = country.text
        country.click()

        try:
            register.driver.find_element(By.XPATH, COUNTRY_ERROR)
        except NoSuchElementException:
            continue

        invalid_countries.append((country_index, country_name))
        print(country_index, country_name)

    return invalid_countries


def main():
    register = Register()
    register.open()
    try:
        invalid_countries = find_invalid_countries(register)
    finally:
        register.close()

    print("The country cannot register:", [name for _, name in invalid_countries])
    print("country number:", [index for index, _ in invalid_countries])


if __name__ == "__main__":
    main()
