from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import re

driver = webdriver.Chrome()
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3233765030&distance=25&f_AL=true&f_WT=2&geoId=92000000&keywords=web%20developer")

#login
sign_in_button = driver.find_element(By.LINK_TEXT, "Sign in")
sign_in_button.click()

email_field = driver.find_element(By.ID, "username")
email_field.send_keys("your email")

password_field = driver.find_element(By.ID, "password")
password_field.send_keys("your password")

password_field.send_keys(Keys.ENTER)

#grab all job listings
all_listings = driver.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")

def closeWindow():
    close_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
    close_button.click()
    time.sleep(2)
    discard_button = driver.find_element(By.XPATH, "//button[contains(@class, 'artdeco-button')]//*[contains(., 'Discard')]/..")
    discard_button.click()

def answer_questions():
    input_list = driver.find_elements(By.CSS_SELECTOR, "input")
    label_list = driver.find_elements(By.CSS_SELECTOR, "label")
    
    for index, label in enumerate(label_list):
        if "years" in label.text:
            input_list[index].send_keys(2)
        if "salary" in label.text:
            input_list[index].send_keys("30,000/year")

def submit_application():
    submit_button = driver.find_element(By.CLASS_NAME, "artdeco-button--primary")
    if submit_button.get_attribute("aria-label") == "Submit application":
        submit_button.click()
        time.sleep(2)
        close_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
        close_button.click()
    else:
        closeWindow()
        print("Complex application skipped...")
      


list_of_technologies = ["React", "JavaScript", "Node", "express", "bootstrap", "python", "php", "wordpress", "Jquery", "redux", "HTML", "Css", "three.js"]

for listing in all_listings:
    listing.click()
    time.sleep(2)
    try:
        apply_button = driver.find_element(By.CSS_SELECTOR, ".jobs-s-apply span")
        apply_button.click()
        time.sleep(2)
        next_button = driver.find_element(By.CSS_SELECTOR, "footer button")
        if next_button.get_attribute("aria-label") == "Continue to next step":
            next_button.click()
        else:
            closeWindow()
            print("Complex application skipped...")
            continue
        time.sleep(2)
        choose_button = driver.find_element(By.CLASS_NAME, "artdeco-button--1")
        if choose_button.get_attribute("aria-label") == "Choose Resume":
            print("yea")
            choose_button.click()
            time.sleep(2)
            next_button = driver.find_element(By.CSS_SELECTOR, "footer button")
            if next_button.get_attribute("aria-label") == "Continue to next step":
                next_button.click()
            else:
                print("sum ting wong")
        
        review_button = driver.find_elements(By.CSS_SELECTOR, "footer button")[1]
        if review_button.get_attribute("aria-label") != "Review your application":
            review_button.click()
            time.sleep(2)
            answer_questions()
            time.sleep(2)
            review_button = driver.find_elements(By.CSS_SELECTOR, "footer button")[1]
            review_button.click()
            time.sleep(2)
            submit_application()
        else:
            review_button.click()
            time.sleep(2)
            submit_application()
            
    except NoSuchElementException:
        print("no such element found")
        continue
