import time
from processamento_imagem import obter_contornos
from artista import desenhar_contorno, abrir_paint

abrir_paint()

print("Começando em 3 segundos...")
time.sleep(3)

contornos = obter_contornos(
    "imagens/teste.png"
)

for contorno in contornos:

    if len(contorno) > 5:
        desenhar_contorno(contorno)

print("Finalizado!")