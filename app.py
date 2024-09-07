import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel, QFileDialog, QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from qrcode_gen import generate_qr_code, validate_url
from datetime import datetime

class QRCodeApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.url_input = QLineEdit(self)
        self.url_input.setPlaceholderText("Enter URL")
        layout.addWidget(self.url_input)

        self.generate_button = QPushButton("Generate QR Code", self)
        self.generate_button.clicked.connect(self.generate_qr_code)
        layout.addWidget(self.generate_button)

        self.qr_image_label = QLabel(self)
        self.qr_image_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.qr_image_label)

        self.save_button = QPushButton("Save QR Code", self)
        self.save_button.clicked.connect(self.save_qr_code)
        layout.addWidget(self.save_button)

        # self.regenerate_button = QPushButton("Regenerate QR Code", self)
        # self.regenerate_button.clicked.connect(self.regenerate_qr_code)
        # layout.addWidget(self.regenerate_button)

        self.setLayout(layout)
        self.setWindowTitle("QR Code Generator")
        self.setGeometry(100, 100, 400, 400)

        self.qr_code_image = None

    def generate_qr_code(self):
        url = self.url_input.text().strip()
        if not validate_url(url):
            self.show_message("Invalid URL", "The URL you entered is not valid.")
            return

        self.qr_code_image = generate_qr_code(url)
        self.display_qr_code_image(self.qr_code_image)
    
    def regenerate_qr_code(self):
        if self.qr_code_image is None:
            self.show_message("No QR Code", "Generate a QR Code first.")
            return

        self.qr_code_image = generate_qr_code(self.url_input.text().strip())
        self.display_qr_code_image(self.qr_code_image)

    def display_qr_code_image(self, img):
        img.save("temp_qr_code.png")
        pixmap = QPixmap("temp_qr_code.png")
        self.qr_image_label.setPixmap(pixmap)
        self.qr_image_label.setScaledContents(True)

    def save_qr_code(self):
        if self.qr_code_image is None:
            self.show_message("No QR Code", "Generate a QR Code first.")
            return
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_path, _ = QFileDialog.getSaveFileName(self, "Save QR Code", f"qrcode_{timestamp}.png", "PNG Files (*.png);;All Files (*)")
        if file_path:
            self.qr_code_image.save(file_path)
            self.show_message("Success", "QR Code saved successfully.")

    def show_message(self, title, message):
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = QRCodeApp()
    ex.show()
    sys.exit(app.exec_())
