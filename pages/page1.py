
# import dash
# from dash import html, dcc, Dash
# import dash_bootstrap_components as dbc
# from dash.dependencies import Output,Input,State


# next_page = html.Div([
# html.Div(dcc.Link('Log out', href='/',style={'color':'#bed4c4','font-family': 'serif', 'font-weight': 'bold', "text-decoration": "none",'font-size':'20px'}),style={'padding-left':'80%','padding-top':'10px'}),
#         html.H1(children="This is the Next Page, the main Page",className="ap",style={
#  'color':'#89b394','text-align':'center','justify':'center','padding-top':'170px','font-weight':'bold',
#  'font-family':'courier',
#  'padding-left':'1px'  })
# ]) 
import dash
from dash import Dash, dcc, html, callback, Input, Output

dash.register_page(__name__,name="next_page")

# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# app = Dash(__name__, external_stylesheets=external_stylesheets)

layout = html.Div([
    # represents the browser address bar and doesn't render anything
    html.Div(dcc.Link('Log out', href='http://google.com',style={'color':'#bed4c4','font-family': 'serif', 'font-weight': 'bold', "text-decoration": "none",'font-size':'20px'}),style={'padding-left':'80%','padding-top':'10px'}),
        html.H1(children="This is the Next Page, the main Page",className="ap",style={
 'color':'#89b394','text-align':'center','justify':'center','padding-top':'170px','font-weight':'bold',
 'font-family':'courier',
 'padding-left':'1px'  }),
    dash.page_container,
])



if __name__ == '__main__':
    app.run_server(debug=True)