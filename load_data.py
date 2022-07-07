import numpy as np
import pandas as pd


def load_data(PATH):
    raw_data = pd.read_json(PATH)
    print(raw_data.head())
