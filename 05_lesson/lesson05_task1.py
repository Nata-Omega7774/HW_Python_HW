from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def click_blue_button():
    # Настройка Chrome для видимого режима и обхода SSL ошибок
    chrome_options = Options()
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--window-size=1024,768")
    
    driver = webdriver.Chrome(options=chrome_options)
    
    try:
        print("Открываем страницу...")
        driver.get("http://uitestingplayground.com/classattr")
        time.sleep(1)  # Даем странице загрузиться
        
        print("Ищем синюю кнопку...")
        blue_button = driver.find_element(By.CSS_SELECTOR, "button.btn-primary")
        print("Найдена кнопка с текстом:", blue_button.text)
        
        print("Кликаем по кнопке...")
        blue_button.click()
        time.sleep(1)  # Даем время для визуальной проверки
        
        # Обработка алерта (если появится)
        try:
            alert = driver.switch_to.alert
            print("Обнаружен alert с текстом:", alert.text)
            alert.accept()
            print("Alert закрыт")
        except:
            print("Alert не появился")
            
    except Exception as e:
        print("Ошибка:", str(e))
    finally:
        print("Закрываем браузер...")
        driver.quit()
        print("Готово!")

if __name__ == "__main__":
    click_blue_button()
    print("\nСкрипт выполнен. Запустите его еще два раза для проверки.")
