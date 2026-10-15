from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("file:///C:/Users/DELL/STM/app/index.html")
time.sleep(5)
driver.find_element(By.ID, "username").send_keys("admin")
driver.find_element(By.ID, "password").send_keys("12345")
driver.find_element(By.ID, "loginButton").click()
time.sleep(5)
otp_text = driver.find_element(By.ID, "generatedOTP").text
print("TC01 - Valid Login")
print("Result:", otp_text)
generated_otp = otp_text.split(":")[1].strip()
driver.find_element(By.ID, "otp").send_keys(generated_otp)
driver.find_element(By.ID, "verifyButton").click()
time.sleep(5)

message = driver.find_element(By.ID, "otpMessage").text

print("TC07 - Valid OTP")
print("Result:", message)



driver.quit()