import pandas as pd

if __name__ == "__main__":
    data = pd.read_csv('./data/CRDC2013_14.csv')
    data['total_enrollment'] = data['TOT_ENR_M'] + data['TOT_ENR_F']
    all_enrollment = data['total_enrollment'].sum()
    
    
    gender_labels = ['F', 'M']
    race_labels = ['HI', 'AM', 'AS', 'HP', 'BL', 'WH', 'TR']
    
    for r in race_labels:

        
        enrollment_col_name_M = 'SCH_ENR_' + r + '_' + 'M'
        enrollment_col_name_F = 'SCH_ENR_' + r + '_' + 'F'

        sum_by_gender_and_race = data[enrollment_col_name_M].sum() + data[enrollment_col_name_F].sum()
        print('race', r)
        print(sum_by_gender_and_race / all_enrollment * 100) 