from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

USERNAME = "teddy_james17"
PASSWORD = "Vb@x2=tqDxbpt7U"

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 20)

try:
    # Step 1: Login
    driver.get("https://www.instagram.com/accounts/login/")
    wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys(USERNAME)
    driver.find_element(By.NAME, "password").send_keys(PASSWORD, Keys.ENTER)
    print("Logged in")
    time.sleep(5)

    # Step 2: Handle popups like "Save Info", "Not Now"
    for popup in ["Save info", "Not Now"]:
        try:
            btn = wait.until(EC.element_to_be_clickable((By.XPATH, f"//button[text()='{popup}']")))
            btn.click()
            time.sleep(2)
        except:
            continue

    # Step 3: Click Search in sidebar
    search_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Search']/ancestor::a")))
    search_button.click()
    time.sleep(2)

    # Step 4: Search for cbitosc
    search_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search']")))
    search_input.send_keys("cbitosc")
    time.sleep(2)

    profile_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/cbitosc/')]")))
    profile_link.click()
    print("Opened cbitosc profile")
    time.sleep(5)

    # Step 5: Follow button
    try:
        follow_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Follow']")))
        follow_btn.click()
        print("Followed the account")
    except:
        print(" Already followed or Follow button not visible")

    

    # Step 7: Stats
    try:
        stats = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//header//ul/li")))
        posts = stats[0].text.split('\n')[0]
        followers = stats[1].text.split('\n')[0]
        following = stats[2].text.split('\n')[0]
    except:
        posts = followers = following = "N/A"

    # Step 8: Save to file
    with open("cbitosc_profile.txt", "w", encoding="utf-8") as f:
        f.write("CBIT OSC Instagram Profile\n")
        f.write(f"Posts: {posts}\n")
        f.write(f"Followers: {followers}\n")
        f.write(f"Following: {following}\n")

    print("📁 Data saved to cbitosc_profile.txt")

except Exception as e:
    print("❌ Error occurred:", e)
    driver.save_screenshot("error.png")

finally:
    driver.quit()