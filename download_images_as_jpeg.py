import os
import json
import requests
from PIL import Image
from io import BytesIO
import re

# Hàm chuẩn hóa tên file: bỏ dấu, khoảng trắng, ký tự đặc biệt
def sanitize_filename(name):
    name = name.strip().replace(' ', '_')
    name = re.sub(r'[^\w\-_.]', '', name)
    return name

# Tạo thư mục lưu ảnh
output_dir = "menu_images"
os.makedirs(output_dir, exist_ok=True)

# Đọc dữ liệu từ JSON
with open("menu_deduplicated.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Tải và lưu ảnh
for i, item in enumerate(data):
    try:
        name = sanitize_filename(item['name'])
        img_url = item['image']

        response = requests.get(img_url, timeout=10)
        if response.status_code != 200:
            print(f"[{i}] Không tải được ảnh cho món: {item['name']}")
            continue

        img = Image.open(BytesIO(response.content)).convert("RGB")  # Chuyển sang RGB nếu là PNG/WebP
        save_path = os.path.join(output_dir, f"{name}.jpg")
        img.save(save_path, format="JPEG", quality=90)

        print(f"[{i}] Đã lưu: {save_path}")
    except Exception as e:
        print(f"[{i}] Lỗi với món '{item['name']}': {e}")
