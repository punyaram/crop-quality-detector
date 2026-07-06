# 🌾 Crop Quality Detector

An AI-powered web application that classifies the quality of agricultural crops into **Grade A**, **Grade B**, or **Grade C** using a deep learning model. Users can upload an image of a crop, and the system predicts both the crop type and its quality grade with a confidence score.

---

## Features

- 📸 Upload crop images for analysis
- 🤖 Deep Learning-based quality prediction
- 🌱 Supports multiple crop types
- 📊 Displays:
  - Crop Name
  - Quality Grade (A/B/C)
  - Prediction Confidence
- 🖥️ User-friendly web interface built with Streamlit
- ⚡ React + Vite frontend

---

## Supported Crops

- 🍎 Apple
- 🌽 Corn
- 🍇 Grape
- 🥔 Potato
- 🍅 Tomato

Each crop is classified into:

- Grade A
- Grade B
- Grade C

Total Classes: **15**

---

## Tech Stack

### Frontend
- React
- Vite
- Tailwind CSS

### Backend
- Python
- Streamlit

### Machine Learning
- TensorFlow
- Keras
- NumPy
- Pillow

---

## Project Structure

```
cropqualitytest/
│
├── app.py
├── README.md
├── .gitignore
│
├── oiyu/                 # React frontend
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── ...
│
├── cropdataset/          # Dataset (ignored)
├── cropdataset.zip       # Dataset archive (ignored)
├── crop_quality_detector_model.keras  # Model (ignored)
└── venv/                 # Virtual environment (ignored)
```

---

## Installation

### Clone the repository

```bash
git clone https://github.com/punyaram/crop-quality-detector.git
cd crop-quality-detector
```

### Create a virtual environment

```bash
python -m venv venv
```

### Activate the virtual environment

**Windows**

```bash
venv\Scripts\activate
```

**Git Bash**

```bash
source venv/Scripts/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

If you don't have a requirements file, install the required packages manually:

```bash
pip install streamlit tensorflow pillow numpy
```

### Start the application

```bash
streamlit run app.py
```

---

## Model File

The trained model file

```
crop_quality_detector_model.keras
```

is **not included** in this repository because GitHub limits normal Git uploads to **100 MB**, while the model is approximately **255 MB**.

To run this project successfully, place the trained model file in the project root directory:

```
cropqualitytest/
│
├── app.py
├── crop_quality_detector_model.keras
└── ...
```

Once the model is available in the project root, the application will automatically load it during startup.

---

## Future Improvements

- Support additional crops
- Crop disease detection
- Mobile-responsive UI
- Live camera prediction
- Cloud deployment
- Prediction history
- Batch image processing

---

## Author

**Punya R**

B.Tech – Computer Science Engineering (AI & ML)

Passionate about Artificial Intelligence, Machine Learning, Computer Vision, and Full Stack Development.

---

## License

This project is intended for educational and research purposes.
