import pandas as pd
import numpy  as np
import matplotlib.pyplot as plt

file_path = "/content/mitbih_test.csv"

try:
  data = pd.read_csv(file_path)
  print ("data loaded")
except:
  print ("failed")

print (data.info())
