import src
import pandas as pd

if __name__ == "__main__":
    anie = src.Animal()
    anie.feed()
    print(pd.read_csv("src/data.csv"))