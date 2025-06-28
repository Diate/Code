import os
import json
from PIL import Image
import re

# Thư mục ảnh ban đầu
img_folder = "menu_images"
output_folder = "menu_images_renamed"
os.makedirs(output_folder, exist_ok=True)

# Đọc JSON
with open("menu_deduplicated.json", "r", encoding="utf-8") as f:
    data = json.load(f)

new_data = []

for idx, item in enumerate(data, start=1):
    index_str = f"{idx:03}"  # 001, 002,...
    item["index"] = index_str

    # Tên ảnh gốc (dựa theo script cũ bạn đã tải về)
    raw_name = item["name"].strip().replace(" ", "_")
    raw_name = re.sub(r"[^\w\-_.]", "", raw_name)
    original_path = os.path.join(img_folder, f"{raw_name}.jpg")

    # Tên ảnh mới
    new_filename = f"{index_str}.jpg"
    new_path = os.path.join(output_folder, new_filename)

    # Đổi tên file nếu tồn tại
    if os.path.exists(original_path):
        img = Image.open(original_path).convert("RGB")
        img.save(new_path, format="JPEG", quality=90)
        print(f"✔ Đổi: {original_path} → {new_path}")
    else:
        print(f"✘ Không tìm thấy ảnh: {original_path}")

    new_data.append(item)

# Ghi lại JSON mới
with open("menu_with_index.json", "w", encoding="utf-8") as f:
    json.dump(new_data, f, ensure_ascii=False, indent=4)

print("✅ Hoàn tất: ảnh đã được đổi tên và JSON đã cập nhật chỉ số.")
