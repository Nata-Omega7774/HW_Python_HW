from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager  # Исправленный импорт
from selenium.webdriver.firefox.service import Service    # Исправленный импорт

def test_firefox():
    try:
        # 1. Настройка сервиса
        service = Service(GeckoDriverManager().install())
        
        # 2. Опции Firefox (режим без GUI)
        options = webdriver.FirefoxOptions()
        options.add_argument("--headless")
        
        # 3. Инициализация драйвера
        driver = webdriver.Firefox(service=service, options=options)
        
        # 4. Тестовые действия
        driver.get("https://uitestingplayground.com/")
        print("✅ Страница загружена. Заголовок:", driver.title)
        
    except Exception as e:
        print(f"❌ Ошибка: {e}")
    finally:
        if 'driver' in locals():
            driver.quit()
            print("✖ Браузер закрыт")

if __name__ == "__main__":
    test_firefox()
