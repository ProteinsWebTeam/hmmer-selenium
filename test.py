from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://www.ebi.ac.uk/Tools/hmmer/')

assert 'HMMER' in browser.title