import pandas as pd
import numpy as np

def load_csv(file_path):
    try:
        data = pd.read_csv(file_path)
        print("\n✅ File loaded successfully.\n")
        return data
    except FileNotFoundError:
        print("❌ File not found.")
        return None

def show_basic_info(df):
    print("📊 Dataset Preview:\n", df.head())
    print("\n📏 Dataset Shape:", df.shape)
    print("\n📌 Column Data Types:\n", df.dtypes)
    print("\n🧼 Missing Values:\n", df.isnull().sum())

def show_summary_stats(df):
    print("\n📈 Summary Statistics:\n", df.describe())

def column_analysis(df):
    column = input("\n🔍 Enter a column name to analyze: ")
    if column in df.columns:
        print(f"\n📊 Analyzing column: {column}")
        print("➡️ Mean:", df[column].mean())
        print("➡️ Median:", df[column].median())
        print("➡️ Mode:", df[column].mode().values)
        print("➡️ Std Dev:", df[column].std())
    else:
        print("❌ Column not found.")

def main():
    print("=== CSV Data Analyzer ===")
    file_path = input("📁 Enter the path to your CSV file: ")
    df = load_csv(file_path)

    if df is not None:
        show_basic_info(df)
        show_summary_stats(df)
        while True:
            more = input("\n🔁 Want to analyze a specific column? (y/n): ").lower()
            if more == 'y':
                column_analysis(df)
            else:
                print("👋 Exiting...")
                break

if __name__ == "__main__":
    main()
