import time

from utilities import XLUtilis
from selenium import webdriver

driver = webdriver.Chrome(executable_path="/Users/macbook/test_automation/_TEST AUTOMATION/Driver/chromedriver")

driver.get("https://performance-qa.seamlesshrms.com/")
driver.maximize_window()
time.sleep(5)
driver.find_element_by_id("callToActionBtn").click()

path = "/Users/macbook/Desktop/LoginTest.xlsx"
rows = XLUtilis.getRowCount(path, "Sheet1")
columns = XLUtilis.getColunmCount(path, "Sheet1")

for r in range(2, rows+1):
    username = XLUtilis.readData(path, "Sheet1", r, 1)
    password = XLUtilis.readData(path, "Sheet1", r, 2)

    time.sleep(5)
    driver.find_element_by_id("username").send_keys(username)
    driver.find_element_by_id("password").send_keys(password)
    driver.find_element_by_id("login-btn").click()

    if driver.title == "SeamlessHR.com Limited - QA PERFORMANCE":
        print("Test passed")
        expectedresult = XLUtilis.writeData(path, "Sheet1", r, 3, "Test passed")
        time.sleep(5)
        driver.find_element_by_xpath("//img[@class='img-circle']").click()
        time.sleep(3)
        driver.find_element_by_id("logout-btn").click()
    else:
        print("Test Failed")
        expectedresult = XLUtilis.writeData(path, "Sheet1", r, 3, "Test Failed")

    time.sleep(3)