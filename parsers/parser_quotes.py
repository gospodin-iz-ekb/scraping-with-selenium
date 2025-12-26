from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options ### импорт библиотек
import time

chrome_options = Options()

chrome_options.add_argument("--incognito") # задаем опцию incognito, чтобы браузер не выдавал предупреждения
chrome_options.add_argument("--headless")  # задаем опцию headless, чтобы браузер работал в фон. режиме

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://quotes.toscrape.com/js/") ### открытие сайта

wait = WebDriverWait(driver, 10) # ввод переменной для ожидания

login_link = wait.until(EC.element_to_be_clickable(("link text", "Login")))  ### находим кнопку и кликаем по ней
login_link.click()

Username = "soul"
Password = "goodman"  ### ввод переменной под логин и пароль

username = wait.until(EC.presence_of_element_located(("name", "username")))
username.clear()
username.send_keys(Username)
password = wait.until(EC.presence_of_element_located(("name", "password")))
password.clear()
password.send_keys(Password)
password.send_keys(Keys.RETURN)  ### вход в аккаунт


def get_quotes():       ### функция, которая собирает цитаты со всех страниц

    while 1:
        boxes = wait.until(EC.presence_of_all_elements_located(("xpath", "//div[@class='quote']")))
        for index in range(len(boxes)):
            current_boxes = wait.until(EC.presence_of_all_elements_located(("xpath", "//div[@class='quote']")))
            quote = current_boxes[index].find_element("class name", "text").text

            about_author = current_boxes[index].find_element("xpath", ".//a[text()='(about)']")
            about_author.click()

            name_author = wait.until(EC.presence_of_element_located(("xpath", "//h3"))).text
            about_born_author = wait.until(EC.presence_of_element_located((
                "xpath", "//span[@class='author-born-date']"))).text + ' ' + wait.until(EC.presence_of_element_located((
                "xpath", "//span[@class='author-born-location']"))).text

            driver.back()

            print(quote + '\n' + name_author + '\n' + about_born_author)

        try:
            next_button = driver.find_element("xpath", "//li/a[text()='Next ']")  ### попытка найти переход на следующую страницу
            next_button.click()
        except:
            break          ### если кнопки для перехода нет, функция прекращается

    driver.close()   ### закрытие браузера

if __name__ == "__main__":   ### запуск функции
    get_quotes()

