import numpy as np
import cv2 as cv
from pathlib import Path

def create_data():
    sign = input('Vilket tecken vill du lägga till? -> ')
    Path('dataset/' + sign).mkdir(parents=True, exist_ok=True)  # Skapar en mapp för tecknet
    cap = cv.VideoCapture(0)  # Startar webbkameran
    i = 0    
    while True:
        ret, frame = cap.read()
        i += 1
        if i % 5 == 0:
            cv.imwrite(f'dataset/{sign}/{str(i)}.png', frame)  # Sparar var femte bild
        cv.imshow('frame', frame)  # Visar den nuvarande bilden
        if cv.waitKey(1) == ord('q') or i >= 500:  # Avbryter om användaren trycker på 'q'  eller om 500 bilder har sparats
            break
    cap.release()  # Stänger ned webbkameran
    cv.destroyAllWindows()  # Stänger alla fönster

if __name__ == "__main__":
    create_data()

