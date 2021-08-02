from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

url = 'https://acy.com/en/open-live-account'
edge_path = EdgeChromiumDriverManager().install()
driver = webdriver.Edge(edge_path)

driver.get(url)


class Keyword:
    select_language_confirm = '/html/body/div[1]/div[1]/div[1]/div[2]/div[3]/a'


def main():
    driver.find_element_by_xpath(Keyword.select_language_confirm).click()


if __name__ == '__main__':
    main()
