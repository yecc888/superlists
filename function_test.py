from selenium import webdriver
driver = webdriver.Firefox()
driver.get("http://127.0.0.1:8000/")
assert "Django" in driver.title
t = driver.title
print(t)
