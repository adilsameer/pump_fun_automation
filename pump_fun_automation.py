import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def start_instance():
    global driver
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()


def auto_wallet_connect():
    driver.get("https://pump.fun/board")
    # Time for manual account creation which can be automated
    # time.sleep(200)

    pass


def setup_website():
    driver.get("https://pump.fun/board")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="radix-:r0:"]/button'))).click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="btn-reject-all"]'))).click()
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, '/html/body/main/div/div[3]/div[1]/div[2]/div[2]/div[1]/div[3]'))).click()


def perform_automation(comment):
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/main/div/div[3]/div[2]/a')))
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div[3]/div[2]/a'))).click()
    time.sleep(1)
    divs = WebDriverWait(driver, 10).until(
        EC.visibility_of_all_elements_located((By.XPATH, '/html/body/main/div[2]/div[2]/div[1]/div[4]/div')))
    # print(len(divs))
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, f'/html/body/main/div[2]/div[2]/div[1]/div[4]/div[{len(divs)}]')))
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, f'body > main > div.md\:block.hidden.mt-16.p-4.mb-16 > div.flex.space-x-8.mt-4 > div.flex.flex-col.gap-2.w-2\/3 > div.text-slate-300.grid.gap-1.relative > div.justify-self-center.hover\:underline.cursor-pointer'))).click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="text"]'))).send_keys(
        f"{comment}")
    for i in range(1, 15):
        try:
            driver.find_element(By.XPATH, f'/html/body/div[{i}]/button').click()
            print("Commented Successfully")
        except NoSuchElementException:
            pass
        else:
            break
    time.sleep(2)
    driver.get('https://pump.fun/board')


def end_automation():
    driver.quit()


start_instance()
to_stop = False
setup_website()
# auto_wallet_connect()
i = 0
message = "Hey I found this amazing bot @pump_pump_fun_bot for trading try this"
while not to_stop:
    i += 1
    print(f"Script Running for {i} times...")
    perform_automation(message)
