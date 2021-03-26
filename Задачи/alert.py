from selenium import webdriver
driver = webdriver.Chrome(executable_path="c:\chromedriver\chromedriver.exe")
import math
import time
def calc(y):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
     browser = webdriver.Chrome()
     link = "http://suninjuly.github.io/alert_accept.html"
     browser.get(link)
     button1 = browser.find_element_by_xpath("/html/body/form/div/div/button")
     button1.click()
     confirm = browser.switch_to.alert
     confirm.accept()
     x = browser.find_element_by_id("input_value").text
     value = calc("y")
     print(value)
     input = browser.find_element_by_id("answer")
     input.send_keys(value)

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
