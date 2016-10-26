import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


info = open("info.txt").read()
NETID,PASSWORD = info.split()

DOWNLOAD_PATH = "C:\\Downloads"

def getNUM(text):
	text = text.strip()
	ind = text.index("#")
	return int(text[ind+1:])


delay = 20

chromeOptions = webdriver.ChromeOptions()

chromeOptions.add_argument("download.default_directory=%s"%DOWNLOAD_PATH)

''' Me trying to disable 'This type of file can harm your computer' pop up '''
chromeOptions.add_argument("download.directory_upgrade=true")
chromeOptions.add_argument("download.prompt_for_download=false")
chromeOptions.add_argument("safebrowsing.enabled=true")
chromeOptions.add_argument("profile.default_content_settings.popups=0")
chromeOptions.add_argument("--safebrowsing-disable-download-protection")
chromeOptions.add_argument("--safebrowsing-disable-extension-blacklist")
chromeOptions.add_argument("--disable-improved-download-protection")
''' I guess I failed.... '''

driver = webdriver.Chrome(chrome_options=chromeOptions)  # Optional argument, if not specified will search path.
driver.get('https://prairielearn.engr.illinois.edu/cs225/')
# enter netid
netid_box = driver.find_element_by_name('j_username')
netid_box.send_keys(NETID)
# enter password
password_box = driver.find_element_by_name('j_password')
password_box.send_keys(PASSWORD)
# submit
submit = driver.find_element_by_name('_eventId_proceed')
submit.click()

WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Problem of the Day")))

potd_link = driver.find_elements_by_partial_link_text('Problem of the Day')
NUM = getNUM(potd_link[-1].text)


driver.get('https://prairielearn.engr.illinois.edu/cs225/#q/potd-q%d/1/1'%NUM)

WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Download")))
download_link = driver.find_element_by_partial_link_text('Download')
download_link.click()
