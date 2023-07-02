import os

from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas


class MyPDF:
    def __init__(self, name, birthday, language, gender):
        self.name = name
        self.birthday = birthday
        self.language = language
        self.gender = gender
        self.width, self.height = 559, 512

        def create_folder(folder_path):
            try:
                os.makedirs(folder_path)
                print(f"Folder '{folder_path}' created successfully.")
            except FileExistsError:
                print(f"Folder '{folder_path}' already exists.")

        # Создаем новый PDF-файл
        width, height = 559, 512
        custom_page_size = (width * mm, height * mm)
        height_text = 15.8 * mm  # Смотри в canva
        name = "ві"
        birthday = "ва"

        # Пример использования
        folder_path = f"./static/result/{self.name}_{self.birthday}"
        create_folder(folder_path)

        self.pdf = canvas.Canvas(f"{folder_path}/{self.name}_{self.birthday}.pdf", pagesize=custom_page_size)

        # Загрузка нового шрифта
        pdfmetrics.registerFont(TTFont('Klein-Medium', './jpeg/font/Klein-Medium.ttf'))

        # Установка нового шрифта
        self.pdf.setFont("Klein-Medium", 18 * mm)

        # Вставка картинки на страницу
        if self.language == "RUS" and self.gender == "Woman":
            image_path = "./jpeg/template/Шаблон RUS.png"
        elif self.language == "UKR" and self.gender == "Woman":
            image_path = "./jpeg/template/Шаблон UKR.png"
        elif self.language == "RUS" and self.gender == "Man":
            image_path = "./jpeg/template/Шаблон UKR man.png"
        elif self.language == "UKR" and self.gender == "Man":
            image_path = "./jpeg/template/Шаблон UKR man.png"

        self.pdf.drawImage(image_path, x=0, y=0, width=width * mm, height=height * mm)
