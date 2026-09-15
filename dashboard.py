from dataClass import Settings, Memories
from settings import load, save
from dialogs import FormularioFuente, FormularioLenguaje, FormularioTema, FormularioUsuario, FormularioFondo


from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt, QTranslator)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout, QPushButton, QFileDialog,
    QLabel, QMainWindow, QSplitter, QMenu, QMenuBar, QTextEdit, QMessageBox, QColorDialog, QDialog, 
    QPlainTextEdit, QSizePolicy, QVBoxLayout, QWidget)

class DashBoard(QMainWindow):
    INIT_SIZE_IMG = [600,400]
    settings = None
    memories = Memories()
    
    menu_color_light =  "#F5F5F5" 
    menu_color_dark = "#1F1F1F" 
    index_page = 1
    
    foreground = ""
    
    def get_light_stylesheet(self):
        settings = self.settings
        menu_color_light = self.menu_color_light
        font_color = settings.foreground if (settings and settings.foreground) else "#3E2723"
        font_size = settings.font_size if (settings and settings.font_size) else 13
        return f"""
    QMainWindow {{
        background-color: {menu_color_light if settings.menu_color == "#F5F5F5" else settings.menu_color};
    }}
 
    QLabel {{
        color: {"#FAFAD1"};
        font-family: "Georgia", "Garamond", serif;
        font-size: 15pt;
    }}
 
    QLabel#labelHeader {{
        color: #6B2D2D;
        font-weight: bold;
        font-style: italic;
    }}
 
    QLabel#optionsLabel {{
        color: {'#7B5E3C'};
        font-weight: 600;
    }}
    
    QLabel#actual_page_label {{
            color: {'#7B5E3C'};
            font-weight: 600;
        }}
 
    QFrame#leftFrame {{
        background-color: #FBF6E9;
        border: 2px solid #C9A66B;
        border-radius: 10px;
        margin: 4px;
    }}
 
    QFrame#rightFrame {{
        background-color: #FFFDF6;
        border: 2px solid #C9A66B;
        border-radius: 10px;
        margin: 4px;
    }}
 
    QPlainTextEdit#textData {{
        background-color: #FFFDF6;
        color: {font_color};
        border: 1px solid #C9A66B;
        border-radius: 6px;
        padding: 10px;
        font-family: "Georgia", "Garamond", serif;
        font-size: {font_size}pt;
    }}
 
    QPlainTextEdit#textData:focus {{
        border: 2px solid #8B4513;
        background-color: #FFFFFF;
    }}
 
    QMenuBar {{
        background-color: #6B2D2D;
        color: #F4ECD8;
        font-family: "Georgia", "Garamond", serif;
        font-size: 13px;
        border: none;
    }}
 
    QMenuBar::item {{
        background: transparent;
        padding: 6px 12px;
    }}
 
    QMenuBar::item:selected {{
        background-color: #8B4513;
    }}
 
    QMenu {{
        background-color: #FBF6E9;
        color: {"#F6F4B3"};
        border: 1px solid #C9A66B;
        padding: 4px;
    }}
 
    QMenu::item {{
        padding: 6px 24px 6px 12px;
        border-radius: 4px;
    }}
 
    QMenu::item:selected {{
        background-color: #EADCC0;
        color: #6B2D2D;
    }}
 
    QSplitter::handle {{
        background-color: #C9A66B;
        width: 4px;
    }}
 
    QSplitter::handle:hover {{
        background-color: #8B4513;
    }}
    
    QPushButton {{
    background-color: #EADCC0;
    color: #3E2723;
    border: 2px solid #C9A66B;
    border-radius: 8px;
    padding: 8px 16px;
    font-family: "Georgia", "Garamond", serif;
    font-weight: 600;
}}

QPushButton:hover {{
    background-color: #DCC79A;
    border-color: #8B4513;
}}

QPushButton:pressed {{
    background-color: #C9A66B;
    color: #FFFDF6;
}}

QPushButton:disabled {{
    background-color: #E8E0D0;
    color: #A89880;
    border-color: #D8C9A8;
}}

QPushButton#btnPrev, QPushButton#btnNext {{
    background-color: #EADCC0;
    color: #6B2D2D;
    border: 2px solid #C9A66B;
    border-radius: 18px;
    min-width: 36px;
    max-width: 36px;
    min-height: 36px;
    max-height: 36px;
    font-family: "Georgia", "Garamond", serif;
    font-weight: bold;
    padding: 0px;
}}

QPushButton#btnPrev:hover, QPushButton#btnNext:hover {{
    background-color: #DCC79A;
    border-color: #8B4513;
    color: #3E2723;
}}

QPushButton#btnPrev:pressed, QPushButton#btnNext:pressed {{
    background-color: #C9A66B;
    color: #FFFDF6;
}}

QPushButton#btnPrev:disabled, QPushButton#btnNext:disabled {{
    background-color: #E8E0D0;
    color: #C9BBA0;
    border-color: #D8C9A8;
}}

    """
    #dark_mode
    def get_dark_stylesheet(self):
        settings = self.settings
        menu_color_dark = self.menu_color_dark
        font_color = settings.foreground if (settings and settings.foreground) else "#E8D9B5"
        font_color_text = settings.foreground if (settings and settings.foreground) else "#F0E3C4"
        font_size = settings.font_size if (settings and settings.font_size) else 13
        return f"""
    /* Estilo base de la ventana */
    QMainWindow {{
        background-color: {menu_color_dark if settings.menu_color == "#1F1F1F" else settings.menu_color};
    }}
 
    /* Menú Superior y Dropdowns */
    QMenuBar {{
        background-color: #1B130D;
        color: #E8D9B5;
        font-family: "Georgia", "Garamond", serif;
        font-size: 13px;
        border-bottom: 1px solid #4A3826;
    }}
 
    QMenuBar::item {{
        background: transparent;
        padding: 6px 12px;
    }}
 
    QMenuBar::item:selected {{
        background-color: #3B2A1D;
    }}
 
    QMenu {{
        background-color: #2B1F16;
        color: #E8D9B5;
        border: 1px solid #4A3826;
        padding: 4px;
    }}
 
    QMenu::item {{
        padding: 6px 24px 6px 12px;
        border-radius: 4px;
    }}
 
    QMenu::item:selected {{
        background-color: #4A3826;
        color: #D9B96C;
    }}
 
    /* Panel Izquierdo (Lateral) */
    QFrame#leftFrame {{
        background-color: #2B1F16;
        border: 1px solid #4A3826;
        border-radius: 10px;
        margin: 4px;
    }}
 
    /* Panel Derecho (Contenido Principal) */
    QFrame#rightFrame {{
        background-color: #2B1F16;
        border: 1px solid #4A3826;
        border-radius: 10px;
        margin: 4px;
    }}
 
    /* Etiquetas y Textos */
    QLabel {{
        color: {font_color};
        font-family: "Georgia", "Garamond", serif;
        font-size: {font_size}pt;
    }}
 
    QLabel#labelHeader {{
        color: #D9B96C;
        font-weight: bold;
        font-style: italic;
    }}
 
    QLabel#optionsLabel {{
        color: #C2A878;
        font-weight: 600;
    }}
    
    QLabel#actual_page_label {{
        color: {'#C2A878'};
        font-weight: 600;
    }}

    /* Área de Texto / Editor de Blog */
    QPlainTextEdit#textData {{
        background-color: #1E1610;
        color: {font_color_text};
        border: 1px solid #4A3826;
        border-radius: 6px;
        padding: 10px;
        font-family: "Georgia", "Garamond", serif;
        font-size: {font_size}pt;
    }}
 
    QPlainTextEdit#textData:focus {{
        border: 2px solid #D9B96C;
    }}
 
    QSplitter::handle {{
        background-color: #4A3826;
        width: 4px;
    }}
 
    QSplitter::handle:hover {{
        background-color: #D9B96C;
    }}
    
    QPushButton {{
    background-color: #3B2A1D;
    color: #E8D9B5;
    border: 2px solid #4A3826;
    border-radius: 8px;
    padding: 8px 16px;
    font-family: "Georgia", "Garamond", serif;
    font-weight: 600;
}}

QPushButton:hover {{
    background-color: #4A3826;
    border-color: #D9B96C;
}}

QPushButton:pressed {{
    background-color: #2B1F16;
    color: #D9B96C;
}}

QPushButton:disabled {{
    background-color: #241A12;
    color: #6B5A46;
    border-color: #3B2A1D;
}}

QPushButton#btnPrev, QPushButton#btnNext {{
    background-color: #3B2A1D;
    color: #D9B96C;
    border: 2px solid #4A3826;
    border-radius: 18px;
    min-width: 36px;
    max-width: 36px;
    min-height: 36px;
    max-height: 36px;
    font-family: "Georgia", "Garamond", serif;
    font-weight: bold;
    padding: 0px;
}}

QPushButton#btnPrev:hover, QPushButton#btnNext:hover {{
    background-color: #4A3826;
    border-color: #D9B96C;
    color: #F0E3C4;
}}
QPushButton#btnPrev:pressed, QPushButton#btnNext:pressed {{
    background-color: #2B1F16;
    color: #D9B96C;
}}

QPushButton#btnPrev:disabled, QPushButton#btnNext:disabled {{
    background-color: #241A12;
    color: #5A4C3A;
    border-color: #3B2A1D;
}}
    """
    
    
    def __init__(self):
        super().__init__()
        self.init_load_config()
        self.setupUi(self)
        self.widgets_load_config()
    
    def init_load_config(self):
        self.settings = load()
        
    def widgets_load_config(self):
        #self.labelBottom.setText("Nombre de usuario: "+self.settings.user_name)
        self.labelHeader.setText("Memorias de " + self.settings.user_name)
        
        self.font_global.setPointSize(self.settings.font_size)
        
        self.textData.setFont(self.font_global)
        #self.labelBottom.setFont(self.font_global)
        
        if self.settings.theme == 1:
            self.setStyleSheet(self.get_light_stylesheet())
        else: 
            self.setStyleSheet(self.get_dark_stylesheet())

        self.aplicar_idioma(self.settings.lenguague)
        
        self.load_image(
            self.settings.photo[2:-1].encode('utf-8').decode('unicode_escape').encode('latin-1')
        )
        
        self.sol_load()
        self.info_label.hide()
        print("todo cargado!")
       
        
    
    #===================================sSOLS (oara las QaCTIONS)
    def sol_name(self):
        dialog = FormularioUsuario(self, self.settings.user_name)
        dialog.setStyleSheet(f"font-size: 14px; color: white; background-color: #202020")
                
        if dialog.exec() == QDialog.DialogCode.Accepted:
            self.settings.user_name = dialog.obtener_resultado()
            #self.labelBottom.setText("Nombre de usuario: "+self.settings.user_name)
            self.labelHeader.setText("Memorias de " + self.settings.user_name)
            print( self.settings.user_name)
            save(self.settings)
    
    def sol_theme(self):
        dialog = FormularioTema(self, self.settings.theme)
        dialog.setStyleSheet(f"font-size: 14px; color: white; background-color: #202020")
                
        if dialog.exec() ==  QDialog.DialogCode.Accepted:
            self.settings.theme = dialog.obtener_resultado()
            
            if self.settings.theme == 1:
                self.setStyleSheet(self.get_light_stylesheet())
            else: 
                self.setStyleSheet(self.get_dark_stylesheet())
            save(self.settings)
    
    def sol_lenguague(self):
        dialog = FormularioLenguaje(self, 0 if self.settings.lenguague == 'es' else 1)
        dialog.setStyleSheet(f"font-size: 14px; color: white; background-color: #202020")

        if dialog.exec() ==  QDialog.DialogCode.Accepted:
            self.settings.lenguague = dialog.obtener_resultado()
            print(self.settings.lenguague)
            save(self.settings)
            self.aplicar_idioma(self.settings.lenguague)
    
    def sol_font(self):
        dialog = FormularioFuente(self, self.settings.font_size, self.settings.foreground)
        dialog.setStyleSheet(f"font-size: 14px; color: white; background-color: #202020")
        
        if dialog.exec() ==  QDialog.DialogCode.Accepted:
            r = dialog.obtener_resultado()
            self.settings.foreground = r['color_hex']
            self.settings.font_size = r['tamano']
            
            self.font_global.setPointSize(self.settings.font_size)
            if self.settings.theme == 1:
                self.setStyleSheet(self.get_light_stylesheet())
            else: 
                self.setStyleSheet(self.get_dark_stylesheet())
            save(self.settings)
    
    def sol_background(self):
        dialog = FormularioFondo(self, self.settings.menu_color)
        #dialog.setStyleSheet(f"font-size: 14px; color: white; background-color: #202020")
        
        if dialog.exec() ==  QDialog.DialogCode.Accepted:
            r = dialog.obtener_resultado()
            self.settings.menu_color = r['color_hex']
            if self.settings.theme == 1:
                self.setStyleSheet(self.get_light_stylesheet())
            else: 
                self.setStyleSheet(self.get_dark_stylesheet())
            save(self.settings)
    
    def sol_image(self):
        path, _ = QFileDialog.getOpenFileName(
            self,
            "Selecciona tu imagen de usuario", 
            "",
            "Imágenes (*.png *.jpg *.jpeg *.gif)"
        )

        if path:
            try:
                pixmap = QPixmap(path)
                if not pixmap.isNull():
                    pixmap_escalado = pixmap.scaled(
                        self.INIT_SIZE_IMG[0], self.INIT_SIZE_IMG[1], 
                        Qt.AspectRatioMode.KeepAspectRatio, 
                        Qt.TransformationMode.SmoothTransformation
                    )
                    self.image.setPixmap(pixmap_escalado)
                with open(path, 'rb') as file:
                    self.settings.photo = file.read()
                save(self.settings)
            except:
                QMessageBox.critical(self, "Error al cargar imagen de usuario", "Parece hubo un error al cargar tu imagen de usuario, ingresa nuevamente el archivo")
                
    
    def sol_save(self, messageBox= False):
        s = self.textData.toPlainText()
        if s.strip() != '':
            self.memories.save(self.index_page, s)
        else:
            self.memories.delete(self.index_page)
        
        if messageBox:
            QMessageBox.information(self, "Guardado con exito", f"La pagina {self.index_page} fue guardada con exito!")
    
    def sol_load(self):
        s = self.memories.load(self.index_page)
        if s != '':
            self.textData.setPlainText(s)
            self.info_label.hide()
        else: 
            self.info_label.show()
            self.textData.setPlainText('')
    
    #===================================================================EXTRAS
    def load_image(self, bin):
        try:
            pixmap = QPixmap()
            pixmap.loadFromData(bin)
            self.image.setPixmap(pixmap.scaled(
                                    self.INIT_SIZE_IMG[0], self.INIT_SIZE_IMG[1], 
                                    Qt.AspectRatioMode.KeepAspectRatio, 
                                    Qt.TransformationMode.SmoothTransformation))
            self.settings.photo = bin
        except:
            QMessageBox.critical(self, "Error al cargar imagen de usuario", "Parece hubo un error al cargar tu imagen de usuario, ingresa nuevamente el archivo")
    
    def color_selector(self, var):
        color = QColorDialog.getColor(
            initial=QColor("blue"), 
            parent=self, 
            title="Selecciona un Color"
        )

        if color.isValid():
            var = color.name()
            print(f"Color seleccionado (HEX): {color.name()}")
            print(f"Color seleccionado (RGB): {color.red()}, {color.green()}, {color.blue()}")

    def aplicar_idioma(self, codigo):
        app = QApplication.instance()

        if getattr(self, "_translator", None) is not None:
            app.removeTranslator(self._translator)

        self._translator = QTranslator()

        if codigo not in ("es", "es-Es", ""):
            cargado = self._translator.load(f"translations/app_{codigo}.qm")
            if cargado:
                app.installTranslator(self._translator)
            else:
                print(f"Aviso: no se encontró traducción para '{codigo}'")

        self.retranslateUi(self)
        #RESTORE
        self.labelHeader.setText(self.labelHeader.text()+ " " + self.settings.user_name)

    def increment_page(self):
        self.sol_save()
        self.index_page += 1
        self.actual_page_label.setText(str(self.index_page))
        self.sol_load()
        print(self.index_page)
    
    def decrement_page(self):
        self.sol_save()
        if self.index_page == 1: return
        self.index_page -= 1
        self.actual_page_label.setText(str(self.index_page))
        self.sol_load()
        print(self.index_page)

    #=============================================================SETUP
    
    def toggle_panel_izquierdo(self):
        if self.leftFrame.isVisible():
            self._left_panel_prev_sizes = self.centralLayout.sizes()
            self.leftFrame.hide()
        else:
            self.leftFrame.show()
            if self._left_panel_prev_sizes:
                self.centralLayout.setSizes(self._left_panel_prev_sizes)
    
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(795, 415)
        MainWindow.setStyleSheet(self.get_light_stylesheet())
        #---------------------MENU---------------------
        self.actionNuevo = QAction(MainWindow)
        self.actionNuevo.setObjectName(u"actionNuevo")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentNew))
        self.font_global = QFont()
        self.font_global.setPointSize(self.settings.font_size if self.settings else 15)
 
        self.actionNuevo.setIcon(icon)
        self.actionAbrir = QAction(MainWindow)
        self.actionAbrir.setObjectName(u"actionAbrir")
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentOpen))
        self.actionAbrir.setIcon(icon1)
        self.actionGuardar = QAction(MainWindow)
        self.actionGuardar.setObjectName(u"actionGuardar")
        icon2 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentSave))
        self.actionGuardar.setIcon(icon2)
        self.actionSalir = QAction(MainWindow)
        self.actionSalir.setObjectName(u"actionSalir")
        icon3 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.EditClear))
        self.actionSalir.setIcon(icon3)
        self.actionCortar = QAction(MainWindow)
        self.actionCortar.setObjectName(u"actionCortar")
        icon4 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.EditCut))
        self.actionCortar.setIcon(icon4)
        self.actionPegar = QAction(MainWindow)
        self.actionPegar.setObjectName(u"actionPegar")
        icon5 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.EditPaste))
        self.actionPegar.setIcon(icon5)
        self.actionSeleccionar_Todo = QAction(MainWindow)
        self.actionSeleccionar_Todo.setObjectName(u"actionSeleccionar_Todo")
        icon6 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.EditSelectAll))
        self.actionSeleccionar_Todo.setIcon(icon6)
        self.actionVer_foto = QAction(MainWindow)
        self.actionVer_foto.setObjectName(u"actionVer_foto")
        icon7 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.UserAvailable))
        self.actionVer_foto.setIcon(icon7)
        self.actionPantalla_completa = QAction(MainWindow)
        self.actionPantalla_completa.setObjectName(u"actionPantalla_completa")
        self.actionMinimizar = QAction(MainWindow)
        self.actionMinimizar.setObjectName(u"actionMinimizar")
        self.actionNombre_de_usuario = QAction(MainWindow)
        self.actionNombre_de_usuario.setObjectName(u"actionNombre_de_usuario")
        self.actionNombre_de_usuario.triggered.connect(
            self.sol_name
        )
        icon8 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ContactNew))
        self.actionNombre_de_usuario.setIcon(icon8)
        self.actionTema_Claro_Oscuro = QAction(MainWindow)
        self.actionTema_Claro_Oscuro.setObjectName(u"actionTema_Claro_Oscuro")
        self.actionTema_Claro_Oscuro.triggered.connect(
            self.sol_theme
        )
        self.actionIdioma = QAction(MainWindow)
        self.actionIdioma.setObjectName(u"actionIdioma")
        self.actionIdioma.triggered.connect(
            self.sol_lenguague
        )
        self.actionBarra = QAction(MainWindow)
        self.actionBarra.setObjectName(u"actionBarra")
        self.actionBarra.triggered.connect(
            self.toggle_panel_izquierdo
        )
        
        self.actionColor_de_letra = QAction(MainWindow)
        self.actionColor_de_letra.setObjectName(u"actionColor_de_letra")
        self.actionColor_de_letra.triggered.connect(
            self.sol_font
        )
        self.actionFoto_de_perfil = QAction(MainWindow)
        self.actionFoto_de_perfil.setObjectName(u"actionFoto_de_perfil")
        self.actionFoto_de_perfil.triggered.connect(
            self.sol_image
        )
        
        self.actionBackground = QAction(MainWindow)
        self.actionBackground.setObjectName(u"actionBackground")
        self.actionBackground.triggered.connect(
            self.sol_background
        )
        
        
        #---------------------CENTRAL---------------------
        icon9 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.AddressBookNew))
        self.actionFoto_de_perfil.setIcon(icon9)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.centralframe = QFrame(self.centralwidget)
        self.centralframe.setObjectName(u"centralframe")
        self.centralframe.setStyleSheet(u"")
        self.centralframe.setFrameShape(QFrame.Shape.NoFrame)
        self.centralframe.setFrameShadow(QFrame.Shadow.Plain)
        self.gridLayout_2 = QGridLayout(self.centralframe)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)

        self.centralLayout = QSplitter(Qt.Orientation.Horizontal, self.centralframe)
        self.centralLayout.setObjectName(u"centralLayout")
        self.centralLayout.setChildrenCollapsible(True)
        self.centralLayout.setHandleWidth(4)
        self.leftFrame = QFrame(self.centralframe)
        self.leftFrame.setObjectName(u"leftFrame")
        self.leftFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.leftFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.leftFrame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.imageLayout = QVBoxLayout()
        self.imageLayout.setObjectName(u"imageLayout")
        
        #---------------------MENU---------------------
        self.image = QLabel(self.leftFrame)
        self.image.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.image.setObjectName(u"image")
        self.image.setStyleSheet("")
        self.image.setMinimumSize(QSize(300, 200))
        self.image.setMaximumSize(QSize(self.INIT_SIZE_IMG[0], self.INIT_SIZE_IMG[1]))
        self.image.setFont(self.font_global)
        self.imageLayout.addWidget(self.image)
        self.gridLayout_3.addLayout(self.imageLayout, 0, 0, 1, 1)

        aux = QVBoxLayout(self.leftFrame)
        aux.setObjectName(u"aux")
        self.optionsLabel = QLabel(self.leftFrame)
        self.optionsLabel.setObjectName(u"optionsLabel")
        self.optionsLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.optionsLabel.setFont(self.font_global)
        
        self.h_button = QHBoxLayout()
        self.h_button.setObjectName(u"h_button")
        
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        
        font_temp = QFont('Arial', 30)
        self.btnPrev = QPushButton('◀', self.leftFrame)
        self.btnPrev.setObjectName('btnPrev')
        self.btnPrev.setFont(font_temp)
        self.btnPrev.setMinimumSize(QSize(45,45))
        self.btnPrev.clicked.connect(
            self.decrement_page
        )
        self.btnNext = QPushButton('▶', self.leftFrame)
        self.btnNext.setObjectName('btnNext')
        self.btnNext.setFont(font_temp)
        self.btnNext.setMinimumSize(QSize(45,45))
        self.btnNext.clicked.connect(
            self.increment_page
        )
        
        self.actual_page_label = QLabel(self.leftFrame)
        self.actual_page_label.setFont(font)
        self.actual_page_label.setObjectName('actual_page_label')
        self.actual_page_label.setMinimumSize(QSize(45,45))
        self.actual_page_label.setText(str(self.index_page))
        self.actual_page_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.h_button.addWidget(self.btnPrev)
        self.h_button.addWidget(self.actual_page_label)
        self.h_button.addWidget(self.btnNext)
        
        self.button_load = QPushButton(self.leftFrame)
        self.button_load.setMinimumSize(QSize(400, 50))
        self.button_load.setObjectName(u"button_load")
        self.button_load.setFont(font)
        self.button_load.clicked.connect(
            self.sol_load
        )
        
        self.button_save = QPushButton(self.leftFrame)
        self.button_save.setMinimumSize(QSize(400, 50))
        self.button_save.setObjectName(u"button_save")
        self.button_save.setFont(font)
        self.button_save.clicked.connect(
            lambda: self.sol_save(True)
        )
        
        aux.addWidget(self.optionsLabel)
        aux.addWidget(self.button_load)
        aux.addWidget(self.button_save)
        
        self.info_label = QLabel(self.leftFrame)
        self.info_label.setObjectName(u"info_label")
        self.info_label.setAlignment( Qt.AlignmentFlag.AlignHCenter)
        self.info_label.setFont(self.font_global)
        
        politica = self.info_label.sizePolicy()
        politica.setRetainSizeWhenHidden(True)
        self.info_label.setSizePolicy(politica)

        
        self.gridLayout_3.addLayout(aux, 1, 0, 1, 1, Qt.AlignmentFlag.AlignCenter)
        self.gridLayout_3.addLayout(self.h_button, 2, 0, 1, 1, Qt.AlignmentFlag.AlignCenter)
        self.gridLayout_3.addWidget(self.info_label, 3, 0, 1, 1)

        
        self.centralLayout.addWidget(self.leftFrame)

        self.rightFrame = QFrame(self.centralframe)
        self.rightFrame.setObjectName(u"rightFrame")
        self.rightFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.rightFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_4 = QGridLayout(self.rightFrame)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.textData = QPlainTextEdit(self.rightFrame)
        self.textData.setObjectName(u"textData")
        self.textData.setFont(self.font_global)
        self.gridLayout_4.addWidget(self.textData, 1, 0, 1, 1)

        self.labelHeader = QLabel(self.rightFrame)
        self.labelHeader.setObjectName(u"labelHeader")
        
        self.labelHeader.setFont(font)
        self.gridLayout_4.addWidget(self.labelHeader, 0, 0, 1, 1)

        self.centralLayout.addWidget(self.rightFrame)

        self.centralLayout.setStretchFactor(0, 0)
        self.centralLayout.setStretchFactor(1, 1)
        self.centralLayout.setSizes([430, 485])

        self.gridLayout_2.addWidget(self.centralLayout, 0, 0, 1, 1)

        self.gridLayout.addWidget(self.centralframe, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 795, 33))
        self.menubar.setStyleSheet(u"background:rgb(30, 30, 30)")
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        self.menuEdici_n = QMenu(self.menubar)
        self.menuEdici_n.setObjectName(u"menuEdici_n")
        self.menuVer = QMenu(self.menubar)
        self.menuVer.setObjectName(u"menuVer")
        self.menuConfiguraci_n = QMenu(self.menubar)
        self.menuConfiguraci_n.setObjectName(u"menuConfiguraci_n")
        MainWindow.setMenuBar(self.menubar)
        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuEdici_n.menuAction())
        self.menubar.addAction(self.menuVer.menuAction())
        self.menubar.addAction(self.menuConfiguraci_n.menuAction())
        self.menuArchivo.addAction(self.actionNuevo)
        self.menuArchivo.addAction(self.actionAbrir)
        self.menuArchivo.addAction(self.actionGuardar)
        self.menuArchivo.addSeparator()
        self.menuArchivo.addAction(self.actionSalir)
        self.menuEdici_n.addAction(self.actionCortar)
        self.menuEdici_n.addAction(self.actionPegar)
        self.menuEdici_n.addAction(self.actionSeleccionar_Todo)
        self.menuVer.addAction(self.actionVer_foto)
        #self.menuVer.addAction(self.actionMostrar_Ocultar_Panel)
        self.menuVer.addSeparator()
        self.menuVer.addAction(self.actionPantalla_completa)
        self.menuVer.addAction(self.actionMinimizar)
        self.menuConfiguraci_n.addAction(self.actionNombre_de_usuario)
        self.menuConfiguraci_n.addAction(self.actionFoto_de_perfil)
        self.menuConfiguraci_n.addSeparator()
        self.menuConfiguraci_n.addAction(self.actionTema_Claro_Oscuro)
        self.menuConfiguraci_n.addAction(self.actionIdioma)
        self.menuConfiguraci_n.addAction(self.actionBarra)
        self.menuConfiguraci_n.addSeparator()
        self.menuConfiguraci_n.addAction(self.actionColor_de_letra)
        self.menuConfiguraci_n.addAction(self.actionBackground)
        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionNuevo.setText(QCoreApplication.translate("MainWindow", u"Nuevo ", None))
        self.actionAbrir.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
        self.actionGuardar.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.actionSalir.setText(QCoreApplication.translate("MainWindow", u"Salir", None))
        self.actionCortar.setText(QCoreApplication.translate("MainWindow", u"Cortar", None))
        self.actionPegar.setText(QCoreApplication.translate("MainWindow", u"Pegar", None))
        self.actionSeleccionar_Todo.setText(QCoreApplication.translate("MainWindow", u"Seleccionar Todo", None))
        self.actionVer_foto.setText(QCoreApplication.translate("MainWindow", u"Ver foto", None))
        self.actionPantalla_completa.setText(QCoreApplication.translate("MainWindow", u"Pantalla completa", None))
        self.actionMinimizar.setText(QCoreApplication.translate("MainWindow", u"Minimizar", None))
        self.actionNombre_de_usuario.setText(QCoreApplication.translate("MainWindow", u"Nombre de usuario", None))
        self.actionTema_Claro_Oscuro.setText(QCoreApplication.translate("MainWindow", u"Tema (Claro/Oscuro)", None))
        self.actionIdioma.setText(QCoreApplication.translate("MainWindow", u"Idioma (es/es-Es, en/en-US)", None))
        self.actionBarra.setText(QCoreApplication.translate("MainWindow", u"Barra lateral", None))
        self.actionColor_de_letra.setText(QCoreApplication.translate("MainWindow", u"Opciones de letra", None))
        self.actionFoto_de_perfil.setText(QCoreApplication.translate("MainWindow", u"Foto de perfil", None))
        self.actionBackground.setText(QCoreApplication.translate("MainWindow", u"Color de fondo", None))
        #self.actionMostrar_Ocultar_Panel.setText(QCoreApplication.translate("MainWindow", u"Mostrar/Ocultar panel lateral", None))
        #self.image.setText(QCoreApplication.translate("MainWindow", u"Inserta una imagen...", None))
        self.optionsLabel.setText(QCoreApplication.translate("MainWindow", u"Opciones Memorias", None))
        self.info_label.setText(QCoreApplication.translate("MainWindow", u"Sin datos que cargar...", None))
        self.button_load.setText(QCoreApplication.translate("MainWindow", u"Cargar", None))
        self.button_save.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.labelHeader.setText(QCoreApplication.translate("MainWindow", u"MEMORIAS DE: ", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
        self.menuEdici_n.setTitle(QCoreApplication.translate("MainWindow", u"Edici\u00f3n", None))
        self.menuVer.setTitle(QCoreApplication.translate("MainWindow", u"Ver", None))
        self.menuConfiguraci_n.setTitle(QCoreApplication.translate("MainWindow", u"Configuraci\u00f3n", None))
    # retranslateUi

    def closeEvent(self, event):
        print(self.settings)
        event.accept
