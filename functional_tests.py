from selenium.webdriver.firefox.service import Service

from selenium import webdriver

service = Service("/snap/bin/firefox.geckodriver")
browser = webdriver.Firefox( service=service)

browser.get('http://localhost:8000')

assert 'django' in browser.title
