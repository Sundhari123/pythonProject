from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def get_webdriver(webdriver_type):
    if webdriver_type == "edge":
        driver = webdriver.Edge()
    elif webdriver_type == "firefox":
        driver = webdriver.Firefox()
    elif webdriver_type == "chrome":
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Chrome(service=Service("chromedriver.exe"))
    return driver