from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def setUp():
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--test-type")
    options.binary_location = "/usr/bin/chromium"
    return webdriver.Chrome(ChromeDriverManager().install())