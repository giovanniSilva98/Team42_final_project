"""
Run this file to start dashboard application.
The file contains the whole app, to modify functionalites
or callbacks you need to modifies this file.
"""
import os
import pathlib
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
import dash_table
import plotly.graph_objs as go
import dash_daq as daq

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# ======= App object creation =======
app = dash.Dash(
    __name__,
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
)
app.title = "StarsDex"
server = app.server
app.config["suppress_callback_exceptions"] = True

# ======= Example Graph from dataframe =======
import plotly.express as px
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

# ======= Initial graph creation =======
def makesphere(center, radius, resolution=10):
    """Return the coordinates for plotting a sphere centered at (x,y,z)"""
    x=center[0]
    y=center[1]
    z=center[2]
    u, v = np.mgrid[0:2*np.pi:resolution*2j, 0:np.pi:resolution*1j]
    X = radius * np.cos(u)*np.sin(v) + x
    Y = radius * np.sin(u)*np.sin(v) + y
    Z = radius * np.cos(v) + z
    return (X, Y, Z)

fig1 = plt.figure("Spheres")
ax1 = fig1.add_subplot(projection='3d')
center1=[1,1,1]
radius=8
X, Y, Z = makesphere(center1, radius)
ax1.plot_surface(X, Y, Z, color="r")

# ======= Buil App Components =======
def build_banner():
    """Function that builds the banner"""
    return html.Div(
        id="banner",
        className="banner",
        children=[
            html.Div(
                id="banner-text",
                className='fill',
                children=[
                     html.A(
                        html.Img(id="title-icon",src=app.get_asset_url("dash-logo-star.PNG"))
                    )
                ],style={'height':"60px"}
            ),
            html.Div(
                id="banner-logo",
                className='fill',
                children=[
                    html.Button(
                        id="learn-more-button", children="LEARN MORE", n_clicks=0
                    ),
                    html.A(
                        html.Img(id="title-icon2", src=app.get_asset_url("Logo_star_viz.jpeg")), 
                        
                    ),
                ],
            ),
        ],
    )


def build_tabs():
    """Function that builds the tabs"""
    return html.Div(
        id="tabs",
        className="tabs",
        children=[
            dcc.Tabs(
                id="app-tabs",
                value="tab1",
                className="custom-tabs",
                children=[
                    dcc.Tab(
                        id="Specs-tab",
                        label="STAR-(T)",
                        value="tab1",
                        className="custom-tab",
                        selected_className="custom-tab--selected",
                    ),
                    dcc.Tab(
                        id="Control-chart-tab",
                        label="OBSERVE",
                        value="tab2",
                        className="custom-tab",
                        selected_className="custom-tab--selected",
                    ),
                    dcc.Tab(
                        id="Achive-tab",
                        label="ACHIVEMENTS",
                        value="tab3",
                        className="custom-tab",
                        selected_className="custom-tab--selected",
                    )
                ],
            )
        ],
    )


def build_tab_1():
    """Build the tab 1 layout"""
    return [
        html.Div(
            id="set-specs-intro-container",
            # className='twelve columns',
            children=html.P(
                "Use the sliders to select the characteristics of the star you want to visualize."
            ),
        ),

        html.Div(
            id= "tab1-main-cont",
            children=[
                html.Div(
                    id= "tab1-left",
                    className='six columns',
                    children=[
                        html.Div(
                            id="input-slider",
                            children=[
                                dcc.Slider(0, 20,
                                value=10,
                                id='my-slider'
                                ),

                                dcc.Slider(0, 20, 
                                value=10,
                                id='my-slider1'
                                ),
                                html.Button('Submit', id='submit-input', n_clicks=0, 
                                style={"float":"right", "margin":"4px 25px 4px 4px"})
                            ],),
                        html.Div(
                            id="sphere-graph",
                            style={"margin":"40px"},
                            children=[
                                html.H3('Grafico sfere'),
                                dcc.Graph(id='example-graph',figure=fig)
                            ]
                        )
                    ]
                ),
                html.Div(
                    id="tab1-right",
                    className='six columns',
                    children=[
                        html.Div(
                            id="hr-graph",
                            children=[
                                html.H1('Grafico qua'),
                                dcc.Graph(id='example-graph',figure=fig)
                            ]
                        ),
                        html.Div(
                            id="star-type",
                            children=[
                                html.H3('Qua INFO'),
                                html.H5('NOME STELLA: '),
                                html.Button('Next>>', id='submit-input', n_clicks=0),
                            ]
                        )
                    ]
                )
            ]
        )
        # html.Div(
        #     id="settings-menu",
        #     children=[
        #         html.Div(
        #             id="metric-select-menu",
        #             # className='five columns',
        #             children=[
        #                 html.Label(id="metric-select-title", children="Select Temperature"),
        #                 html.Br(),
        #                 dcc.Dropdown(
        #                     id="metric-select-dropdown",
        #                     options=list(
        #                         {"label": param, "value": param} for param in params[1:]
        #                     ),
        #                     value=params[1],
        #                 ),
        #             ],
        #         ),
        #         html.Div(
        #             id="value-setter-menu",
        #             # className='six columns',
        #             children=[
        #                 html.Div(id="value-setter-panel"),
        #                 html.Br(),
        #                 html.Div(
        #                     id="button-div",
        #                     children=[
        #                         html.Button("Update", id="value-setter-set-btn"),
        #                         html.Button(
        #                             "View current setup",
        #                             id="value-setter-view-btn",
        #                             n_clicks=0,
        #                         ),
        #                     ],
        #                 ),
        #                 html.Div(
        #                     id="value-setter-view-output", className="output-datatable"
        #                 ),
        #             ],
        #         ),
        #     ],
        # ),
    ]

