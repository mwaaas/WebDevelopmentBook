from ipymonaco import *
import ipywidgets as widgets
from IPython.display import display

text = "bar"
text_widget = widgets.Text(value=text, disabled=True)

hello = Monaco(
    value="""
    def add(a, b):
        pass 
""", theme="vs", language="sql", readOnly=False)
def foo(*args, **kwargs):
    global text 
    text = "foo"
    print(f"args: {args}    kwargs: {kwargs}")
    
display(hello, text_widget)

a = widgets.Text(value=hello.value)
b = widgets.FloatSlider()
display(a,b)
mylink = widgets.jslink((a, 'value'), (hello, 'value'))

open(file)
button = widgets.Button(
    description='click me to raise an exception',
    layout={'width': '300px'}
)