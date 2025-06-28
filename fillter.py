import json

# Đọc dữ liệu từ file JSON
with open("menu_mintea.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Lọc trùng theo 'name'
seen_names = set()
unique_items = []

for item in data:
    name = item.get("name")
    if name not in seen_names:
        seen_names.add(name)
        unique_items.append(item)

# Ghi dữ liệu đã lọc ra file mới
with open("menu_mintea_dup.json", "w", encoding="utf-8") as f:
    json.dump(unique_items, f, ensure_ascii=False, indent=4)

print(f"Đã lọc trùng. Số món còn lại: {len(unique_items)}")
