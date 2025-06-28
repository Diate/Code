from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import json

# Khởi tạo trình duyệt
options = Options()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36")
driver = webdriver.Chrome(options=options)

# Truy cập link GrabFood
url = 'https://food.grab.com/vn/vi/restaurant/online-delivery/5-C7D3DA3ATNDALJ?sourceID=20250626_170118_F8AEFF3AAC5E4879A3C92757AE799F1D_MEXMPS'
driver.get(url)
time.sleep(5)  # Đợi load xong

# Cuộn xuống để load toàn bộ món
for _ in range(30):
    driver.execute_script("window.scrollBy(0, 500);")
    time.sleep(2)

# Lưu dữ liệu
menu_data = []

# Lấy tên món, giá, hình ảnh
items = driver.find_elements(By.CLASS_NAME, 'menuItemWrapper___1xIAB')  # class này có thể thay đổi

for item in items:
    try:
        name = ''
        price = ''
        image = ''
        name = item.find_element(By.CLASS_NAME, 'itemNameTitle___1sFBq').text
        price = item.find_element(By.CLASS_NAME, 'discountedPrice___3MBVA').text
        image = item.find_element(By.TAG_NAME, 'img').get_attribute('src')

        menu_data.append({
            "name": name,
            "price": price,
            "image": image
        })
    except:
        continue

driver.quit()

# Ghi ra file JSON
with open("menu_mintea.json", "w", encoding="utf-8") as f:
    json.dump(menu_data, f, ensure_ascii=False, indent=4)

print("Đã lưu vào menu.json")
