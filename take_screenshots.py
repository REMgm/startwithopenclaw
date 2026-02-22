from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time

# Setup Chrome options
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--window-size=1920,1080')

# Try to find Chrome/Chromium
try:
    driver = webdriver.Chrome(options=chrome_options)
except:
    chrome_options.binary_location = '/usr/bin/chromium-browser'
    driver = webdriver.Chrome(options=chrome_options)

# Take screenshots
driver.get('http://localhost:8082/index.html')
time.sleep(2)
driver.save_screenshot('/root/.openclaw/workspace/startwithopenclaw/screenshot_hero.png')

# Scroll to course banner
driver.execute_script("window.scrollTo(0, 600)")
time.sleep(1)
driver.save_screenshot('/root/.openclaw/workspace/startwithopenclaw/screenshot_course_banner.png')

# Scroll to providers
driver.execute_script("window.scrollTo(0, 1500)")
time.sleep(1)
driver.save_screenshot('/root/.openclaw/workspace/startwithopenclaw/screenshot_providers.png')

# Scroll to course page
# driver.get('http://localhost:8082/course/index.html')
# time.sleep(2)
# driver.save_screenshot('/root/.openclaw/workspace/startwithopenclaw/screenshot_course_page.png')

driver.quit()
print("Screenshots saved!")
