import joblib
import pandas as pd
import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(
    page_title="Damascus Rainfall Prediction",
    page_icon="🌧️",
    layout="centered",
)

# 2. عنوان التطبيق والمقدمة
st.title("🌧️ Damascus Rainfall Prediction System")
st.markdown(
    "Welcome! This interactive web app uses a trained **Random Forest Machine"
    " Learning Model** to forecast whether it will rain tomorrow in Damascus"
    " based on today's weather indicators."
)
st.divider()


# 3. تحميل النموذج المحفوظ
@st.cache_resource
def load_model():
  try:
    return joblib.load("rain_model.pkl")
  except FileNotFoundError:
    return None


model = load_model()

if model is None:
  st.error(
      "❌ Model file 'rain_model.pkl' not found! Please run 'train.py' first."
  )
  st.stop()

# 4. تصميم واجهة إدخال البيانات (Inputs)
st.header("📊 Enter Today's Meteorological Data")

col1, col2 = st.columns(2)

with col1:
  min_temp = st.number_input(
      "Minimum Temperature (°C)", value=15.2, step=0.1
  )
  max_temp = st.number_input(
      "Maximum Temperature (°C)", value=28.5, step=0.1
  )
  rainfall = st.number_input("Current Rainfall (mm)", value=0.0, step=0.1)
  humidity = st.slider("Humidity (%)", min_value=0, max_value=100, value=65)

with col2:
  pressure = st.number_input(
      "Atmospheric Pressure (hPa)", value=1012.0, step=0.5
  )
  wind_speed = st.number_input("Wind Speed (km/h)", value=10.5, step=0.5)
  wind_gust = st.number_input("Wind Gust Speed (km/h)", value=22.0, step=0.5)
  cloud = st.slider("Cloud Cover (Okta: 0-8)", min_value=0, max_value=8, value=2)

st.divider()

# 5. زر التنبؤ وتصميم النتيجة (Prediction)
if st.button("🔮 Predict Tomorrow's Weather", type="primary", use_container_width=True):
  # ترتيب الأعمدة المعتمد عند تدريب النموذج
  features = [
      "MinTemp",
      "MaxTemp",
      "Rainfall",
      "Humidity",
      "Pressure",
      "WindSpeed",
      "WindGustSpeed",
      "Cloud",
  ]
  input_data = pd.DataFrame(
      [[
          min_temp,
          max_temp,
          rainfall,
          humidity,
          pressure,
          wind_speed,
          wind_gust,
          cloud,
      ]],
      columns=features,
  )

  # إجراء التنبؤ وحساب الاحتمالية
  prediction = model.predict(input_data)[0]
  probabilities = model.predict_proba(input_data)[0]
  confidence = max(probabilities) * 100

  st.subheader("🎯 Prediction Result:")

  if prediction == 1:
    st.error(f"🌧️ **YES, it is likely to rain tomorrow!**")
    st.info(f"💡 Model Confidence: **{confidence:.2f}%**")
  else:
    st.success(f"☀️ **NO, it will not rain tomorrow.**")
    st.info(f"💡 Model Confidence: **{confidence:.2f}%**")