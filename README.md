# House Price Prediction

A machine learning project that predicts residential house prices across six major Indian cities using Linear Regression. Built end-to-end  from raw data to a live Streamlit web app where users can input property details and get an instant price estimate.

---

## The Dataset

Six city specific CSV files covering Bangalore, Chennai, Delhi, Hyderabad, Kolkata, and Mumbai  totaling around **33,000 property listings** with **40 features** each.

Features span structural attributes (area, bedrooms, floors) and amenity flags (gymnasium, swimming pool, 24x7 security, CCTV, lift, parking, and more), making it possible to capture both the size and quality of a property in a single feature vector.

---

## Project Structure

```
House_Prediction_Project/
│
├── data/
│   ├── Bangalore.csv
│   ├── Chennai.csv
│   ├── Delhi.csv
│   ├── Hyderabad.csv
│   ├── Kolkata.csv
│   └── Mumbai.csv
│
├── notebooks/
│   └── House_price_prediction_project.ipynb   # Full EDA, preprocessing, training
│
├── apps/
│   └── app.py                                 # Streamlit prediction UI
│
├── models/
│   ├── linear_regression_model.pkl            # Serialized trained model
│   └── scaler.pkl                             # Fitted StandardScaler
│
├── requirements.txt
└── README.md
```

---

## Tech Stack

**Language:** Python 3.10

**Libraries:**

| Library | Version | Purpose |
|---|---|---|
| pandas | 2.2.2 | Data loading and manipulation |
| numpy | 1.26.4 | Numerical operations |
| scikit-learn | 1.5.1 | Model training, scaling, evaluation |
| streamlit | 1.36.0 | Interactive prediction web app |
| joblib | 1.4.2 | Model serialization |

---

## Setup

**Clone the repository**

```bash
git clone https://github.com/madiboyinakalyan/House_Price_Prediction.git
cd House_Prediction_Project
```

**Create a virtual environment**

```bash
python -m venv .venv
.venv\Scripts\activate        # Windows
source .venv/bin/activate     # macOS / Linux
```

**Install dependencies**

```bash
pip install -r requirements.txt
```

---

## Running the App

The Streamlit app loads the pre-trained model and lets you predict prices interactively.

```bash
cd apps
streamlit run app.py
```

The app takes the following inputs and returns an estimated price in INR:

| Input | Type |
|---|---|
| Bedrooms | Number |
| Bathrooms | Number |
| Floors | Number |
| Total Square Feet | Number |
| Parking Spaces | Number |
| House Age (Years) | Number |
| Furnishing Type | Dropdown |

---

## How the Model Was Built

The full workflow lives in `notebooks/House_price_prediction_project.ipynb`.

**Step 1 — Data loading:** All six city CSVs are loaded and merged into a single DataFrame.

**Step 2 — Preprocessing:** Missing values handled, categorical features (furnishing type, location) encoded, and all binary amenity flags retained as-is.

**Step 3 — Feature scaling:** `StandardScaler` applied to numeric features before training. The fitted scaler is saved to `models/scaler.pkl` so the app uses identical transformations at inference time.

**Step 4 — Training:** A `LinearRegression` model from scikit-learn trained on the processed features. Model serialized to `models/linear_regression_model.pkl` using joblib.

**Step 5 — Evaluation:** Performance measured on a held-out test split.

---

## Model Performance

| Metric | Value |
|---|---|
| R² Score | *(fill after training)* |
| Mean Absolute Error | *(fill after training)* |
| Root Mean Squared Error | *(fill after training)* |

Run the notebook to see your exact numbers  they print automatically at the evaluation cell.

---

## Future Work

A few directions worth exploring:

**Better models:** Random Forest or XGBoost would likely outperform Linear Regression here, especially with 40 mixed-type features. Worth benchmarking.

**City specific models:** Training separate models per city rather than a pooled model could reduce noise from city-level price differences.

**Feature engineering:** Price per square foot, proximity based location encoding, and interaction terms between amenities could meaningfully improve accuracy.

**Deployment:** The Streamlit app is locally runnable today deploying to Streamlit Cloud or a small VM would make it publicly accessible with no extra setup.

---

## License

MIT

---

## Author

Built by **Madiboyina Kalyan** — [github.com/madiboyinakalyan](https://github.com/madiboyinakalyan)
