from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc

a=0
while(a==0):
    try:
        driver = uc.Chrome(use_subprocess=True)
        driver.get("https://accounts.google.com/signin/v2/identifier?flowName=GlifWebSignIn&flowEntry=ServiceLogin")
        sleep(1)

        mail = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "identifier")))
        mail.send_keys("")
        driver.find_element("id", "identifierNext").click()
        sleep(1)
        passwd = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "Passwd")))
        passwd.send_keys("")
        driver.find_element("id", "passwordNext").click()
        sleep(2)

        driver.get("Youtube Upload Button Link")
        sleep(1)
        x=1

        while(x<=100):
            driver.find_element(By.CSS_SELECTOR,"#content > input[type=file]").send_keys("example.mp4")
            sleep(1)
            notkids = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "VIDEO_MADE_FOR_KIDS_NOT_MFK")))
            notkids.click()
            sleep(1)
            next1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "next-button")))
            next1.click()
            sleep(1)
            next2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "next-button")))
            next2.click()
            sleep(1)
            next3 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "next-button")))
            next3.click()
            sleep(1)
            driver.find_element(By.NAME,"PUBLIC").click()
            sleep(1)
            done = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "done-button")))
            done.click()
            print("No: of videos = "+str(x))
            x=x+1
            sleep(5)
            driver.refresh()
            sleep(4)
        a+=1
    except:
        print("Error Occured")