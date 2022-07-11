import numpy as np
import pandas as pd

from preparation import prepare_data


def main():
    df = prepare_data(PATH)
    print(df)

if __name__ == '__main__':
    pd.set_option('display.max_colwidth', None) # show full df info
    pd.set_option('display.max_rows', 500)
    pd.set_option('display.width', 1000)
    PATH = "C:/Users/San/Documents/CS projects/yt_activity_analysis/data/Takeout/YouTube and YouTube Music/history/watch-history.json"
    main()
