
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt
import joblib

from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

ROOT = Path(__file__).resolve().parents[1]

DATA_FILE = ROOT / "dataset" / "usd_inr.csv"
OUTPUT_DIR = ROOT / "outputs"
MODEL_DIR = ROOT / "models"

FEATURES = [
    "previous_open",
    "previous_high",
    "previous_low",
    "previous_close",
    "close_2_days_ago",
    "close_5_days_ago",
    "close_5day_mean"
]


def prepare_data():

    data = pd.read_csv(DATA_FILE, parse_dates=["Date"])
    data = data.sort_values("Date").dropna().copy()

    # Use previous trading observations as model inputs.
    data["previous_open"] = data["Open"].shift(1)
    data["previous_high"] = data["High"].shift(1)
    data["previous_low"] = data["Low"].shift(1)
    data["previous_close"] = data["Close"].shift(1)

    data["close_2_days_ago"] = data["Close"].shift(2)
    data["close_5_days_ago"] = data["Close"].shift(5)

    data["close_5day_mean"] = (
        data["Close"].shift(1).rolling(5).mean()
    )

    data = data.dropna().reset_index(drop=True)

    return data


def main():

    OUTPUT_DIR.mkdir(exist_ok=True)
    MODEL_DIR.mkdir(exist_ok=True)

    if not DATA_FILE.exists():
        raise FileNotFoundError(
            "Dataset not found. Run src/fetch_data.py first."
        )

    data = prepare_data()

    X = data[FEATURES]
    y = data["Close"]

    # Chronological 80:20 split.
    split = int(len(data) * 0.80)

    X_train = X.iloc[:split]
    X_test = X.iloc[split:]

    y_train = y.iloc[:split]
    y_test = y.iloc[split:]

    model = DecisionTreeRegressor(
        max_depth=5,
        min_samples_leaf=5,
        random_state=42
    )

    print("Training Decision Tree Regression model...")

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    # Evaluation metrics.
    mae = mean_absolute_error(y_test, predictions)
    mse = mean_squared_error(y_test, predictions)
    rmse = mse ** 0.5
    r2 = r2_score(y_test, predictions)

    print("\nModel Evaluation")
    print("----------------")
    print("MAE:", round(mae, 4))
    print("MSE:", round(mse, 4))
    print("RMSE:", round(rmse, 4))
    print("R2 Score:", round(r2, 4))

    metrics = (
        f"MAE: {mae:.4f}\n"
        f"MSE: {mse:.4f}\n"
        f"RMSE: {rmse:.4f}\n"
        f"R2 Score: {r2:.4f}\n"
    )

    (OUTPUT_DIR / "metrics.txt").write_text(
        metrics, encoding="utf-8"
    )

    results = pd.DataFrame({
        "Date": data["Date"].iloc[split:],
        "Actual_Close": y_test.values,
        "Predicted_Close": predictions
    })

    results.to_csv(
        OUTPUT_DIR / "predictions.csv",
        index=False
    )

    # Actual versus predicted graph.
    plt.figure(figsize=(12, 5))

    plt.plot(
        data["Date"].iloc[split:],
        y_test.values,
        label="Actual Rate"
    )

    plt.plot(
        data["Date"].iloc[split:],
        predictions,
        label="Predicted Rate"
    )

    plt.title("Actual vs Predicted USD-INR Exchange Rate")
    plt.xlabel("Date")
    plt.ylabel("INR per USD")
    plt.legend()
    plt.tight_layout()

    plt.savefig(OUTPUT_DIR / "actual_vs_predicted.png")
    plt.close()

    # Historical exchange rate graph.
    plt.figure(figsize=(12, 5))

    plt.plot(data["Date"], data["Close"])

    plt.title("Historical USD-INR Exchange Rate")
    plt.xlabel("Date")
    plt.ylabel("INR per USD")
    plt.tight_layout()

    plt.savefig(OUTPUT_DIR / "historical_exchange_rate.png")
    plt.close()

    # Save the trained model.
    joblib.dump(
        {"model": model, "features": FEATURES},
        MODEL_DIR / "decision_tree_model.joblib"
    )

    # Estimate the next trading observation.
    raw = pd.read_csv(DATA_FILE, parse_dates=["Date"])
    raw = raw.sort_values("Date").dropna().reset_index(drop=True)

    latest = raw.iloc[-1]

    next_input = pd.DataFrame([{
        "previous_open": latest["Open"],
        "previous_high": latest["High"],
        "previous_low": latest["Low"],
        "previous_close": latest["Close"],
        "close_2_days_ago": raw.iloc[-2]["Close"],
        "close_5_days_ago": raw.iloc[-5]["Close"],
        "close_5day_mean": raw["Close"].tail(5).mean()
    }])

    next_forecast = model.predict(next_input[FEATURES])[0]

    forecast_text = (
        f"Last available date: {latest['Date'].date()}\n"
        f"Estimated next-observation close: "
        f"{next_forecast:.4f} INR per USD\n"
        "This is an educational estimate, not a guaranteed rate."
    )

    (OUTPUT_DIR / "next_observation_forecast.txt").write_text(
        forecast_text, encoding="utf-8"
    )

    print("\nNext Observation Forecast")
    print(forecast_text)

    print("\nExecution completed successfully.")


if __name__ == "__main__":
    main()
