import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

options = Options()

options.add_experimental_option('excludeSwitches', ['enable-logging'])

PATH = "D:\TinderBot\chromedriver.exe"   # provide here chromedriver installer local path - install it from google.


class LinkedInBot():
    def __init__(self):
        self.driver = webdriver.Chrome(
            executable_path=PATH, chrome_options=options)

    def linkedin_bot(self):
        try:
            linked_in_home_page = 'https://linkedin.com/'

            self.driver.get(linked_in_home_page)
            self.driver.implicitly_wait(3)

            # enter the login credentials and login

            user_name = self.driver.find_element(By.ID, 'session_key')
            pass_word = self.driver.find_element(By.ID, 'session_password')

            user_name.send_keys('xxxxxxx@gmail.com')
            pass_word.send_keys('xxxpassword')

            login = self.driver.find_element(By.XPATH, '//form/button[1]')
            login.click()

            sleep(12)

            # minimize the chat box in the right down side corner

            minimize_chat_box = self.driver.find_element(
                By.XPATH, '/html/body/div[5]/aside/div[1]/header/div[3]/button[2]')
            minimize_chat_box.click()

            sleep(2)

            # select the jobs hyperlink on the top of the menu

            jobs_hyperlink = self.driver.find_element(
                By.XPATH, '//*[@id="global-nav"]/div/nav/ul/li[3]/a')
            jobs_hyperlink.click()

            sleep(5)

            # find the ids of text boxes for skills and location of the jobs and search the data

            ember_id = self.driver.find_element(
                By.CLASS_NAME, 'jobs-search-box__inner').get_attribute('id').split('-')[3].replace('ember', '')

            input_skills = self.driver.find_element(
                By.ID, 'jobs-search-box-keyword-id-ember' + ember_id)
            input_country = self.driver.find_element(
                By.ID, 'jobs-search-box-location-id-ember' + ember_id)

            input_skills.send_keys('Angular')
            sleep(5)

            input_country.send_keys('Singapore')
            sleep(5)

            location_suggestions = self.driver.find_elements(
                By.CLASS_NAME, 'jobs-search-box__typeahead-suggestion')[0]
            location_suggestions.click()

            # select the easy apply button for filter

            easy_apply_btn = self.driver.find_element(
                By.XPATH, '/html/body/div[5]/div[3]/div[4]/section/div/section/div/div/div/ul/li[8]/div/button')
            easy_apply_btn.click()

        except Exception as e:
            print(e)


 bot = LinkedInBot()
 bot.linkedin_bot()
