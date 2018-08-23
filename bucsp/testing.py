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
import numpy as np



import plotly.graph_objs as go
datasets, groups = return_options('/home/ashaki/Downloads/mlh170821i.004.hdf5')

app = dash.Dash()

app.layout = html.Div([
    dcc.Graph(id = 'Full_Plot'),
    html.Label('Mode/Beam'),
    dcc.Dropdown(
        id = 'Group_Dropdown',
        options=groups,
        value='Array with kinst=31 and mdtyp=115 and pl=0.00048 /1D Parameters',
    ),
    html.Label('Parameter'),
    dcc.Dropdown(
        id = 'Dataset_Dropdown',
        options=datasets,
        value = 'ne'
    ),
    dcc.RadioItems(
            id = 'linorlog',
            options = [{'label' : i, 'value' : i} for i in ['linear', 'log']],
            value = 'linear',
            ) #you can change betwwen log or linear scale





], style={'columnCount': 2})




@app.callback(
     dash.dependencies.Output('Full_Plot', 'figure'),
     [dash.dependencies.Input('Dataset_Dropdown', 'value'),
     dash.dependencies.Input('Group_Dropdown', 'value'),
     dash.dependencies.Input('linorlog', 'value')]
     )   
def update_figure(group, parameter, linorlogvalue):
    print(parameter + "/" + group)
    newtime, rng ,data = returningdata2('/home/ashaki/Downloads/mlh170821i.004.hdf5', parameter + "/" + group)
    if (linorlogvalue == 'log'):
        data = np.log(data)
    else:
        data = data
    return{
        'data':[go.Contour(  #determines the type of graph which will be plotted
            z = data,
            colorscale = 'Jet',
        )
    ],
        'layout': go.Layout(
            autosize = False,
            width = 1000,
            height = 1000,
            xaxis={
                'title' : 'time',
                'tickvals' : np.arange(len(newtime)),
                'ticktext' :newtime,
            },
            yaxis={
                'title' : 'range (km)',
                'tickvals' : np.arange(len(rng)),
                'ticktext' : rng,
                
            })
}



if __name__ == '__main__':
   app.run_server(debug=True)
