import pyautogui
import time
import pandas as pd

def abri_excel():

    print("Abrindo excel...")
    pyautogui.press("win")
    time.sleep(1)

    pyautogui.write("excel")
    time.sleep(1)

    pyautogui.press("enter")
    time.sleep(2)

    pyautogui.press("enter")
    time.sleep(2)

    pyautogui.press("enter")
    time.sleep(1)

def escrever_coluna(valores):
    for valor in valores:
        pyautogui.write(str(valor))
        pyautogui.press("enter")

def escrever_linha(valores):
    for valor in valores:
        pyautogui.write(str(valor))
        pyautogui.press("tab")



def extrair(arquivo):
    try:
        # Leitura de dados da planilha 
        df = pd.read_csv(arquivo , header=0, sep=',', encoding='utf-8')

        df['Total'] = df['Quantidade'] * df['Valor Unitário']
        dados = [df.columns.tolist()] + df.values.tolist()

        return dados

    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")


def fazer_tabela():
    
    print("Desenhando tabela...")

    dados = extrair(r"C:\Users\alisson.rocha\Documents\tabela.csv")

    for linha in dados:
        escrever_linha(linha)
        pyautogui.press("enter")

    

    pyautogui.hotkey("ctrl", "home")
    pyautogui.hotkey("ctrl", "shift", "n")

    pyautogui.hotkey("ctrl", "home")
    pyautogui.press('right')
    pyautogui.press('right')
    pyautogui.hotkey("ctrl", "space")
    pyautogui.hotkey("shift", "f8")
    pyautogui.press('right')
    pyautogui.hotkey("ctrl", "space")
    pyautogui.press('right')
    pyautogui.press('right')
    pyautogui.press('right')
    pyautogui.hotkey("ctrl", "space")
    pyautogui.hotkey("alt", "f1")
    time.sleep(1)
    pyautogui.press('f12')
    pyautogui.write('Relatorio_30-06-2026.xlsx')
    pyautogui.press('enter')
    pyautogui.hotkey("alt", "f4")

abri_excel()
fazer_tabela()
