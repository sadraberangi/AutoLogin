import time

from pynput.keyboard import Key, Controller
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.microsoft import EdgeChromiumDriverManager

options = webdriver.EdgeOptions()
web = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()), options=options)
web.get('https://slms.sbu.ac.ir/')
while True:  # this is same thing which WebDriverWait to
    try:
        web.find_element(by='xpath', value='//*[@id="inputName"]').send_keys('username')
        web.find_element(by='xpath', value='//*[@id="inputPassword"]').send_keys('password')
        break
    except:
        pass
WebDriverWait(web, 100).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="submit"]')))  # wait for the page to load
web.find_element(by='xpath', value='//*[@id="submit"]').click()
WebDriverWait(web, 100).until(EC.presence_of_element_located((By.XPATH, '//*[@id="inst43"]/div[2]/ul/li[2]/div/a')))
web.find_element(by='xpath', value='//*[@id="inst43"]/div[2]/ul/li[2]/div/a').click()
WebDriverWait(web, 100).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="module-7215"]/div/div/div[2]/div/a/span')))
web.find_element(by='xpath', value='//*[@id="module-7215"]/div/div/div[2]/div/a/span').click()
WebDriverWait(web, 100).until(EC.presence_of_element_located((By.XPATH, '//*[@id="id_submitbutton"]')))
web.find_element(by='xpath', value='//*[@id="id_submitbutton"]').click()
WebDriverWait(web, 100).until(EC.presence_of_element_located(
    (By.XPATH, '//*[@id="launchOptionsDialog"]/div[2]/coral-dialog-content/div[1]/div[2]/div')))

web.find_element(by='xpath',
                 value='//*[@id="launchOptionsDialog"]/div[2]/coral-dialog-content/div[1]/div[2]/div').click()
time.sleep(4)
kb = Controller()
kb.press(Key.left)
kb.press(Key.enter)  # press enter because of alert
time.sleep(10)
