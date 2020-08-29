# ========================================================================== #
#                                                                            #
#      @ AUTHOR : Brandon Mulas                                              #
#      @   DATE : 20200226114738                                             #
#      @  TITLE : demo-dash                                                  #
#                                                                            #
# ========================================================================== #
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html


"""
    External stylesheets is going to be linked to the bootstrap cdn
    bootswatch template. Use this template to give yourself fast styling
    options.
"""
fa_bootstrap = "https://stackpath.bootstrapcdn.com/font-awesome/"
ext_style = [
    dbc.themes.SIMPLEX,
    f"{fa_bootstrap}4.7.0/css/font-awesome.min.css"
]

"""
    Meta tags are meta
"""
meta_tags = [{'name':'viewport',
              'content':'width=device-width, initial-scale=1'}]

"""
    Define app as dash.Dash object. Set external stylesheets and meta tags.
"""
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__,
                # external_stylesheets=external_stylesheets,
                external_stylesheets=ext_style,
                meta_tags=meta_tags)
app.config.suppress_callback_exceptions = True
app.title = "My Awesome Title"
server = app.server
