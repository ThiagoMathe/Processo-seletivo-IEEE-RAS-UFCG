import cv2
imagem = cv2.imread('Ponte.jpg')
for y in range(0, imagem.shape[0]):
 for x in range(0, imagem.shape[1]):
     imagem[y, x] = (255,0,0)
cv2.imshow("Imagem modificada", imagem)
cv2.waitKey(0)
