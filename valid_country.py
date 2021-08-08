from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
import Locators

url = 'https://acycn.com/en/open-live-account'
chrome_path = ChromeDriverManager().install()
driver = webdriver.Chrome(chrome_path)
driver.get(url)
driver.maximize_window()


def main():
    check_no = []
    check_name = []
    select_language()

    for i in range(248):

        select_country = f'li[data-testid="country{i}"]'
        select_country_name_box = '//*[@id="gatsby-focus-wrapper"]/div/div/div[1]/div/div/div/div/div[2]/div/div/div[' \
                                  '2]/div/div/form/div[2]/div/div/div/div/div[1]/div '
        driver.find_element_by_xpath(select_country_name_box).click()
        country_name = driver.find_element_by_css_selector(select_country).text
        driver.find_element_by_css_selector(select_country).click()

        try:
            driver.find_element_by_xpath \
                ('/html/body/div[1]/div[1]/div/div/div[1]/div/div/div/div/div[2]/div/div/div[2]/div/div/form/div['
                 '2]/div[2]/span')
            check_no.append(i)
            check_name.append(country_name)
            print(i, country_name)
        except:
            pass

    print('The country cannot register: ', check_name)
    print("country number:", check_no)
    driver.quit()


def select_language():
    WebDriverWait(driver, 5, 0.5). \
        until(ec.element_to_be_clickable((By.XPATH, Locators.PersonalDetail.select_language_confirm)))
    # select language box
    driver.find_element_by_xpath(Locators.PersonalDetail.select_language_box).click()
    driver.find_element_by_xpath(Locators.PersonalDetail.select_language_name).click()
    driver.find_element_by_xpath(Locators.PersonalDetail.select_language_confirm).click()

    WebDriverWait(driver, 5, 0.5). \
        until(ec.element_to_be_clickable((By.XPATH, Locators.PersonalDetail.select_account_type_box)))


if __name__ == '__main__':
    main()
