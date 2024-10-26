import pyautogui
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://github.com/login?return_to=https%3A%2F%2Fgithub.com%2Fsignup%3Fref_cta%3DSign%2Bup%26ref_loc%3Dheader%2Blogged%2Bout%26ref_page%3D%252F%253Cuser-name%253E%26source%3Dheader")

username = driver.find_element(By.ID, "login_field")
username.send_keys("username")

mdp = driver.find_element(By.ID, "password")
mdp.send_keys("mdp")

submit = driver.find_element(By.NAME, "commit").click()

profil = driver.find_element(By.CLASS_NAME, "button_to").click()
   
time.sleep(1000)
