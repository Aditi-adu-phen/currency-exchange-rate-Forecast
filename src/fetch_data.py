
from pathlib import Path
import pandas as pd
import yfinance as yf

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "dataset"
DATA_DIR.mkdir(exist_ok=True)


def main():
    ticker = "INR=X"

    print("Downloading historical USD-INR data...")

    data = yf.download(
        ticker,
        period="10y",
        interval="1d",
        auto_adjust=False,
        progress=False
    )

    if data.empty:
        raise ValueError(
            "No data downloaded. Please check your internet connection."
        )

    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.get_level_values(0)

    data = data.reset_index()

    required_columns = ["Date", "Open", "High", "Low", "Close"]

    data = data[required_columns]
    data = data.dropna()
    data = data.sort_values("Date")

    output_file = DATA_DIR / "usd_inr.csv"
    data.to_csv(output_file, index=False)

    print("Dataset downloaded successfully.")
    print("Saved to:", output_file)
    print(data.head())


if __name__ == "__main__":
    main()
