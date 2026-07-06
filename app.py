import streamlit as st
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image
import re

# Load model
model = tf.keras.models.load_model("crop_quality_detector_model.keras", safe_mode=False)

# Class labels
class_labels = [
    "applegradeA", "applegradeB", "applegradeC",
    "corngradeA", "corngradeB", "corngradeC",
    "grapegradeA", "grapegradeB", "grapegradeC",
    "potatogradeA", "potatogradeB", "potatogradeC",
    "tomatogradeA", "tomatogradeB", "tomatogradeC"
]

# App layout
def main():
    # Sidebar
    st.sidebar.title(" About This Project")
    st.sidebar.info(
        "This AI-powered Crop Quality Detector classifies the **grade (A/B/C)** "
        "of 5 major crops based on image quality.\n\n"
        "Supported crops:\n"
        "- 🍎 Apple\n"
        "- 🌽 Corn\n"
        "- 🍇 Grape\n"
        "- 🥔 Potato\n"
        "- 🍅 Tomato\n\n"
        "Upload a crop image to check its grade!"
    )

    # Title
    st.title("🌾 Crop Quality Detector")
    st.markdown(
        """
        ### Welcome!   
        This web app uses a deep learning model trained on thousands of crop images  
        to automatically detect the **quality grade (A, B, or C)** of your crop.  
        Simply upload a clear photo, and let AI do the rest!
        """
    )

    # Upload section
    uploaded_file = st.file_uploader("Upload an image of your crop...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        img = Image.open(uploaded_file).convert("RGB")
        st.image(img, caption="Uploaded Image", use_container_width=True)

        # Preprocess image
        img = img.resize((224, 224))  # must match training input size
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0) / 255.0

        # Predict
        predictions = model.predict(img_array)
        predicted_class = np.argmax(predictions, axis=1)[0]
        confidence = np.max(predictions)

        # Extract label
        predicted_label = class_labels[predicted_class].strip()

        # Split crop and grade intelligently
        match = re.match(r"([a-zA-Z]+)(grade)([a-zA-Z])", predicted_label, re.IGNORECASE)
        if match:
            crop_name = match.group(1).capitalize()
            grade = f"Grade {match.group(3).upper()}"
        else:
            crop_name = predicted_label.capitalize()
            grade = "Unknown"

        # --- Display results beautifully ---
        st.subheader("🔍 Prediction Results")
        st.markdown(f"""
        <div style='
            background-color:#f0f8ff;
            padding:20px;
            border-radius:12px;
            border-left:6px solid #1f77b4;
            font-size:18px;'>
             <h4><span style='color:#2e8b57;'>Crop Detected:</span></h4><span style='color:#8b0000;'>{crop_name}</span><br><br>
             <h4><span style='color:#2e8b57;'>Quality Grade:</span></h4><span style='color:#8b0000;'>{grade}</span><br><br>
             <h4><span style='color:#2e8b57;'>Confidence:</span></h4><span style='color:#8b0000;'>{confidence*100:.2f}%</span>
        </div>
        """, unsafe_allow_html=True)

               # Friendly message
        st.markdown("---")
        st.markdown(
            f"**{crop_name} - {grade}** represents the AI's prediction of this crop’s quality "
            f"based on its color, texture, and overall appearance."
        )

        # Add grade meaning
        st.markdown(
            """
            <div style='
                background-color:#f9fafb;
                border-left:5px solid #10b981;
                padding:10px 15px;
                border-radius:8px;
                font-size:16px;
                color:#111827;
                margin-top:10px;'>
                 <b>Grade meanings:</b><br>
                • <b>Grade A</b> → Premium quality: vibrant color, smooth texture, minimal defects.<br>
                • <b>Grade B</b> → Moderate quality: slight imperfections or discoloration.<br>
                • <b>Grade C</b> → Lower quality: visible defects or inconsistent ripeness.
            </div>
            """,
            unsafe_allow_html=True
        )

    else:
        st.warning("Please upload an image to begin crop quality detection.")

if __name__ == "__main__":
    main()
