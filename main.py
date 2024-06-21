import pyautogui
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from PIL import Image

# Constants
GAME_URL = "chrome://dino"  # Corrected URL for offline game
chrome_driver_path = "ChromeDriver\\chromedriver.exe"

# Setup WebDriver
service = Service(chrome_driver_path)
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=service)
driver.get(GAME_URL)
driver.maximize_window()
    # Pause to ensure the page is fully loaded
time.sleep(2)

    # Locate the Dino on the screen
dino_location = pyautogui.locateOnScreen("dino.png")
if dino_location:
    print(f"Dino located at: {dino_location}")
else:
    print("Dino not found on screen.")

# Close the driver after some time or add more automation as needed
time.sleep(10)
driver.quit()
