A professional end-to-end Machine Learning web application built to predict whether it will rain tomorrow in Damascus based on daily meteorological indicators. The project follows industry best practices by decoupling model training from real-time inference and providing an interactive modern web interface.

---

## 📌 Project Architecture & Workflow

1. **Model Training (`train.py`):** 
   * Processes the historical weather dataset.
   * Trains a robust **Random Forest Classifier** and evaluates its performance.
   * Serializes and saves the trained model into a production-ready file (`rain_model.pkl`).
2. **Web Application (`app.py`):** 
   * An interactive, modern UI built using **Streamlit**.
   * Loads the pre-trained model instantly, accepts live meteorological inputs via sliders and number inputs, and forecasts tomorrow's precipitation with confidence probabilities.

---

## 📊 Key Insights & Performance

* **Accuracy:** **100.00%** on the test dataset.
* **Feature Importance Analysis:** 
  * **Cloud Cover (`Cloud`):** ~49.7% impact
  * **Humidity (`Humidity`):** ~46.4% impact
  * Together, Cloud Cover and Humidity govern over **96%** of the prediction logic.

---

## 📁 Repository File Structure

```text
Rainfall_predict/
│
├── weather_based_rain_prediction_dataset.csv # Historical weather dataset
├── train.py                # Training pipeline & model serialization
├── app.py                  # Interactive Streamlit Web UI
├── rain_model.pkl          # Serialized trained Random Forest model
├── requirements.txt        # Project dependencies
├── .gitignore              # Ignored temporary files
└── README.md               # Project documentation
🚀 How to Run Locally
1. Clone the repository
Bash
git clone [https://github.com/mhmoud456/Rainfall_predict.git](https://github.com/mhmoud456/Rainfall_predict.git)
cd Rainfall_predict
2. Install dependencies
Bash
pip install -r requirements.txt
3. Train the model (Optional / Generates rain_model.pkl)
Bash
python train.py
4. Run the Streamlit Web Application
Bash
python -m streamlit run app.py
👤 Author
Mahmoud Mamo

Electronics & Communications Engineer