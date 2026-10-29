import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score , classification_report , confusion_matrix
def main():
    print("1-loading data")
    df=pd.read_csv('weather_based_rain_prediction_dataset.csv')
    print(f"dataset shape:{df.shape}\n")
    print("2-preparing features and target")
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
    X = df[features]
    y = df["RainTomorrow"]
    print("3-spliting")
    X_train ,X_test , y_train ,y_test =train_test_split(X,y,test_size=0.2,random_state=42,stratify=y)
    print("4-training RandomForestClassifier")
    clf=RandomForestClassifier(n_estimators=100,random_state=42)
    clf.fit(X_train,y_train)
    print("model training completed succesfully")
    print("5-evaluating model performance")
    y_pred=clf.predict(X_test)
    accuracy=accuracy_score(y_test,y_pred)
    print(f"Accuracy: {accuracy * 100:.2f}%\n")

    print("Classification Report:")
    print(classification_report(y_test, y_pred))

    print("Confusion Matrix:")
    print(confusion_matrix(y_test, y_pred))

    print("\n=== 6. Feature Importance Analysis ===")
    importances = clf.feature_importances_
    feature_importance_df = pd.DataFrame(
        {"Feature": features, "Importance": importances}
    )
    feature_importance_df = feature_importance_df.sort_values(
        by="Importance", ascending=False
    )
    print(feature_importance_df)

if __name__ == "__main__":
     main()

