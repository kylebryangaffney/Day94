import pyautogui
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from PIL import Image

GAME_URL = "https://trex-runner.com/#google_vignette"
chrome_driver_path = "ChromeDriver\\chromedriver.exe"

service = Service(chrome_driver_path)
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=service)
driver.get(GAME_URL)
driver.maximize_window()
time.sleep(2)

dino_location = pyautogui.locateOnScreen("dino.png")
if dino_location:
    print(f"Dino located at: {dino_location}")
else:
    print("Dino not found on screen.")
    driver.quit()
    exit()

bg_image = Image.open("bgColor.png")
background_color = bg_image.getpixel((20, 6))[:3]
print(f"Background color: {background_color}")
time.sleep(2)
pyautogui.keyDown('space')
pyautogui.keyUp('space')

tolerance = 5

def colors_are_similar(color1, color2, tolerance):
    return all(abs(c1 - c2) <= tolerance for c1, c2 in zip(color1, color2))

# Function to detect obstacle
def detect_obstacle(dino_location, background_color, tolerance):
    dino_mid_y = dino_location.top + dino_location.height // 2
    for x_offset in range(60, 70, 2):  # Narrower offset range
        obstacle_color = pyautogui.pixel(dino_location.left + x_offset, dino_mid_y)[:3]  # Extract only RGB values
        print(f"Checking pixel at {(dino_location.left + x_offset, dino_mid_y)}: {obstacle_color}")
        if not colors_are_similar(obstacle_color, background_color, tolerance):
            return True
    return False

while True:
    obstacle_detected = False
    for _ in range(2):
        if detect_obstacle(dino_location, background_color, tolerance):
            obstacle_detected = True
            break
        time.sleep(0.05)
    if obstacle_detected:
        pyautogui.keyDown('space')
        pyautogui.keyUp('space')
    time.sleep(0.2)

driver.quit()
