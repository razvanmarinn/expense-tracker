"""Avatar handling for user profile"""
import psycopg2
from PyQt6.QtWidgets import QFileDialog
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt, QByteArray, QBuffer


class AvatarHandler():  # too be modified into API call
    """Avatar handler"""
    def __init__(self, main_window):
        self.conn = psycopg2.connect(database="expense-tracker", user='postgres', password='raz', host='127.0.0.1', port='5432')
        self.cursor = self.conn.cursor()
        self.main_window = main_window

    def open_avatar(self):
        """Open avatar from file"""
        fname = QFileDialog.getOpenFileName(self.main_window.parent, 'Open file', 'c:\\', "Image files (*.jpg *.gif)")
        if fname[0]:

            pixmap = QPixmap(fname[0]).scaled(self.main_window.l_photo.width(), self.main_window.l_photo.height(), Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
            self.main_window.l_photo.setPixmap(pixmap)
            AvatarHandler.save_avatar_to_database(self, pixmap)

    def save_avatar_to_database(self, pixmap):
        """Save avatar to database"""
        byte_array = QByteArray()
        buffer = QBuffer(byte_array)
        buffer.open(QBuffer.OpenModeFlag.WriteOnly)
        pixmap.save(buffer, 'PNG')

        data = byte_array.toBase64().data().decode()
        self.cursor.execute("DELETE FROM user_avatar WHERE user_id = %s", (self.main_window.parent.user.id,))
        self.cursor.execute("INSERT INTO user_avatar (user_id, filename, avatar) VALUES (%s, %s, %s)", (self.main_window.parent.user.id, 'asd.jpg', data))
        self.conn.commit()

    def get_avatar_from_database(self):
        """Get avatar from database"""
        self.cursor.execute("SELECT avatar FROM user_avatar WHERE user_id = %s", (self.main_window.parent.user.id,))
        avatar = self.cursor.fetchone()
        ba = QByteArray.fromBase64(bytes(avatar[0]))
        if avatar is not None:
            pixmap = QPixmap()
            pixmap.loadFromData(ba)
            self.main_window.l_photo.setPixmap(pixmap)
