# #CRONTAB
# XPATH FINDER EXTENSION CHROME
# SELENIUM
# SUBPROCESS

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import time
from datetime import date

today = date.today()
dates = today.strftime('%d')

if int(dates)%2 == 0:
    science = "quantum physics"
    informatic = "Blender and js"
    dream = "be good enough in code to get a good job for my CV"
    info_college = "that's pretty easy"
    phrase_de_fin = " One day I ill be a good coder."
    end = "This code has been changed by my code."
else:
    science = "arithmetics"
    informatic = "Python and Java"
    dream = "get a lot of skills so you can someone that you can be proud of"
    info_college = "that's pretty boring"
    phrase_de_fin = " One day I'll be a good scientist;"
    end = "This code has been changed by my program."

driver = webdriver.Chrome()

url = "https://github.com/login?return_to=https%3A%2F%2Fgithub.com%2Fooo-dev-code"

driver.get(url)

username = driver.find_element(By.ID, "login_field")
username.send_keys("ooo-dev-code")

mdp = driver.find_element(By.ID, "password")
mdp.send_keys("ZebraQFackPassword012749@%")

submit = driver.find_element(By.NAME, "commit").click()

profil = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[5]/main/div/div/div[2]/turbo-frame/div/div[1]/div/div/div[2]/a").click()


input_box = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, f"/html/body/div[1]/div[5]/div/main/turbo-frame/div/react-app/div/div/div[1]/div/div/div[2]/div[2]/div/div[3]/div[3]/div/div[2]/file-attachment/div/div/div[2]/div[2]/div[1]")))
input_box.click()
input_box.clear()
input_box.send_keys("-><b> Hi, I am ooo-dev-code                                                             </b>")

input_box2 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, f"/html/body/div[1]/div[5]/div/main/turbo-frame/div/react-app/div/div/div[1]/div/div/div[2]/div[2]/div/div[3]/div[3]/div/div[2]/file-attachment/div/div/div[2]/div[2]/div[2]")))
input_box2.click()
input_box2.clear()
input_box2.send_keys(f"-> I am a big lover of {science}. I learn more and more about it everyday and I enjoy it very much.                                              ")
input_box2.send_keys(Keys.ENTER)

input_box3 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, f"/html/body/div[1]/div[5]/div/main/turbo-frame/div/react-app/div/div/div[1]/div/div/div[2]/div[2]/div/div[3]/div[3]/div/div[2]/file-attachment/div/div/div[2]/div[2]/div[3]")))
input_box3.click()
input_box3.clear()
input_box3.send_keys(f"-> I am actually learning about {informatic}. I try to get skills to get proud of myself and to get a good job in the future.                                                      ")
input_box3.send_keys(Keys.ENTER)

input_box4 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, f"/html/body/div[1]/div[5]/div/main/turbo-frame/div/react-app/div/div/div[1]/div/div/div[2]/div[2]/div/div[3]/div[3]/div/div[2]/file-attachment/div/div/div[2]/div[2]/div[4]")))
input_box4.click()
input_box4.clear()
input_box4.send_keys(f"-> I am in college and {info_college}.                                                         ")
input_box4.send_keys(Keys.ENTER)

input_box5 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, f"/html/body/div[1]/div[5]/div/main/turbo-frame/div/react-app/div/div/div[1]/div/div/div[2]/div[2]/div/div[3]/div[3]/div/div[2]/file-attachment/div/div/div[2]/div[2]/div[5]")))
input_box5.click()
input_box5.clear()
input_box5.send_keys(f"-> My greatest wish is to {dream}                                                                 ")
input_box5.send_keys(Keys.ENTER)

input_box6 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, f"/html/body/div[1]/div[5]/div/main/turbo-frame/div/react-app/div/div/div[1]/div/div/div[2]/div[2]/div/div[3]/div[3]/div/div[2]/file-attachment/div/div/div[2]/div[2]/div[6]")))
input_box6.click()
input_box6.clear()
input_box6.send_keys(f"-> {phrase_de_fin}                                                                                ")

input_box6.send_keys(Keys.ENTER)

input_box7 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, f"/html/body/div[1]/div[5]/div/main/turbo-frame/div/react-app/div/div/div[1]/div/div/div[2]/div[2]/div/div[3]/div[3]/div/div[2]/file-attachment/div/div/div[2]/div[2]/div[7]")))
input_box7.click()
input_box7.clear()
input_box7.send_keys(f"-> Fun fact: {end}                              ")
input_box7.send_keys(Keys.ENTER)

input_box8 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, f"/html/body/div[1]/div[5]/div/main/turbo-frame/div/react-app/div/div/div[1]/div/div/div[2]/div[2]/div/div[3]/div[3]/div/div[2]/file-attachment/div/div/div[2]/div[2]/div[8]")))
input_box8.click()
input_box8.clear()

Conclude1 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, f"/html/body/div[1]/div[5]/div/main/turbo-frame/div/react-app/div/div/div[1]/div/div/div[2]/div[2]/div/div[3]/div[2]/div[2]/button")))
Conclude1.click()

Conclude2 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, f"/html/body/div[4]/div[2]/div/div/div[3]/button[2]")))
Conclude2.click()

time.sleep(200)

driver.quit()
