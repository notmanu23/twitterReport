from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from proxy import *
from config import *
import time, random
#
f = open('order1786211.txt', 'r')
lst = f.read()
lst = lst.split('\n')
lst2=[]
for i in lst:
    lst2.append(i.split(':'))
    print(i)
f.close()

for account in lst2:
    prx = random.choice(proxies)
    driver = proxy_chrome(prx[0], prx[1], 'SelFahdoviix', 'Y5e6JwW')
    driver.get("https://twitter.com/i/flow/login")
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "r-30o5oe r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-1dz5y72 r-fdjqy7 r-13qz1uu".replace(' ', '.')))).send_keys(account[0])
    time.sleep(2)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "css-18t94o4 css-1dbjc4n r-42olwf r-sdzlij r-1phboty r-rs99b7 r-peo1c r-1ps3wis r-1ny4l3l r-1guathk r-o7ynqc r-6416eg r-lrvibr".replace(' ', '.')))).click()
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "r-30o5oe r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-1dz5y72 r-fdjqy7 r-13qz1uu".replace(' ', '.')))).send_keys(account[1])
    time.sleep(2)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "css-18t94o4 css-1dbjc4n r-42olwf r-sdzlij r-1phboty r-rs99b7 r-peo1c r-1ps3wis r-1ny4l3l r-1guathk r-o7ynqc r-6416eg r-lrvibr".replace(' ', '.')))).click()
    time.sleep(3)
    if driver.current_url == "https://twitter.com/home":
        pass
    else:
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "r-30o5oe r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-1dz5y72 r-fdjqy7 r-13qz1uu".replace(' ', '.'))))
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "r-30o5oe r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-1dz5y72 r-fdjqy7 r-13qz1uu".replace(' ', '.')))).send_keys(account[2])
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "css-18t94o4 css-1dbjc4n r-42olwf r-sdzlij r-1phboty r-rs99b7 r-peo1c r-1ps3wis r-1ny4l3l r-1guathk r-o7ynqc r-6416eg r-lrvibr".replace(' ', '.')))).click()
    time.sleep(3)

    if driver.current_url == "https://twitter.com/home":
        pass
    else:
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "r-30o5oe r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-1dz5y72 r-fdjqy7 r-13qz1uu".replace(' ', '.'))))
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "r-30o5oe r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-1dz5y72 r-fdjqy7 r-13qz1uu".replace(' ', '.')))).send_keys(account[1])
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "css-18t94o4 css-1dbjc4n r-42olwf r-sdzlij r-1phboty r-rs99b7 r-peo1c r-1ps3wis r-1ny4l3l r-1guathk r-o7ynqc r-6416eg r-lrvibr".replace(' ', '.')))).click()

    time.sleep(3)

    if driver.current_url == "https://twitter.com/home":
        pass
    else:
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "r-30o5oe r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-1dz5y72 r-fdjqy7 r-13qz1uu".replace(' ', '.'))))
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "r-30o5oe r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-1dz5y72 r-fdjqy7 r-13qz1uu".replace(' ', '.')))).send_keys(account[2])
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "css-18t94o4 css-1dbjc4n r-42olwf r-sdzlij r-1phboty r-rs99b7 r-peo1c r-1ps3wis r-1ny4l3l r-1guathk r-o7ynqc r-6416eg r-lrvibr".replace(' ', '.')))).click()

    if driver.current_url == "https://twitter.com/home":
        pass
    else:
        input("Login Failed. Please Log in Manually and press enter.")

    time.sleep(5)
    driver.get(f'https://twitter.com/{userName}')
    # WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "r-18jsvk2 r-4qtqp9 r-yyyyoo r-z80fyv r-dnmrzs r-bnwqim r-1plcrui r-lrvibr r-19wmn03".replace(' ', '.'))))[1].click()
    # WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "css-901oao r-18jsvk2 r-37j5jr r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-qvutc0".replace(' ', '.'))))[8].click()
    time.sleep(2)
    driver.find_elements_by_class_name("r-18jsvk2 r-4qtqp9 r-yyyyoo r-z80fyv r-dnmrzs r-bnwqim r-1plcrui r-lrvibr r-19wmn03".replace(' ', '.'))[1].click()
    time.sleep(2)
    driver.find_element_by_xpath(f"//*[contains(text(), 'Report @{userName}')]").click()
    time.sleep(2)
    iframe = driver.find_element_by_class_name('r-1yadl64.r-16y2uox')
    driver.switch_to_frame(iframe)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "sensitive-info-v2-btn"))).click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "adult-btn"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "submit-btn".replace(' ', '.')))).click()
    driver.close()
    print(f"Reported with {account[0]}")
    print("waiting ...")
    time.sleep(random.randint(100, 600))


