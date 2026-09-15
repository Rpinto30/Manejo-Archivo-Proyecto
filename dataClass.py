

class Settings:
    def __init__(self,
                 user_name,
                 theme,
                 lenguague,
                 font_size,
                 menu_color,
                 foreground,
                 photo):
        self.user_name = user_name
        self.theme = theme
        self.lenguague = lenguague
        self.font_size = font_size
        self.menu_color = menu_color
        self.foreground = foreground
        self.photo = photo
        
    def setJson(self):
        return {
            "user_name": self.user_name,
            "theme": self.theme,
            "lenguague": self.lenguague,
            "font_size": self.font_size,
            "menu_color": self.menu_color,
            "foreground": self.foreground,
            "photo": str(self.photo)
        }
        
    def __str__(self):
        return f"""
                user_name: {self.user_name},
                theme: {self.theme},
                lenguague: {self.lenguague},
                font_size: {self.font_size},
                menu_color: {self.menu_color},
                foreground: {self.foreground},
                photo: {self.photo[:20]}"""

import os
class Memories:
    MEMORIES_PATH = '.data/text/memories'

    def __init__(self):
        pass
        
    def save(self, i: int, s: str):
        with open(self.MEMORIES_PATH + f'_{i}.txt', 'w', encoding='utf-8') as file:
            file.write(s)
            print("Guardado")

    def load(self, i: int):
        try:
            with open(self.MEMORIES_PATH + f'_{i}.txt', 'r', encoding='utf-8') as file:
                s =  file.read()
            return s
        except:
            return ''
        
    def delete(self, i: int):
        if os.path.exists(self.MEMORIES_PATH + f'_{i}.txt'):
            os.remove(self.MEMORIES_PATH + f'_{i}.txt')