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

# Load the background color from the provided image
bg_image = Image.open("bgColor.png")
background_color = bg_image.getpixel((20, 20))[:3]
print(f"Background color: {background_color}")

time.sleep(2)
# Start the game by simulating a key press
pyautogui.keyDown('space')
pyautogui.keyUp('space')

time.sleep(2)

# Locate the dinosaur on screen
dino_box = pyautogui.locateOnScreen("dino.png", confidence=0.8)
if dino_box:
    print(f"Dino located at: {dino_box}")
else:
    driver.quit()
    exit()

def detect_obstacle(dino_box, background_color):
    collision_box = {
        'left': dino_box.left + dino_box.width,
        'top': dino_box.top - (dino_box.top // 2),
        'width': 125,
        'height': dino_box.height // 2
    }
    for x in range(collision_box['left'], collision_box['left'] + collision_box['width']):
        for y in range(collision_box['top'], collision_box['top'] + collision_box['height']):
            if not pyautogui.pixelMatchesColor(x, y, background_color):
                print(f"Obstacle at: {x, y}")
                return True
    return False

while True:
    dino_box = pyautogui.locateOnScreen("dino.png", confidence=0.8)
    if dino_box and detect_obstacle(dino_box, background_color):
        pyautogui.keyDown('space')
        pyautogui.keyUp('space')
        time.sleep(0.2)
    time.sleep(0.05)

driver.quit()
