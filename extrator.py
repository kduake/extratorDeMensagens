import time
import threading
from tkinter import *
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

root = Tk()


class Functions:
    def extrair(self):
        browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self.options)
        time.sleep(3)
        browser.get("https://t.me/Area52ofc")

        while len(browser.find_elements(By.XPATH, '/html/body/div[2]/div[2]/div/div[6]/a/span')) < 1:
            time.sleep(2)
        browser.execute_script('document.querySelector("body > div.tgme_page_wrap > div.tgme_body_wrap > div > '
                               'div.tgme_page_action.tgme_page_web_action > a").click()')
        lista_mensagens = []
        while True:
            time.sleep(1)
            if len(browser.find_elements(By.XPATH,
                                         '//*[@id="MiddleColumn"]/div[3]/div[1]/div[3]/div')) >= 1:
                time.sleep(1)
                browser.get('https://web.telegram.org/k/#-1527158327')
                time.sleep(2)
            elif len(browser.find_elements(By.XPATH,
                                           '//*[@id="column-center"]/div/div/div[2]/div[1]/div[2]/button[6]')) >= 1:
                time.sleep(2)
                browser.execute_script('document.querySelector("#column-center > div > div > div.chat-input > div > '
                                       'button.btn-circle.btn-corner.z-depth-1.bubbles-corner-button.bubbles-go-down'
                                       '.tgico-arrow_down.rp").click()')
                time.sleep(1)
                break

        self.entry_rolagem = self.entry_variavel.get()
        for i in range(int(self.entry_rolagem)):
            flag = browser.find_element(by=By.XPATH, value='//*[@id="column-center"]/div/div/div[3]/div/div')
            browser.execute_script("arguments[0].scrollIntoView();", flag)
            time.sleep(0.3)

            retorno = browser.execute_script(
                'const nodeList = document.querySelectorAll(".message"); const conversa = []; for (let i = 0; i < '
                'nodeList.length; i++) { conversa.push(nodeList[i].innerText.split(`\n`).join("$").split("2").join("$")'
                '.split("1").join("$").split("0").join("$").split("$")[0])}; return conversa')
            for x in retorno:
                lista_mensagens.append(x)
            i += 1

        arquivoMensagens = pd.DataFrame(lista_mensagens, columns=['Mensagens'])
        arquivoMensagens.to_csv('mensagens.csv', index=False)

        # "Apagar linhas vazias"
        arquivoler = pd.read_csv("mensagens.csv").dropna()
        arquivoler.to_csv('mensagens.csv', index=False)

        # "Apagar linhas duplicadas"
        arquivoler2 = pd.read_csv("mensagens.csv").drop_duplicates()
        arquivoler2.to_csv('mensagens.csv', index=False)

        self.root.destroy


class Application(Functions):
    def __init__(self):
        # configuração do WebDriver(Navegador)
        self.options = webdriver.ChromeOptions()
        self.options.add_argument(
            f'--user-data-dir=/profile')

        # Funções que começaram sendo inicializadas
        self.root = root
        self.tela()
        self.frames()
        root.mainloop()

    def tela(self):
        self.root.title("Extrator de mensagens")
        self.root.configure(bg='#5e4d85')
        self.root.geometry("300x200")
        self.root.resizable(False, False)

    def frames(self):
        self.label_frame = LabelFrame(self.root,
                                      bg="#5e4d85",
                                      text="Quantas rolagens o programa executará?",
                                      fg="pink",
                                      font="arial 9")
        self.label_frame.pack()

        self.entry_variavel = Entry(self.label_frame)
        self.entry_variavel.pack(pady=10)

        self.botao_variavel = Button(self.root,
                                     bg="#007FFF",
                                     width=15,
                                     text="Executar programa",
                                     command=self.extrair)
        self.botao_variavel.pack(pady=50)


Application()
