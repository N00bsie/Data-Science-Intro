'''
Created on Dec 28, 2016

@author: AmarViswanathan
'''

import pandas as pd

def add_full_name(path_to_csv,path_to_new_csv):
    
    baseball_data = pd.read_csv(path_to_csv)
    
    baseball_data['nameFull'] = baseball_data['nameFirst'] + " " + baseball_data['nameLast']
    #Write back
    baseball_data.to_csv(path_to_new_csv)
    print("File was written to " + path_to_new_csv)
    
    
if __name__ == "__main__":
    path_to_csv = "../Master.csv"
    path_to_new_csv = "../MasterNew.csv"
    add_full_name(path_to_csv, path_to_new_csv)
    print("Done!")
        