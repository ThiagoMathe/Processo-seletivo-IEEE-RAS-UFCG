# Importação das bibliotecas
import cv2 as cv
import numpy as np
import pandas as pd

# Leitura da imagem com a função imread()

imagem = cv.imread('imagem.png')
print('Largura em pixels: ', end='')
print(imagem.shape[1]) #largura da imagem
print('Altura em pixels: ', end='')
print(imagem.shape[0]) #altura da imagem
print('Qtde de canais: ', end='')
print(imagem.shape[2])
# Mostra a imagem com a função imshow
cv.imshow("Nome da janela", imagem)
cv.waitKey(0) #espera pressionar qualquer tecla
# Salvar a imagem no disco com função imwrite()
cv.imwrite("saida.jpg", imagem)
