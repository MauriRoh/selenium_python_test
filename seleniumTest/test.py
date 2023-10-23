# import unittest
# from pyunitreport import HTMLTestRunner
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select    # Para los elementos Select - Dropdown


# # driver = webdriver.Firefox()
# # driver = webdriver.Edge()
# # driver = webdriver.Chrome()
# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# driver.get(url='https://www.carrefour.com.ar/')
# # driver.maximize_window()
# print(driver.title)
# driver.quit()
# driver.close()

class FindElementByXPath():

    def ButtonAccess(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        # driver.get(url='https://www.farmacity.com/')
        # driver.get(url='https://www.sugarcrm.com/au/request-demo/')
        # driver.get(url='https://www.yatra.com/')
        driver.get(url='https://www.salesforce.com/au/form/signup/freetrial-sales/?d=topnav2-btn-ft')

        time.sleep(5)
        # driver.find_element(By.XPATH, "//span[normalize-space()='Ingresar']").click()
        # time.sleep(5)
        # driver.find_element(By.XPATH, "//input[@placeholder='ejemplo@mail.com']").send_keys('soft.organapp@gmail.com')
        # driver.find_element(By.XPATH, "//input[@placeholder='ejemplo@mail.com']").is_enabled() # si está activo un elemento
        # driver.find_element(By.XPATH, "//input[@placeholder='ejemplo@mail.com']").is_displayed() # si un elemento está presente en la página retorna True
        #
        # driver.find_element(By.XPATH,"//input[@placeholder='ejemplo@mail.com']").click()  # Activas el CheckBox o RadioButton
        # driver.find_element(By.XPATH, "//input[@placeholder='ejemplo@mail.com']").is_selected() # CheckBox o RadioButton está seleccionado retorna True
        driver.find_element(By.ID, "onetrust-accept-btn-handler").click()

        # Selector Drowdown
        selectDropdown = Select(driver.find_element(By.NAME, "CompanyEmployees"))  # Select - Dropdown
        selectDropdown.select_by_index(1)
        time.sleep(5)
        selectDropdown.select_by_visible_text('1 - 15 employees')
        time.sleep(5)
        selectDropdown.select_by_value('30')


        time.sleep(15)
        # driver.find_element("//input[@placeholder='ejemplo@mail.com']").send_keys('test@test.com')
        # time.sleep(5)


findElementByXPath = FindElementByXPath()
print(findElementByXPath.ButtonAccess())


# class PruebaTest(unittest.TestCase):
#     def SetUp(self):
#         self.driver = webdriver.Chrome(executable_path = "C://Users/HP/Documents/DriverAplications/chromedriver/chromedriver.exe")
#
#     def test_Prueba(self):
#         pass
#
#     def tearDown(self):
#         return super().tearDown()