import json
import os
from dataClass import Settings
SETTINGS_PATH = ".data/config.json"
SETTINGS_PATH_TEMP = ".data/config_temp.json"
SETTINGS_PATH_BACKUP = ".data/config.bak"

def load() -> Settings:
    try:
        with open(SETTINGS_PATH, 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        if data:
            return Settings(
                data["user_name"],
                data["theme"],
                data["lenguague"],
                data["font_size"],
                data["menu_color"],
                data["foreground"],
                data["photo"]
            )
        else:
            return Settings(
                "N/A",
                0,
                "es",
                15,
                "#F5F5F5",
                "#242424",
                ""
            )
    except:
        if os.path.exists(SETTINGS_PATH_BACKUP):
            new_path = SETTINGS_PATH_BACKUP.replace('.bak', '.json')
            with open(SETTINGS_PATH_BACKUP, 'rb') as origin, open(new_path, 'wb') as new_:
                new_.write(origin.read())
            
            with open(new_path, "r", encoding="utf-8") as old_file:
                old = json.load(old_file)
            
            return Settings(
                old["user_name"],
                old["theme"],
                old["lenguague"],
                old["font_size"],
                old["menu_color"],
                old["foreground"],
                old["photo"]
            )
            
        else:
            return Settings(
                        "N/A",
                        0,
                        "es",
                        15,
                        "#F5F5F5",
                        "#242424",
                        ""
                    )

def save(settings: Settings):
    try:
        with open(SETTINGS_PATH_TEMP, 'w', encoding='utf-8') as file:
            json.dump(
                settings.setJson(), 
                file,
                indent=4)
            #print(settings.setJson())
            
        if os.path.exists(SETTINGS_PATH_TEMP):
            with open(SETTINGS_PATH_TEMP, "r", encoding="utf-8") as old_file:
                old = json.load(old_file)
            with open(SETTINGS_PATH_BACKUP, "w", encoding="utf-8") as new_file:
                json.dump(old, new_file, indent=4, ensure_ascii=False)

            os.replace(SETTINGS_PATH_TEMP, SETTINGS_PATH)
        
        if os.path.exists(SETTINGS_PATH_TEMP):
            os.rename(SETTINGS_PATH_TEMP, SETTINGS_PATH)
    except:
        with open(SETTINGS_PATH_TEMP, 'w', encoding='utf-8') as file:
            json.dump(
                Settings(
                        "N/A",
                        0,
                        "es",
                        15,
                        "#F5F5F5",
                        "#242424",
                        ""
                    ).setJson(), 
                file,
                indent=4)
        if os.path.exists(SETTINGS_PATH_TEMP):
            os.rename(SETTINGS_PATH_TEMP, SETTINGS_PATH)
