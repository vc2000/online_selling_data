import pandas as pd 
from os import listdir
from os.path import isfile, join


def cleandata(directory):
    alldata = [f for f in listdir(directory) if isfile(join("data", f))]
    df_list=list()
    for i in alldata :
        print(i)
        df = pd.read_csv(directory + "/" +i, encoding="ISO-8859-1")
        df_name_phone_email = df.iloc[:,2:5]
        df_name_phone_email=df_name_phone_email.drop('Buyer Phone Number',axis=1).dropna()
        df_list.append(df_name_phone_email)
    result = pd.concat(df_list)
    result.to_csv("email_list.csv",encoding="utf-8")
    print("done")

cleandata("data")