import time
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

from selenium import webdriver


def create_driver(browser="yandex"):
    if browser == "yandex":
        yandex_driver_path = 'yandexdriver.exe'  # путь к Yandex WebDriver
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=Service(yandex_driver_path), options=options)
    else:
        # Используем WebDriver для Chrome
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    return driver


def test_saucedemo(browser="yandex"):
    driver = create_driver(browser)
    # 1. Открытие сайта
    driver.get("https://www.saucedemo.com")
    driver.maximize_window()

    # 2. Авторизация
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # 3. Добавление товара в корзину
    try:
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "inventory_item"))
        ).click()

        items = driver.find_elements(By.CLASS_NAME, "inventory_item")
        for item in items:
            name = item.find_element(By.CLASS_NAME, "inventory_item_name").text
            if name == "Sauce Labs Bike Light":
                # Нажимаем кнопку "Add to cart"
                item.find_element(By.CLASS_NAME, "btn_inventory").click()
                break

    except TimeoutException:
        # Делаем скриншот в случае таймаута для отладки
        driver.save_screenshot("screenshot_error.png")
        print("Элемент не найден. Проверьте скриншот.")
        driver.quit()
        return

    # 4. Переход в корзину
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # 5. Проверка, что товар в корзине
    assert driver.find_element(By.CLASS_NAME, "inventory_item_name").text == "Sauce Labs Bike Light"

    # 6. Оформление заказа
    driver.find_element(By.ID, "checkout").click()
    driver.find_element(By.ID, "first-name").send_keys("Test")
    driver.find_element(By.ID, "last-name").send_keys("User")
    driver.find_element(By.ID, "postal-code").send_keys("12345")
    driver.find_element(By.ID, "continue").click()
    driver.find_element(By.ID, "finish").click()

    # 7. Проверка успешного завершения заказа
    success_message = driver.find_element(By.CLASS_NAME, "complete-header").text
    assert success_message == "Thank you for your order!"

    # 8. Завершение теста
    print("Тест успешно выполнен!")
    time.sleep(2)  # Для того чтобы успеть увидеть результат

    driver.quit()


test_saucedemo(browser='yandex')
