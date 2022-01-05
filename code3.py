import csv
import pandas as pd
import plotly.express as pe

data = pd.read_csv("data.csv")
datamean = (data.groupby(["student_id","level"], as_index= False)["attempt"].mean())

df = pe.scatter(datamean , x = "student_id" , y = "level" , color = "attempt" , size = "attempt")
df.show()
