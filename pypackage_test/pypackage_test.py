"""Main module."""
import pandas as pd
def read_file(path): 
   df = pd.read_csv(path,sep=';')
   return df 