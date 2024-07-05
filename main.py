import pyqrcode
import customtkinter as ctk
from PIL import Image

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

App = ctk.CTk()
App.geometry("+700+350")
App.title("QR Code Generator")


def generate_qr_code(text, file_name):
    # Создаём объект QRCode
    qr = pyqrcode.create(text)
    # Рисуем QR-код
    qr.png(file_name, scale=6)
    # Открываем изображение в программе
    img = ctk.CTkImage(Image.open(file_name), size=(250, 250))
    qr_Label.configure(text="", image=img)


img_code = ctk.CTkImage(Image.open("images/qr-code.jpg"), size=(250, 250))
qr_Label = ctk.CTkLabel(App, text="", image=img_code)
qr_Label.pack(padx=10, pady=10, fill="both", expand=True)

text_input = ctk.CTkEntry(App, placeholder_text="Enter text or URL", width=250, height=35)
text_input.pack(padx=10,  anchor="w", fill="both")

generate_button = ctk.CTkButton(App, text="Generate QR Code", width=250, height=35,
                                command=lambda: generate_qr_code(text_input.get(), "images/qr_code.png"))
generate_button.pack(pady=10, padx=10, anchor="w", fill="both")

if __name__ == "__main__":
    App.mainloop()
