import pickle
from typing import List
import pandas as pd

def load_list(filename: str) -> List:
    with open(filename, 'rb') as f:
        return pickle.load(f)

def main():
    df = pd.read_csv('data.csv')
    print(df.head())
    print(load_list('base_asset_list.pkl'))

if __name__ == '__main__':
    main()
