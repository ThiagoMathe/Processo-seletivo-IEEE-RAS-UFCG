import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)

#configuracao do mediapipe
hands = mp.solutions.hands 
Hands = hands.Hands(max_num_hands=1) #maximo de mão
mpDwaw = mp.solutions.drawing_utils # desenhar ligações da mão

while True:
    success, img = cap.read()
    frameRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB) # convertendo para RGB
    results = Hands.process(frameRGB)
    handPoints = results.multi_hand_landmarks
    h, w, _ = img.shape
    pontos = []# array com todas as coordenadas dos pontos a cada frame
    if handPoints:# cada ponto encontrado da mão
        for points in handPoints:
            mpDwaw.draw_landmarks(img, points,hands.HAND_CONNECTIONS)# desenho de todos os pontos na imagem
            # enumeração de cada ponto da mão com as coordenadas
            for id, cord in enumerate(points.landmark):
                cx, cy = int(cord.x * w), int(cord.y * h)
                pontos.append((cx,cy))

            dedos = [8,12,16,20] # pontos superior de cada dedo exceto o polegar
            contador = 0
            
            if pontos:
                # dedo polegar pegando o eixo se estiver a direita contamos como dedo levantando e assim somados a um contador
                if pontos[4][0] < pontos[3][0]:
                    contador += 1
                # verificar se os pontos superiores sao maiores que os dois pontos abaixo, se tiver ele conta como dedo levantado   
                for x in dedos:
                   if pontos[x][1] < pontos[x-2][1]:
                       contador +=1

            cv2.rectangle(img, (80, 10), (200,110), (255, 0, 0), -1)
            cv2.putText(img,str(contador),(100,100),cv2.FONT_HERSHEY_SIMPLEX,4,(255,255,255),5) # colocando a contagem dentro da tela 
            #print(contador) print para test do contador
    cv2.imshow('Imagem',img)
    cv2.waitKey(1)