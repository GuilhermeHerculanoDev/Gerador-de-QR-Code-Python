import io
import os
from tkinter import filedialog

class Controller:
    def __init__(self, view, model):
        self.view = view
        self.model = model

        self.view.button.configure(command = self.generate_qrcode)


    def generate_qrcode(self):
        self.view.root.geometry("400x430")
        self.url = self.view.entry.get()
        self.image_qrcode = self.model.generate_qrcode(self.url)

        img_byte_arr = io.BytesIO()
        self.image_qrcode.save(img_byte_arr, format='PNG')
        img_byte_arr.seek(0)

        self.view.colocar_image(self, img_byte_arr)

    
    def dowload(self, qr):
        self.view.screen_dowload(self, qr)


    def save(self, qr):
        name = self.view.entry_name.get()
        caminho_pasta = filedialog.askdirectory()

        if caminho_pasta:
            if caminho_pasta:
                caminho_arquivo = os.path.join(caminho_pasta, f'{name}.png')
                
                if os.path.isfile(caminho_arquivo):
                    return self.view.messager_box()
                
                qr.save(caminho_arquivo)
        
        again = self.view.generate_again()
        if again == "Sim":
            self.view.root.deiconify()
        else:
            self.view.root.destroy()
            self.view.screen.destroy