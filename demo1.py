import pandas as pd 
import plotly.figure_factory as ff
df=pd.read_csv("data.csv")
figure=ff.create_distplot([df["Avg"].tolist()],["Average Result"],show_hist=False)
figure.show()