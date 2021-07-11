
import pandas
import plotly.express as px

import plotly.graph_objects as go
from plotly.subplots import make_subplots

ln = pandas.read_csv('recife_data.csv') 
bl = pandas.read_csv('global_data.csv')


'''
fig = px.line(ln, x='year', y=[ln['avg_temp'],bl['avg_temp'].loc[1:182]])

fig.update_layout(title_text='Udacity Exercise', legend_title='Lines')
fig.update_yaxes(

fig.show()
'''

fig = make_subplots(specs=[[{"secondary_y": True}]])

fig.add_trace(
    go.Scatter(x=ln['year'], y=ln['avg_temp'], name="Recife City data"),
    secondary_y=False,
)

fig.add_trace(
    go.Scatter(x=ln['year'], y=bl['avg_temp'], name="Global data"),
    secondary_y=True,
)

fig.update_layout(
    title_text="Udacity Exercise - J Neilton"
)

fig.update_xaxes(title_text="year")

#fig.update_yaxes(title_text="<b>primary</b> yaxis title", secondary_y=False)
#fig.update_yaxes(title_text="<b>secondary</b> yaxis title", secondary_y=True)

fig.show()








