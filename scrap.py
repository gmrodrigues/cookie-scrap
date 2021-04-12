from selenium import webdriver
import sys

url = sys.argv[1] # any website here ex: https://google.com

fireFoxOptions = webdriver.FirefoxOptions()
fireFoxOptions.set_headless()
brower = webdriver.Firefox(options=fireFoxOptions)
brower.get(url)

cookies = brower.get_cookies()

print(cookies)