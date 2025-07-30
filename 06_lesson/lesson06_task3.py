from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def main():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    
    try:
        # 1. Перейти на страницу
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
        
        # 2. Дождаться загрузки всех картинок
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "img[id^='image']"))
        )
        
        # 3. Получить src 3-й картинки
        src = driver.find_element(By.CSS_SELECTOR, "#landscape").get_attribute("src")
        
        # 4. Вывести значение в консоль
        print(src)
    
    finally:
        driver.quit()

if __name__ == "__main__":
    main()