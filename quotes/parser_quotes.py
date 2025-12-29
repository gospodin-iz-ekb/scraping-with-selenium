### импорт библиотек
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

chrome_options = Options()  # переменная под опции

chrome_options.add_argument("--incognito")  # задаем опцию incognito, чтобы браузер не выдавал предупреждения
chrome_options.add_argument("--headless")  # задаем опцию headless, чтобы браузер работал в фон. режиме

### открытие сайта
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://quotes.toscrape.com/js/")

wait = WebDriverWait(driver, 10)  # ввод переменной для ожидания

### находим кнопку и кликаем по ней
login_link = wait.until(EC.element_to_be_clickable(("link text", "Login")))
login_link.click()

### ввод переменной под логин и пароль
Username = "soul"
Password = "goodman"

### вход в аккаунт
username = wait.until(EC.presence_of_element_located(("name", "username")))
username.clear()
username.send_keys(Username)
password = wait.until(EC.presence_of_element_located(("name", "password")))
password.clear()
password.send_keys(Password)
password.send_keys(Keys.RETURN)

### функция, которая собирает цитаты со всех страниц
def get_quotes():

    while 1:
        boxes = wait.until(EC.presence_of_all_elements_located(("xpath", "//div[@class='quote']")))  # нахождение ячеек с информацией
        for index in range(len(boxes)):
            current_boxes = wait.until(EC.presence_of_all_elements_located(("xpath", "//div[@class='quote']")))  # нахождение ТЕКУЩИХ ячеек
            quote = current_boxes[index].find_element("class name", "text").text  # запись цитаты

            ### переход на сайт с информацией об авторе
            about_author = current_boxes[index].find_element("xpath", ".//a[text()='(about)']")
            about_author.click()

            # запись имени и информации о рождении автора
            name_author = wait.until(EC.presence_of_element_located(("xpath", "//h3"))).text
            born_author = wait.until(EC.presence_of_element_located((
                "xpath", "//span[@class='author-born-date']"))).text + ' ' + wait.until(EC.presence_of_element_located((
                "xpath", "//span[@class='author-born-location']"))).text

            driver.back()  # возврат на предыдущую страницу

            yield quote, name_author, born_author

        ### попытка найти переход на следующую страницу
        try:
            next_button = driver.find_element("xpath", "//li/a[text()='Next ']")
            next_button.click()
        except:
            break  # если кнопки для перехода нет, функция прекращается

    driver.close()  # закрытие браузера



