import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QDialog, QVBoxLayout, QHBoxLayout, 
    QLabel, QTextEdit, QComboBox, QSpinBox, QPushButton, 
    QColorDialog, QFormLayout, QMessageBox
)
from PySide6.QtGui import QColor, QFont


class DialogoFormularioBase(QDialog):
    def __init__(self, titulo: str, parent=None):
        super().__init__(parent)
        self.setWindowTitle(titulo)
        self.setMinimumWidth(320)
        
        self.layout_principal = QVBoxLayout(self)

        self.layout_contenido = QVBoxLayout()
        self.layout_principal.addLayout(self.layout_contenido)

        layout_botones = QHBoxLayout()
        self.btn_cancelar = QPushButton("Cancelar", self)
        self.btn_agregar = QPushButton("Agregar", self)

        self.btn_cancelar.clicked.connect(self.reject)
        self.btn_agregar.clicked.connect(self.accept)

        
        layout_botones.addWidget(self.btn_agregar)
        layout_botones.addWidget(self.btn_cancelar)
        self.btn_agregar.setFocus()
        self.layout_principal.addLayout(layout_botones)


class FormularioUsuario(DialogoFormularioBase):
    def __init__(self, parent=None, user_name=""):
        super().__init__("Nombre de usuario", parent)

        self.label = QLabel("Ingresa el nombre de usuario:", self)
        self.txt_usuario = QTextEdit(self)
        self.txt_usuario.setText(user_name)
        self.txt_usuario.setMaximumHeight(30)
        #self.txt_usuario.setMaximumHeight(80) 

        self.layout_contenido.addWidget(self.label)
        self.layout_contenido.addWidget(self.txt_usuario)

    def obtener_resultado(s) -> str:
        """Retorna el texto ingresado como string."""
        return s.txt_usuario.toPlainText().strip()


class FormularioTema(DialogoFormularioBase):
    def __init__(self, parent=None, actual = 0):
        super().__init__("Seleccionar Tema", parent)

        self.combo_tema = QComboBox(self)
        # Índice 0 = Oscuro, Índice 1 = Claro
        self.combo_tema.addItem("Oscuro")
        self.combo_tema.addItem("Claro")
        
        self.combo_tema.setCurrentIndex(actual)

        self.layout_contenido.addWidget(QLabel("Tema de la interfaz:", self))
        self.layout_contenido.addWidget(self.combo_tema)

    def obtener_resultado(self) -> int:
        """Retorna 0 si es Oscuro, 1 si es Claro."""
        return self.combo_tema.currentIndex()


class FormularioLenguaje(DialogoFormularioBase):
    def __init__(self, parent=None, actual=0):
        super().__init__("Seleccionar Lenguaje", parent)

        self.combo_lenguaje = QComboBox(self)
        self.combo_lenguaje.addItem("Español (es)", userData="es")
        self.combo_lenguaje.addItem("English (en)", userData="en")

        
        self.combo_lenguaje.setCurrentIndex(actual)

        self.layout_contenido.addWidget(QLabel("Lenguaje:", self))
        self.layout_contenido.addWidget(self.combo_lenguaje)

    def obtener_resultado(self) -> str:
        """Retorna el código de lenguaje seleccionado ('es' o 'en')."""
        return self.combo_lenguaje.currentData()


class FormularioFuente(DialogoFormularioBase):
    def __init__(self, parent=None, size=15, color='#000000'):
        super().__init__("Configuración de Fuente", parent)
        self.color_seleccionado = QColor(color)

        self.spin_tamano = QSpinBox(self)
        self.spin_tamano.setRange(6, 72)
        self.spin_tamano.setValue(size)
        txt = QLabel()
        txt.setText("Tamaño entre 6 y 72 pt")
        txt.setStyleSheet(f"color: {"#8C8999"}")
        txt.setFont(QFont("Arial", 8))

        self.btn_color = QPushButton("Elegir nuevo color", self)
        self.btn_color.clicked.connect(self._seleccionar_color)
        self._actualizar_estilo_boton_color()

        form_layout = QFormLayout()
        form_layout.addRow("Tamaño:", self.spin_tamano)
        form_layout.addWidget(txt)
        form_layout.addRow("Color:", self.btn_color)
        
        self.layout_contenido.addLayout(form_layout)

    def _seleccionar_color(self):
        color = QColorDialog.getColor(self.color_seleccionado, self, "Selecciona el color de la fuente")
        if color.isValid():
            self.color_seleccionado = color
            self._actualizar_estilo_boton_color()

    def _actualizar_estilo_boton_color(self):
        hex_color = self.color_seleccionado.name()
        self.btn_color.setStyleSheet(f"background-color: {hex_color}; color: {'white' if self.color_seleccionado.lightness() < 128 else 'black'};")

    def obtener_resultado(self) -> dict:
        return {
            "tamano": self.spin_tamano.value(),
            "color_hex": self.color_seleccionado.name(),
            "color_qcolor": self.color_seleccionado
        }


class FormularioFondo(DialogoFormularioBase):
    hex_color = ''
    def __init__(self, parent=None, color='#000000'):
        super().__init__("Configuración de Fuente", parent)
        self.color_seleccionado = QColor(color)
        self.hex_color = color
        self.btn_color = QPushButton("Elegir nuevo color", self)
        self.btn_color.clicked.connect(self._seleccionar_color)
        self._actualizar_estilo_boton_color()

        form_layout = QFormLayout()
        form_layout.addRow("Color:", self.btn_color)
        
        v = QHBoxLayout()
        v.setContentsMargins(0,0,0, 20)
        self.btn_light = QPushButton("Fondo Claro", self)
        self.btn_light.clicked.connect(
            lambda: self._actualizar_( '#F5F5F5')
        )
        self.btn_light.setStyleSheet(self.btn_light.styleSheet() + """
        background-color: #F5F5F5;
        color: black; 
        """)
        
        self.btn_black =  QPushButton("Fondo Oscuro", self)
        self.btn_black.setStyleSheet(self.btn_black.styleSheet() + """
        background-color: #1F1F1F;
        color: white;
        """)
        self.btn_black.clicked.connect(
                    lambda: self._actualizar_( '#1F1F1F')
        )
        
        v.addWidget(self.btn_light)
        v.addWidget(self.btn_black)
        
        self.layout_contenido.addLayout(form_layout)
        self.layout_contenido.addLayout(v)

    def _seleccionar_color(self):
        color = QColorDialog.getColor(self.color_seleccionado, self, "Selecciona el color de la fuente")
        if color.isValid():
            self.color_seleccionado = color
            self._actualizar_estilo_boton_color()
            #QMessageBox.information(self, 'Color de fondo', 'El color de fondo fue agregado con exito!')


    def _actualizar_estilo_boton_color(self):
        self.hex_color = self.color_seleccionado.name()
        self.btn_color.setStyleSheet(f"background-color: {self.hex_color}; color: {'white' if self.color_seleccionado.lightness() < 128 else 'black'};")

    def _actualizar_(self, color):
        self.hex_color = color
        if color == '#1F1F1F':
            self.btn_color.setStyleSheet(f"background-color: {self.hex_color}; color: white;")
        else:
            self.btn_color.setStyleSheet(f"background-color: {self.hex_color}; color: black;")
        #QMessageBox.information(self, 'Color de fondo', 'El color de fondo fue agregado con exito!')

    def obtener_resultado(self) -> dict:
        return {
            "color_hex": self.hex_color,
            "color_qcolor": self.color_seleccionado
        }
