from appium import webdriver
from time import sleep
from selenium import webdriver
import xlrd

class Setup:
    """"Setup class which opens the UI of the application on the iOS emulator"""

    def __init__(self): #iOS real device setup on Xcode 11
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities={
                'app': 'Settings',
                'platformName': 'iOS',
                'platformVersion': '12.4.6',
                'deviceName': 'iPhone 6',
                'udid': 'ceee8d29ae3ba9f3bc19969e19fa66e4574d4f77'
            } )
        sleep(5)
        el = self.driver.find_element_by_name('Continue')  # Accept permission popup appearing on the UI
        sleep(5)
        el.click()
        sleep(5)
        self.driver.switch_to_alert().accept()  # Accept alert which appears saying about the OS version to which application is compatible
        sleep(5)
        self.driver.quit()

    def testcase1(self):
        """"Click on google chrome browser icon and check if the box is enabled / available for user input"""

        self.driver.find_element_by_xpath('//*[@id="screenshotContainer"]/div/div/div/div/div/div[14]').click()
        self.driver.find_element_by_xpath('//*[@id="screenshotContainer"]/div/div/div/div/div/div[23]').is_displayed()
        self.driver.find_element_by_xpath('//*[@id="screenshotContainer"]/div/div/div/div/div/div[23]').is_enabled()

    def testcase2(self):
        """Click on the "Go to home screen button""to check if the default home screen of the application appears"""

        self.driver.find_element_by_xpath(
            '//*[@id="screenshotContainer"]/div/div/div/div/div/div[14]').click()  # click on the button to go back to homescreen
        sleep(5)
        self.driver.find_element_by_xpath('//*[@id="screenshotContainer"]/div/div/div/div/div/div[4]/div').is_enabled()
        self.driver.find_element_by_xpath(
            '//*[@id="screenshotContainer"]/div/div/div/div/div/div[4]/div').is_displayed()

    def testcase3(self):
        """Register a new user account by filing all the details from CSV file"""

        self.driver.find_element_by_xpath('//*[@id="screenshotContainer"]/div/div/div/div/div/div[13]').click()
        sleep(2)
        loc = ("C:\Users\Home\Desktop\Python\Data.csv")  # Read data from excel sheet for creating new regustered user
        wb = xlrd.open_workbook(loc)
        sheet = wb.sheet_by_index(0)
        self.driver.find_element_by_xpath('//*[@id="screenshotContainer"]/div/div/div/div/div/div[10]').send_keys(
            sheet.cell_value(0, 0))
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="screenshotContainer"]/div/div/div/div/div/div[13]').send_keys(
            sheet.cell_value(1.0))
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="screenshotContainer"]/div/div/div/div/div/div[14]').send_keys(
            sheet.cell_value(2, 0))
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="screenshotContainer"]/div/div/div/div/div/div[16]').send_keys(
            sheet.cell_value(3, 0))
        sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="screenshotContainer"]/div/div/div/div/div/div[19]').select.select_by_value('Python')
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="screenshotContainer"]/div/div/div/div/div/div[22]').click()
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="screenshotContainer"]/div/div/div/div/div/div[22]').click()

    def testcase4(self):
        """"Check the exception thrown by the application on different enteries by the user"""
        self.driver.find_element_by_xpath('//*[@id="screenshotContainer"]/div/div/div/div/div/div[24]').is_enabled()
        self.driver.find_element_by_xpath('//*[@id="screenshotContainer"]/div/div/div/div/div/div[24]').send_keys("123")

    def teardown(self):
        """Close the application and quit the appium automation"""
        self.driver.quit()

    """Trigger automation by calling the class"""

    Selendroid()