def build_tab_2():
    """Build the tab 2 layout"""
    return [
        html.Div(
            id="tab2-intro",
            # className='twelve columns',
            children=html.P(
                "You can observe the stellar SHORT term variability here."
            ),
        ),

        html.Div(
            id= "tab2-main-cont",
            children=[
                html.Div(
                    id= "tab2-left",
                    className='six columns',
                    children=[
                        html.Div(
                            id="veideo-graph",
                            children=[
                                html.H3('Video luminosity'),
                                dcc.Graph(id='example-graph',figure=fig)
                            ]
                        )
                    ]
                ),
                html.Div(
                    id="tab2-right",
                    className='six columns',
                    children=[
                        html.Div(
                            id="luminosity-plot",
                            children=[
                                html.H1('Grafico qua'),
                                dcc.Graph(id='example-graph',figure=fig)
                            ]
                        ),
                        html.Div(
                            id="star-type",
                            children=[
                                html.H3('Qua INFO'),
                                html.H5('NOME STELLA: , CATEGORIAL VARIABILITY'),
                                html.Button('DELETE>>', id='submit-input', n_clicks=0),
                            ]
                        )
                    ]
                )
            ]
        )
        
    ]

def build_tab2_2():
    """Build the tab 2 long term variability"""
    return [
        html.Div(
            id="tab22-intro",
            # className='twelve columns',
            children=html.P(
                "You can observe the stellar LONG term variability here."
            ),
        ),

        html.Div(
            id= "tab22-main-cont",
            children=[
                html.Div(
                    id= "tab22-left",
                    className='six columns',
                    children=[
                        html.H5('graph here'),
                        dcc.Graph(id='example-graph',figure=fig)
                    ]
                ),
                html.Div(
                    id="tab22-right",
                    className='six columns',
                    children=[
                        html.H5('graph2 here'),
                        dcc.Graph(id='example-graph',figure=fig)
                    ]
                ),
                html.Div(
                    id="prova33",
                    children=[
                        html.H5('pulsanti qua'),
                        html.Button('DELETE>>', id='submit-input', n_clicks=0),
                    ]
                )
            ]
        )
        
    ]

