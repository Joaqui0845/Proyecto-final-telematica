import pandas as pd
import plotly.graph_objects as go
import dash
from dash import dcc as dcc
from dash import html as html
from flask import Flask, request, redirect

url = "http://siata.gov.co:8089/estacionesNivel/cf7bb09b4d7d859a2840e22c3f3a9a8039917cc3/"
data = pd.read_json(url, convert_dates=True)

latr = []
lonr = []
zr = []
for i in range(0, 100):
    zr.append(data['datos'][i]['porcentajeNivel'])
    latr.append(data['datos'][i]['coordenadas'][0]['latitud'])
    lonr.append(data['datos'][i]['coordenadas'][0]['longitud'])

fig = go.Figure(go.Densitymapbox(lat=latr, lon=lonr, z=zr, radius=20, opacity=0.9, zmin=0, zmax=100))
fig.update_layout(mapbox_style="stamen-terrain", mapbox_center_lon=-75.589, mapbox_center_lat=6.2429)
fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

server = Flask(__name__)

VALID_PASSWORD = "123456"

@server.route('/')
def index():
    password = request.args.get('password')
    if password == VALID_PASSWORD:
        return redirect('/dashboard')
    else:
        return redirect("https://www.youtube.com/watch?v=mCdA4bJAGGk")


app = dash.Dash(__name__, server=server, url_base_pathname='/dashboard/')

app.layout = html.Div([
    html.H1("Mapa con niveles"),
    dcc.Graph(figure=fig),
])

if __name__ == '__main__':
    server.run(host='0.0.0.0', port=5600)