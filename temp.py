import json 

photo = input("path: ")
d = 0
with open(photo, 'rb') as file:
    d = file.read()

print(d)
d = {
    "user_name": input("Nombre: "),
    "theme": int(input("theme (0/1): ")),
    "lenguague": input("lenguague (es/en): "),
    "font_size": float(input("fontsize: ")),
    "menu_color": input("menucolor: "),
    "foreground": input("foreground: "),
    "photo": str(d)
}


with open("config.json", 'w', encoding='utf-8') as file:
    json.dump(d, file, indent=4)