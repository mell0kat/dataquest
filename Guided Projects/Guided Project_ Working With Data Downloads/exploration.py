import pandas as pd

if __name__ == "__main__":
    data = pd.read_csv('./data/CRDC2013_14.csv', encoding="Latin-1")

    pivot_1 = pd.pivot_table(data, values=["TOT_ENR_M", "TOT_ENR_F"], index="JJ", aggfunc="sum")
    print(data['JJ'].value_counts())
    print(pivot_1)
    pivot_2 = pd.pivot_table(data, values=["TOT_ENR_M", "TOT_ENR_F"], index="SCH_STATUS_MAGNET", aggfunc="sum") 
    print('\n\n\n\n')
    print(data['SCH_STATUS_MAGNET'].value_counts())
    print(pivot_2)