from numpy import size
import pandas as pd
import plotly.express as px
import csv

df = pd.read_csv('datas.csv')
print(df.groupby("level")["attempt"].mean())
mean = df.groupby(["student_id", "level",],as_index=False)["attempt"].mean()
fig = px.scatter(mean,
    x = "student_id",
    y = "level",
    size = "attempt",
    color = "attempt"

)
fig.show()