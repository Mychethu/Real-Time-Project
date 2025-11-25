# Real Time Sign Language Recognition System

## 🚀 Project Overview  
This project implements a real-time sign language recognition system using Python and computer vision. The system captures input via webcam, preprocesses hand gestures, and uses a trained model to recognize sign language symbols and translate them into text.  


## 🧩 Features  
- Real-time capture of hand gestures via webcam  
- Pre-processing of gesture images for clarity and consistency  
- Deep-learning model trained for sign language recognition  
- Text output translation of recognized gestures  
- Login/signup modules for user management (if applicable)  
- Modular code structure: data collection → training → inference  


## 🛠️ Tech Stack  
- **Language**: Python  
- **Libraries & Frameworks**: OpenCV, TensorFlow/Keras, NumPy, pandas  
- **Model**: .h5 model file included (trained on custom dataset)  
- **Additional Tools**: package.json + package-lock.json (for any JS tools used)  

## 📂 Repository Structure  
Real-Time-Project
│
├─ datacollection.py # Script to collect hand gesture images
├─ train_model.h5 # Trained model file
├─ final.py # Inference script for real-time recognition
├─ login_page.py # User login module
├─ signup_page.py # User signup module
├─ home.py / home1.py # Main UI modules
├─ test.py # Test script
├─ labels1.txt # Label definitions for gestures
├─ package.json # Project dependencies (if using JS)
├─ package-lock.json
└─ pycache/ # Python cache folder
## 📌 Setup Instructions  
1. Clone the repository:  
   ```bash
   git clone https://github.com/Mychethu/Real-Time-Project.git
   cd Real-Time-Project

##📋 Future Improvements

*Expand dataset for more gesture classes
*Improve model accuracy and speed (e.g., using MobileNet)
*Integrate speech synthesis (convert recognized text into voice)
*Add GUI web interface or mobile app
*Add logging and user-profiles to track usage
