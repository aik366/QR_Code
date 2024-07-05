# pip install requirements.txt
import qrcode
import customtkinter as ctk
from PIL import Image

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

App = ctk.CTk()
App.geometry("270x370+700+350")
App.title("QR Code Generator")


def generate_qr_code(text, file_name):
    # Создание объекта QRCode
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)

    # Генерация изображения QR кода
    qr_image = qr.make_image(fill_color="black", back_color="white")

    # Сохранение изображения в файл
    qr_image.save(file_name)
    img = ctk.CTkImage(Image.open(file_name), size=(250, 250))
    qr_Label.configure(text="", image=img)


qr_Label = ctk.CTkLabel(App, text="QR Code Generator", font=("Roboto", 20))
qr_Label.pack(padx=10, pady=10, fill="both", expand=True)

text_input = ctk.CTkEntry(App, placeholder_text="Enter text or URL", height=35)
text_input.pack(padx=10, anchor="w", fill="both")

generate_button = ctk.CTkButton(App, text="Generate QR Code", height=35,
                                command=lambda: generate_qr_code(text_input.get(), "images/qr_code.png"))
generate_button.pack(pady=10, padx=10, anchor="w", fill="both")

if __name__ == "__main__":
    App.mainloop()
