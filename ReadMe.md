
Title : 
MedIDS: A lightweight hybrid Machine Learning Intrusion Detection System (IDS) for Internet of Medical Things (IoMT) environments Using Network Traffic Analysis and Malware Image Classification on Raspberry Pi 

Features:
- Real-Time Network Monitoring.
- Image-based malware detection.
- Deployed on Raspberry PI 
- Streamlit User Interface
- Email alert system

What We Used : 
- python 
- streamlit
- Scikit-learn
- TensorFlow / Keras
- Raspberry Pi Zero 2W

Dataset: 
- CICIoMT2024 for Network-based IDS  
- MaleX for Image-based IDS

Machine Learning Models : 
- Decision Tree / Naive Bayes / Logistic Regression for Network-based IDS 
- MobileNetV2 for image-based IDS

Structure : 
MedIDS/
│
├── README.md
├── requirements.txt
├── .gitignore
├── main.py
│
├── models/
│   ├── image_based_model.keras
│   ├── image_based_model.h5
│   ├── ids_image.tflite
│   ├── NetworkIDS3.pkl
│   └── image_based_model.zip
│
├── notebooks/
│   ├── Image_basedIDS.ipynb
│   └── Network_based_IDS.ipynb
│
├── image_ids/
│   ├── __init__.py
│   └── image.py
│
├── network_ids/
│   ├── __init__.py
│   ├── network.py
│   └── email_alert.py
│
├── sample_images/
│   ├── benign.png
│   ├── malware.png
│   └── test.jpeg
│
├── sounds/
│   └── alert.mp3
│
│
└── docs/
    └── report.pdf



Installation:

- Clone Repository

```bash
git clone https://github.com/yourusername/MedIDS.git
cd MedIDS
```
- Install Requirements

```bash
pip install -r requirements.txt
```
- Run Streamlit

```bash
streamlit run streamlit.py
```



Created by:
Alsafa Alwahshi 
CYS student at German University of Technology in Oman 

Supervisor : 
Dr. Raja Waseem Anwar

Contact Information : 
Email: alsafaalwahshi@outlook.com





