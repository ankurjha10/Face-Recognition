# 🧠 Face Recognition System using Python & OpenCV

A real-time Face Recognition project built using **Python**, **OpenCV**, **NumPy**, and **Pillow**. The system captures face images, trains a recognizer model, and performs face detection using your webcam.

---

## 📁 Project Structure

```
Face-Recognition/
├── dataset/                  # Stores captured face images (auto-generated)
├── trainer/                  # Contains trained model (trainer.yml)
├── haarcascade/              # Haarcascade XML for face detection
├── dataset_creater.py        # Captures face images and stores with user info
├── trainer.py                # Trains the face recognizer model
├── detect.py                 # Detects and recognizes faces in real-time
└── README.md                 # Project documentation
```

---

## ⚙️ Requirements

Install the required dependencies using pip:

```bash
pip install opencv-contrib-python numpy Pillow
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/ankurjha10/Face-Recognition.git
cd Face-Recognition
```

---

### 2. Run the Scripts

#### ✅ Step 1: Capture Dataset

Use this script to capture face images and save them with ID, Name, and Age.

```bash
python dataset_creater.py
```

- You will be prompted to enter:
  - User ID (numeric)
  - Name
  - Age
- Captured images will be saved in the `dataset/` folder as `User.<ID>.<count>.jpg`.

---

#### ✅ Step 2: Train the Recognizer

Train the model using the collected face images:

```bash
python trainer.py
```

- This will generate `trainer.yml` inside the `trainer/` directory.
- It uses the **LBPH (Local Binary Patterns Histograms)** recognizer from OpenCV.

---

#### ✅ Step 3: Face Detection & Recognition

Run real-time face recognition using webcam:

```bash
python detect.py
```

- The script detects and recognizes faces using the trained model.
- Recognized user’s name and other info will be displayed on screen.

---

## 📌 Notes

- `dataset/` and `trainer/` folders are auto-created. If they’re not visible on GitHub, add an empty `.gitkeep` file inside each.
- Make sure the Haarcascade file `haarcascade_frontalface_default.xml` is present inside the `haarcascade/` folder.
- You can register multiple users by running `dataset_creater.py` again with different user details.

---

