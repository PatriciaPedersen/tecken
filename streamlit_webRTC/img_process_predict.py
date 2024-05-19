import cv2
import mediapipe as mp
import numpy as np 

def img_live(hand_img):
    # Bildbehandling
    # 1. Konvertera BGR till RGB
    img_rgb = cv2.cvtColor(hand_img, cv2.COLOR_BGR2RGB)

    # 2. Spegelvänd bilden längs Y-axeln
    img_flip = cv2.flip(img_rgb, 1)

    # Använd MediaPipe-lösningar
    mp_hands = mp.solutions.hands

    # Initiera Hands
    hands = mp_hands.Hands(static_image_mode=True,
    max_num_hands=1, min_detection_confidence=0.7)

    # Resultat
    output = hands.process(img_flip)

    hands.close()

    try:
        data = output.multi_hand_landmarks[0]
        print(data)

        data = str(data)

        data = data.strip().split('\n')

        delete = ['landmark {', '}']

        keep = []

        for i in data:
            if i not in delete:
                keep.append(i)

        clean = []

        for i in keep:
            i = i.strip()
            clean.append(i[2:])

        for i in range(0, len(clean)):
            clean[i] = float(clean[i])

        return(clean)

    except:
        return(np.zeros([1,63], dtype=int)[0])

if __name__ == "__main__":
    img_live()
