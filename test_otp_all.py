from selenium import webdriver
from selenium.webdriver.common.by import By
import time
HTML_FILE_PATH = "file:///C:/Users/DELL/STM/app/index.html"
def start_browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(HTML_FILE_PATH)
    time.sleep(2)
    return driver
# TC01 - Valid username and password
driver = start_browser()
driver.find_element(By.ID, "username").send_keys("admin")
driver.find_element(By.ID, "password").send_keys("12345")
driver.find_element(By.ID, "loginButton").click()
message = driver.find_element(By.ID, "generatedOTP").text
print("TC01 - Valid username/password")
print("Expected: OTP generated")
print("Actual:", message)
driver.quit()

# TC02 - Invalid username

driver = start_browser()
driver.find_element(By.ID, "username").send_keys("wronguser")
driver.find_element(By.ID, "password").send_keys("12345")
driver.find_element(By.ID, "loginButton").click()
message = driver.find_element(By.ID, "loginMessage").text
print("TC02 - Invalid username")
print("Expected: Invalid username.")
print("Actual:", message)
driver.quit()

# TC03 - Invalid password

driver = start_browser()

driver.find_element(By.ID, "username").send_keys("admin")
driver.find_element(By.ID, "password").send_keys("wrongpass")
driver.find_element(By.ID, "loginButton").click()
message = driver.find_element(By.ID, "loginMessage").text

print("TC03 - Invalid password")
print("Expected: Invalid password.")
print("Actual:", message)

driver.quit()


# TC04 - Empty username


driver = start_browser()

driver.find_element(By.ID, "password").send_keys("12345")
driver.find_element(By.ID, "loginButton").click()

message = driver.find_element(By.ID, "loginMessage").text

print("TC04 - Empty username")
print("Expected: Username and password are required.")
print("Actual:", message)

driver.quit()


# TC05 - Empty password

driver = start_browser()
driver.find_element(By.ID, "username").send_keys("admin")
driver.find_element(By.ID, "loginButton").click()
message = driver.find_element(By.ID, "loginMessage").text
print("TC05 - Empty password")
print("Expected: Username and password are required.")
print("Actual:", message)
driver.quit()

# TC06 - Both fields empty

driver = start_browser()
driver.find_element(By.ID, "loginButton").click()
message = driver.find_element(By.ID, "loginMessage").text
print("TC06 - Empty username and password")
print("Expected: Username and password are required.")
print("Actual:", message)
driver.quit()

# TC07 - Valid OTP

driver = start_browser()
driver.find_element(By.ID, "username").send_keys("admin")
driver.find_element(By.ID, "password").send_keys("12345")
driver.find_element(By.ID, "loginButton").click()
time.sleep(1)
otp_text = driver.find_element(By.ID, "generatedOTP").text
generated_otp = otp_text.split(":")[1].strip()
driver.find_element(By.ID, "otp").send_keys(generated_otp)
driver.find_element(By.ID, "verifyButton").click()

message = driver.find_element(By.ID, "otpMessage").text

print("TC07 - Valid OTP")
print("Expected: OTP verified successfully. Login successful!")
print("Actual:", message)

driver.quit()

# TC08 - Invalid OTP

driver = start_browser()
driver.find_element(By.ID, "username").send_keys("admin")
driver.find_element(By.ID, "password").send_keys("12345")
driver.find_element(By.ID, "loginButton").click()

time.sleep(5)
driver.find_element(By.ID, "otp").send_keys("111111")
driver.find_element(By.ID, "verifyButton").click()

message = driver.find_element(By.ID, "otpMessage").text

print("TC08 - Invalid OTP")
print("Expected: Invalid OTP.")
print("Actual:", message)

driver.quit()

# TC09 - Empty OTP


driver = start_browser()
driver.find_element(By.ID, "username").send_keys("admin")
driver.find_element(By.ID, "password").send_keys("12345")
driver.find_element(By.ID, "loginButton").click()
time.sleep(1)
driver.find_element(By.ID, "verifyButton").click()
message = driver.find_element(By.ID, "otpMessage").text
print("TC09 - Empty OTP")
print("Expected: OTP is required.")
print("Actual:", message)
driver.quit()

# TC10 - OTP containing letters

driver = start_browser()
driver.find_element(By.ID, "username").send_keys("admin")
driver.find_element(By.ID, "password").send_keys("12345")
driver.find_element(By.ID, "loginButton").click()
time.sleep(5)
driver.find_element(By.ID, "otp").send_keys("ABC123")
driver.find_element(By.ID, "verifyButton").click()
message = driver.find_element(By.ID, "otpMessage").text
print("TC10 - OTP with letters")
print("Expected: Invalid OTP.")
print("Actual:", message)
driver.quit()
print("\nAll test cases completed.")