#  Rainfall Prediction 🌧️

A professional machine learning project that predicts whether it will rain tomorrow using historical weather metrics. Built with Python, Pandas, and Scikit-Learn using a **Random Forest Classifier**.

---

## 📌 Project Overview

This project implements an end-to-end Binary Classification pipeline. Rather than guessing today's weather, the model analyzes daily meteorological indicators (cloud cover, humidity, pressure, wind speed, etc.) to accurately forecast **`RainTomorrow`**.

## 📊 Key Results & Insights

* **Accuracy:** **100.00%** on test data.
* **Feature Importance:**
  * **Cloud Cover (`Cloud`):** ~49.7% impact
  * **Humidity (`Humidity`):** ~46.4% impact
  * Combined, **Cloud & Humidity** dictate over **96%** of the physical precipitation logic.

---

## 📁 Repository Structure

```text
damas-rainfall-prediction/
│
├── main.py                 # Core Machine Learning Pipeline
├── requirements.txt        # Project Dependencies
├── .gitignore              # Files ignored by Git
└── README.md               # Project Documentation
🛠️ How to Run Locally
1. Clone the repository
Bash
git clone [https://github.com/mhmoud456/damas-rainfall-prediction.git](https://github.com/mhmoud456/damas-rainfall-prediction.git)
cd damas-rainfall-prediction
2. Install dependencies
Bash
pip install -r requirements.txt
3. Run the ML pipeline
Bash
python main.py
👤 Author
Mahmoud Mamo

Electronics & Communications Engineer