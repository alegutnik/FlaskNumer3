from pdf2image import convert_from_path
from reportlab.lib import colors
from reportlab.lib.units import mm

from jpeg.client import Client
from jpeg.settings_page import MyPDF


class Card:
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday

        def sum_value(value):
            while value >= 10 and value != 11:
                value -= 9
            return value

        def coordinates(rows, columns):
            width, height = 559, 512
            x = width_cell / 2 + (width_cell + 3) * (rows - 1)
            if rows > 3:
                x += 25
            y = height - (100 + 3) * (columns - 1) - 40 - 25
            return (x * mm, y * mm)

        # INPUT
        width_cell, height_cell = 125, 100
        count = 1

        # Создаем клиента
        client = Client(self.name, self.birthday)

        # Задаем цвет в формате HEX
        text_color_blue = colors.HexColor("#091A4C")  # Синий
        text_color_white = colors.HexColor("#FFFFFF")  # Синий

        # -------------------------------------
        pdf = MyPDF(self.name, self.birthday)
        # Устанавливаем цвет текста
        pdf.pdf.setFillColor(text_color_blue)

        # Координаты основных чисел
        coordinats_general_numbers = {"Характер": coordinates(1, 2),
                                      "Енергия": coordinates(1, 3),
                                      "Интерес": coordinates(1, 4),
                                      "Здоровье": coordinates(2, 2),
                                      "Логика": coordinates(2, 3),
                                      "Труд": coordinates(2, 4),
                                      "Удача": coordinates(3, 2),
                                      "Долг": coordinates(3, 3),
                                      "Память": coordinates(3, 4)}

        # Вставка основных показателей
        for key, value in coordinats_general_numbers.items():
            pdf.pdf.drawCentredString(*coordinats_general_numbers.get(key),
                                  str(count) * client.general_numbers.get(key) if client.general_numbers.get(
                                      key) != 0 else "-")
            count += 1

        # -------------------------------------

        # Устанавливаем цвет текста
        pdf.pdf.setFillColor(text_color_white)

        # Координаты дополнительных показательей
        coordinats_second_numbers = {"Быт": coordinates(2, 5),
                                     "Темперамент": coordinates(4, 1),
                                     "Цель": coordinates(4, 2),
                                     "Семья": coordinates(4, 3),
                                     "Привычки": coordinates(4, 4)}

        # Вставка дополнительных показателей
        for key, value in coordinats_second_numbers.items():
            pdf.pdf.drawCentredString(*coordinats_second_numbers.get(key),
                                  str(client.second_general_numbers.get(key)) if
                                  client.second_general_numbers.get(key) != 0 else "-")

        pdf.pdf.drawCentredString(*coordinates(3, 1), str(sum_value(client.additional_number_2())))

        # Вставка заголовка на страницу
        pdf.pdf.drawCentredString((width_cell + 1.5) * mm, (pdf.height - height_cell * 0.6 - 5) * mm, self.birthday)
        pdf.pdf.setFont("Klein-Medium", 16 * mm)
        pdf.pdf.drawCentredString((width_cell + 1.5) * mm, (pdf.height - height_cell * 0.3 - 5) * mm, name.upper())

        # -------------------------------------

        pdf.pdf.save()
        path = f"static/result/{self.name}_{self.birthday}/{self.name}_{self.birthday}"
        images = convert_from_path(f"{path}.pdf", 400)

        images[0].save(f"{path}.jpeg", "JPEG")

        # os.startfile(f"{path}.jpeg".replace("/", "\\"))
