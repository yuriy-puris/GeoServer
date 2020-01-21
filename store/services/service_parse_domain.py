from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Bot:
    def __init__(self):
        self.driver = webdriver.Firefox(executable_path=r'E:\Python\geckodriver.exe')
        self.navigate()


    def navigate(self):
        wait = WebDriverWait(self.driver, 500)
        self.driver.get('https://www.name.com/domain/search/agree')
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "resultsrow")))
        row = self.driver.find_element_by_class_name('resultsrow')
        print(row.find_element_by_class_name('proximanovabold').get_attribute("innerHTML"))

def parse_domain():
    b = Bot()


if __name__ == '__main__':
    parse_domain()