#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 13:36:04 2018

@author: ashaki
"""
import dash
import dash_core_components as dcc
import dash_html_components as html
from returningdata2 import returningdata2
from readh5file import print_hdf5_file_structure, print_hdf5_item_structure, return_options
from dash.dependencies import Input, Output
from readh5file import print_hdf5_file_structure, print_hdf5_item_structure

import plotly.graph_objs as go

options = return_options('/home/ashaki/Downloads/mlh170821i.004.hdf5')

app = dash.Dash()

app.layout = html.Div([
    dcc.Graph(id = 'Full_Plot'),
    html.Label('Dropdown'),
    dcc.Dropdown(
        id = 'Selection_Dropdown',
        options=options,
        value='ne'
    ),





], style={'columnCount': 2})




@app.callback(
     dash.dependencies.Output('Full_Plot', 'figure'),
     [dash.dependencies.Input('Selection_Dropdown', 'value')]
     )   
def update_figure(type):
    print(type)
    t,rng,data = returningdata2('/home/ashaki/Downloads/mlh170821i.004.hdf5', type)
    return{
        'data':[go.Surface(  #determines the type of graph which will be plotted
            z = data,
            colorscale = 'Jet',
        )
    ],
        'layout': go.Layout(
            xaxis={
                'title' : 'time',
            },
            yaxis={
                'title' : 'range'
            })
}



if __name__ == '__main__':
   app.run_server(debug=True)
