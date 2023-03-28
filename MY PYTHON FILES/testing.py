import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pizza=pd.read_csv(r'C:\Users\cdac\Documents\GitHub\CDAC-PYTHON-WITH-AI\JUPITER FOLDER (AI)\ASSIGNMENTS\pizza_sales.csv')
file=pizza.copy()

file.isnull().sum()



