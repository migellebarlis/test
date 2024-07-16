from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://www.trunc.ph/")

driver.implicitly_wait(1)

login = driver.find_element(by=By.CSS_SELECTOR, value="#html-body > div.page-wrapper > header > div.header.content > div.header-content-item.header-main-right > div.header-right-item.customer-wrapper > div > a.customer-item.account-item")
login.click()

driver.implicitly_wait(1)

email = driver.find_element(by=By.XPATH, value="/html/body/div[9]/main/div[2]/div/div[3]/div[4]/div[2]/form/fieldset/div[1]/div/input")
email.send_keys("qatestdemo@mailsac.com")

password = driver.find_element(by=By.XPATH, value="/html/body/div[9]/main/div[2]/div/div[3]/div[4]/div[2]/form/fieldset/div[2]/div/input")
password.send_keys("Testlang1")

submit = driver.find_element(by=By.XPATH, value="/html/body/div[9]/main/div[2]/div/div[3]/div[4]/div[2]/form/fieldset/div[5]/div/button")
submit.click()

driver.quit()