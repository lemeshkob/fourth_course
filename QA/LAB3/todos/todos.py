from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

def setUp():
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--test-type")
    options.binary_location = "/usr/bin/chromium"
    return webdriver.Chrome(ChromeDriverManager().install())

def add_new_element(driver, input_text):
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "new-todo"))
        )
        element.send_keys(input_text)
        element.submit()
    finally:
        pass

def perform_edit(driver, text_to_add):
    actionChains = ActionChains(driver)
    element_to_edit = driver.find_element_by_class_name('ng-binding')
    actionChains.double_click(element_to_edit).perform()
    edit_input = driver.find_element_by_class_name('edit')
    edit_input.send_keys(" " + text_to_add)
    edit_input.submit()

def perform_done(driver):
    toggle = driver.find_element_by_class_name('toggle')
    toggle.click()


if __name__ == "__main__":
    driver = setUp()
    driver.get('http://todomvc.com/examples/angularjs/#/')
    add_new_element(driver, 'Hello there!')
    perform_edit(driver, "BRUH")
    perform_done(driver)