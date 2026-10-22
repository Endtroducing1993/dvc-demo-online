import pandas as pd
import numpy as np
import os


df=pd.read_csv("https://github.com/araj2/customer-database/blob/master/Ecommerce%20Customers.csv?raw=true")

df=df.iloc[:,3:]

df=df[df['Length of Membership']>3]

df.to_csv(os.path.join('data','customer.csv')) 