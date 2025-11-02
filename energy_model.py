import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
import joblib
import warnings

# --- CONFIGURATION ---
FEATURES = ['T1', 'RH_1', 'T_out', 'Windspeed', 'lights']
TARGET = 'Appliances'
MODEL_FILE = 'energy_model.pkl'
SCALER_FILE = 'energy_scaler.pkl'

warnings.filterwarnings('ignore')

print("--- 1. Data Loading and Preparation ---")
# Load the dataset
try:
    df = pd.read_csv('energydata_complete.csv', skipinitialspace=True)
except FileNotFoundError:
    print("Error: 'energydata_complete.csv' not found.")
    exit()

# Select the required features and target, and handle any missing values
df_model = df[FEATURES + [TARGET]].dropna()

X = df_model[FEATURES]
y = df_model[TARGET]

print(f"Data prepared. Total samples: {len(X)}")

print("\n--- 2. Training and Saving Final Production Artifacts ---")

# 1. Final Scaler (Fit on ALL X data)
final_scaler = StandardScaler()
final_scaler.fit(X)
X_scaled_full = final_scaler.transform(X)
print(f"Scaler fit successfully and saved to: {SCALER_FILE}")

# 2. Final Model
final_model = RandomForestRegressor(
    n_estimators=200,
    max_depth=20,
    min_samples_leaf=2,
    min_samples_split=5,
    max_features='sqrt',
    random_state=42,
    n_jobs=-1
)
final_model.fit(X_scaled_full, y)
print(f"Model trained successfully and saved to: {MODEL_FILE}")

# --- 3. Saving Artifacts ---
joblib.dump(final_model, MODEL_FILE)
joblib.dump(final_scaler, SCALER_FILE)

print("\n--- Procedure Complete: Run 'app.py' next to start the API ---")
