from customtkinter import *
from CTkMessagebox import CTkMessagebox
from PIL import Image

class View:
    def __init__(self, root):
        self.root = root

        self.root.title("Gerador de QR Code")
        self.root.geometry("400x180")

        self.label = CTkLabel(self.root, text = 'Gerador de QR Code', font = ('Arial', 20))
        self.label.pack(padx = 10, pady = 10)

        self.entry = CTkEntry(self.root, placeholder_text = 'Digite a sua URL:')
        self.entry.pack(padx = 10, pady = 10) 

        self.button = CTkButton(self.root, text = 'Gerar')
        self.button.pack(padx = 10, pady = 10)


    def colocar_image(self, controller, image_path):
        pil_image = Image.open(image_path)

        ctk_image = CTkImage(pil_image, size=(200,200))
        self.label_image = CTkLabel(self.root, image = ctk_image, text = '')
        self.label_image.pack(padx = 10, pady = 10)

        self.button_dowload = CTkButton(self.root, text = 'Dowload', command = lambda: controller.dowload(pil_image))
        self.button_dowload.pack(padx = 10, pady = 10)


    def screen_dowload(self, controller, qr):
        self.root.withdraw()

        self.screen = CTkToplevel()
        self.screen.title('Tela Dowload')
        self.screen.geometry("300x170")

        self.screen.protocol("WM_DELETE_WINDOW", self.close)

        self.label_dowload = CTkLabel(self.screen, text = 'Digite o nome do arquivo', font = ('Arial', 20))
        self.label_dowload.pack(padx = 10, pady = 10)

        self.entry_name = CTkEntry(self.screen, placeholder_text = 'Nome do arquivo:')
        self.entry_name.pack(padx = 10, pady = 10)

        self.button_save = CTkButton(self.screen, text = 'Salvar', command = lambda: controller.save(qr))
        self.button_save.pack(padx = 10, pady = 10)

        self.screen.mainloop()


    def messager_box(self):
        CTkMessagebox(title = 'Erro', message =  'Já existe um arquivo com esse nome', icon = 'cancel')


    def generate_again(self):
        again = CTkMessagebox(title = "Novamente", message="Deseja gerar outro qrcode?",
                        icon="question", option_1="Não", option_2="Sim")
        return again
    

    def close(self):
        self.root.destroy()