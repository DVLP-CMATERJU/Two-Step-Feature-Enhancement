import numpy as np
import pandas as pd

def join_csv(csv_list,dset_name):
        for num,i in enumerate(csv_list):
                if '.csv' not in i:
                        i=i+'.csv'
                if num==0:
                    df = np.asarray(pd.read_csv(i,header=None))
                    target = df[:,-1]
                    df = df[:,0:-1]
                else:
                    df2 = np.asarray(pd.read_csv(i,header=None))
                    df2 = df2[:,0:-1]
                    df = np.concatenate((df,df2),axis=1)
        df = np.transpose(df)
        df = np.transpose(np.vstack([df,target]))
        np.savetxt(dset_name+".csv", df, delimiter=",")
        return df

csv_list=["f1","f2"]
df = join_csv(csv_list)
