# Hand Gesture Detection for Both Hands using OpenCV and Mediapipe

import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

def fingers_up(hand_landmarks):
    tips = [
        mp_hands.HandLandmark.THUMB_TIP,
        mp_hands.HandLandmark.INDEX_FINGER_TIP,
        mp_hands.HandLandmark.MIDDLE_FINGER_TIP,
        mp_hands.HandLandmark.RING_FINGER_TIP,
        mp_hands.HandLandmark.PINKY_TIP
    ]
    pips = [
        mp_hands.HandLandmark.THUMB_IP,
        mp_hands.HandLandmark.INDEX_FINGER_PIP,
        mp_hands.HandLandmark.MIDDLE_FINGER_PIP,
        mp_hands.HandLandmark.RING_FINGER_PIP,
        mp_hands.HandLandmark.PINKY_PIP
    ]
    fingers = []
    for tip, pip in zip(tips, pips):
        if tip == mp_hands.HandLandmark.THUMB_TIP:
            fingers.append(hand_landmarks.landmark[tip].x < hand_landmarks.landmark[pip].x)
        else:
            fingers.append(hand_landmarks.landmark[tip].y < hand_landmarks.landmark[pip].y)
    return fingers  # [thumb, index, middle, ring, pinky]

with mp_hands.Hands(
    max_num_hands=2,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
) as hands:

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb)

        if results.multi_hand_landmarks:
            for idx, hand_landmarks in enumerate(results.multi_hand_landmarks):
                mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                fingers = fingers_up(hand_landmarks)
                gesture = "Unknown"

                if fingers == [True, False, False, False, False]:
                    gesture = "Thumbs Up!"
                elif fingers == [False, True, True, False, False]:
                    gesture = "Peace ✌️"
                elif fingers == [False, False, False, False, False]:
                    gesture = "Fist"
                elif fingers == [True, True, True, True, True]:
                    gesture = "Open Palm"
                elif fingers[0] and fingers[1] and not any(fingers[2:]):
                    gesture = "OK"
                elif fingers == [False, False, True, False, False]:
                    gesture = "Middle Finger"
                elif fingers == [False, True, False, False, True]:
                    gesture = "Rock 🤘"
                elif fingers == [True, False, False, False, True]:
                    gesture = "Call Me 🤙"
                elif fingers == [False, True, True, True, True]:
                    gesture = "Four"
                elif fingers == [False, True, True, True, False]:
                    gesture = "Three"
                elif fingers == [False, True, True, False, False]:
                    gesture = "Two"

                # Show gesture label near each hand
                x0 = int(hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].x * frame.shape[1])
                y0 = int(hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].y * frame.shape[0])
                cv2.putText(frame, f"Hand {idx+1}: {gesture}", (x0, y0 - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,0), 2)

        cv2.imshow("Gesture Detection (Both Hands)", frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break

cap.release()
cv2.destroyAllWindows()
