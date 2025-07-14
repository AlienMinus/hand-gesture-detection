# 🖐️ Hand Gesture Detection (Both Hands) using OpenCV & MediaPipe

This project is a real-time hand gesture detection system built using **OpenCV** and **MediaPipe**. It can detect gestures made by **both hands** simultaneously and classify them into familiar signs like 👍 Thumbs Up, ✌️ Peace, 🤘 Rock, 🤙 Call Me, Fist, Open Palm, OK Sign, and more.

## 🔍 Features

- Detects and tracks **both hands** in real time via webcam.
- Uses **MediaPipe's Hands module** for landmark detection.
- Classifies gestures based on finger positions:
  - Thumbs Up 👍
  - Peace Sign ✌️
  - Fist ✊
  - Open Palm 🖐️
  - OK Sign 👌
  - Rock Sign 🤘
  - Call Me 🤙
  - Middle Finger 🖕
  - Three, Four, Two finger signs

## 🛠️ Tech Stack

- **Python 3.x**
- [OpenCV](https://opencv.org/)
- [MediaPipe](https://developers.google.com/mediapipe)

## 📁 Project Structure

```bash
hand_gesture_detection/
├── gesture.py   # Main code file
├── README.md    # Project documentation
```

## 🧠 Gesture Logic
The program uses landmark coordinates from MediaPipe's 21 hand landmarks to determine:
- Which fingers are up
- Relative positions of fingertips and pip joints
- Based on conditions, gestures are classified

## 🚀 Getting Started
1. Clone the Repository
```bash
git clone https://github.com/AlienMinus/hand-gesture-detection.git
cd hand-gesture-detection
```
2. Install Dependencies
```bash
pip install opencv-python mediapipe
```
3. Run the Program
```bash
python gesture.py
```

## 🧠 Possible Improvements
- Gesture customization support
- Control computer/media using gestures
- Add gesture-controlled UI navigation
- Multi-language gesture mapping

👨‍💻 Author
Manas Ranjan Das
Electrical & Computer Engineering | AI-ML Enthusiast
🔗 https://www.linkedin.com/in/manas-r-das
📧 dasmanasranjan2005@gmail.com

