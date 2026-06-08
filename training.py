import pandas as pd
import joblib
from sklearn.linear_model import LinearRegression

# -----------------------------
# LOAD DATA
# -----------------------------
df = pd.read_csv("data/Bangalore.csv")

# -----------------------------
# SELECT 20 FEATURES
# -----------------------------
X = df[[
    "Area",
    "No. of Bedrooms",
    "Resale",
    "CarParking",
    "24X7Security",
    "PowerBackup",
    "LiftAvailable",
    "MaintenanceStaff",
    "RainWaterHarvesting",
    "VaastuCompliant",
    "Intercom",
    "StaffQuarter",
    "Gasconnection",
    "AC",
    "Wifi",
    "Children'splayarea",
    "WashingMachine",
    "DiningTable",
    "Wardrobe",
    "Refrigerator"
]]

y = df["Price"]

# -----------------------------
# TRAIN MODEL
# -----------------------------
model = LinearRegression()
model.fit(X, y)

# -----------------------------
# SAVE MODEL
# -----------------------------
joblib.dump(model, "models/linear_regression_model.pkl")

print("✅ Model trained with 20 features and saved")
print("Model trained with shape:", X.shape)