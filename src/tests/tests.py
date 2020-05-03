

import build_features as bf
import pandas as pd




if __name__ == '__main__':

#    os.chdir("/Users/kienlef/SynologyDrive/PPT_slides_Vorlesung/2020_Video_Vorlesung/ads_covid-19/src")
    pd_JH_data=pd.read_csv('data/processed/COVID_relational_confirmed.csv',sep=';',parse_dates=[0])
    pd_JH_data=pd_JH_data.sort_values('date',ascending=True).copy()

    #test_structure=pd_JH_data[((pd_JH_data['country']=='US')|
    #                  (pd_JH_data['country']=='Germany'))]