def build_tab_achive():
    """Build the tab achivement layout"""
    return [
        html.Div(
            id="tab3-intro",
            # className='twelve columns',
            children=html.P(
                "All the available achivements here."
            ),
        ),

        html.Div(
            id= "tab3-main-cont",
            children=[
                html.Div(
                    id= "tab3-left",
                    className='six columns',
                    children=[
                        html.Div(id = "achivement-row",
                            children=[
                                html.Div(id="achive-icon",
                                className='two columns', 
                                children=[html.H5('icona qua')]),
                                html.Div(id="achive-info",
                                className='four columns',children=[html.H5('informazioni qua')])
                            ]
                        ),
                        html.Div(id = "achivement-row",
                            children=[
                                html.Div(id="achive-icon",
                                className='two columns', 
                                children=[html.H5('icona qua')]),
                                html.Div(id="achive-info",
                                className='four columns',children=[html.H5('informazioni qua')])
                            ]
                        ),
                        html.Div(
                            id = "achivement-row",
                            children=[
                                html.Div(id="achive-icon",
                                className='two columns', 
                                children=[html.H5('icona qua')]),
                                html.Div(id="achive-info",
                                className='four columns',children=[html.H5('informazioni qua')])
                            ]
                        )  
                    ]
                ),
                html.Div(
                    id="tab3-right",
                    className='six columns',
                    children=[
                        html.Div(id = "achivement-row",
                            children=[
                                html.Div(id="achive-icon",
                                className='two columns', 
                                children=[html.H5('icona qua')]),
                                html.Div(id="achive-info",
                                className='four columns',children=[html.H5('informazioni qua')])
                            ]
                        
                        ),
                        html.Div(id = "achivement-row",
                            children=[
                                html.Div(id="achive-icon",
                                className='two columns', 
                                children=[html.H5('icona qua')]),
                                html.Div(id="achive-info",
                                className='four columns',children=[html.H5('informazioni qua')])
                            ]
                        
                        ),
                        html.Div(
                            id = "achivement-row",
                            children=[
                                html.Div(id="achive-icon",
                                className='two columns', 
                                children=[html.H5('icona qua')]),
                                html.Div(id="achive-info",
                                className='four columns',children=[html.H5('informazioni qua')])
                            ]
                        
                        )
                    ]
                )
            ]
        )
    ]

#========= modal popup definition ==========
def generate_modal():
    """ Example popup working"""
    return html.Div(
        id="markdown",
        className="modal",
        children=(
            html.Div(
                id="markdown-container",
                className="markdown-container",
                children=[
                    html.Div(
                        className="close-container",
                        children=html.Button(
                            "Close",
                            id="markdown_close",
                            n_clicks=0,
                            className="closeButton",
                        ),
                    ),
                    html.Div(
                        className="markdown-text",
                        children=dcc.Markdown(
                            children=(
                                """
                                ###### Ciao
                                Prova prova prova linea 1
                                ###### Ciao 2 scemo
                                mettere istruzioni qua stronzo
                                ###### Source Code
                                You can find the source code up your ass
                                """
                            )
                        ),
                    ),
                ],
            )
        ),
    )

#This is the current layout ---> the higher level of "div" that you can call
app.layout = html.Div(
    id="big-app-container",
    children=[
        build_banner(),
        # Update periodically your page: 
        dcc.Interval(
            id="interval-component",
            interval=2 * 1000,  # in milliseconds
            n_intervals=50,  # start at batch 50
            disabled=True,
        ),

        html.Div(
            id="app-container",
            children=[
                build_tabs(),
                # Main app
                html.Div(id="app-content"),
            ],
        ),
        # dcc.Store(id="value-setter-store", data=init_value_setter_store()),
        dcc.Store(id="n-interval-stage", data=50),
        generate_modal(),
    ],
)



# ======= Callbacks for tab rendering =======
@app.callback(
    # check if the periodic updates are trully necessary
    [Output("app-content", "children"), Output("interval-component", "n_intervals")],
    [Input("app-tabs", "value")],
    [State("n-interval-stage", "data")],
)
def render_tab_content(tab_switch, stopped_interval):
    """ Function that tell what to build in the
    div 'app-content' that is the container
    the main page """
    if tab_switch == "tab1":
        return build_tab_1(), stopped_interval
    if tab_switch == "tab2":
        return build_tab2_2(), stopped_interval

    return ( build_tab_achive(), stopped_interval,
        # html.Div(
        #     id="status-container",
        #     children=[
        #         build_quick_stats_panel(),
        #         html.Div(
        #             id="graphs-container",
        #             children=[build_top_panel(stopped_interval), build_chart_panel()],
        #         ),
        #     ],
        # ),
        # stopped_interval,
    )

# ======= Callbacks for modal popup =======
@app.callback(
    Output("markdown", "style"),
    [Input("learn-more-button", "n_clicks"), Input("markdown_close", "n_clicks")],
)
def update_click_output(button_click, close_click):
    ctx = dash.callback_context

    if ctx.triggered:
        prop_id = ctx.triggered[0]["prop_id"].split(".")[0]
        if prop_id == "learn-more-button":
            return {"display": "block"}

    return {"display": "none"}


# Running the server
if __name__ == "__main__":
    app.run_server(debug=True, port=8050)
