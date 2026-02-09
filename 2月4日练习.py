old_str = " Agent:007_Bond; Coords:(40,74); Items:gun,money,gun; Mission:2025-RESCUE-X "
new_str = old_str.strip()
parts = new_str.split(";")
new_list = []
new_dict = {}
for p in parts:
    if p.strip():
        part = p.strip()
        new_list.append(part)
for p in new_list:
    temp = p.split(":",1)
    key,value = temp
    if key == "Agent":
        new_dict[key] = value
    elif key == "Coords":
        new_dict[key] = value
    elif key == "Mission":
        new_dict[key] = value
    elif key == "Items":
        Items_list = value.split(",")
        unique_Items = list(set(Items_list))
        new_dict[key] = unique_Items
print(new_dict)


