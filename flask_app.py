
# A very simple Flask Hello World app for you to get started with...

from flask import Flask
import numpy as np
import pandas as pd, seaborn as sns, matplotlib.pyplot as plt
from IPython.display import display,HTML
import base64
from io import BytesIO
from flask import Response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

app = Flask(__name__)

# numpy (rendered properly)
@app.route('/')
def hello_world():
    # numpy
    a = np.array([5, 8,9, 10,12])
    b = np.array([[5, 8,9, 10,12]])
    return r'''
    Hello there from Flask!
    a is {},
    a transpose is {},
    b is {},
    b transpose is {},
    b transpose is {}
    '''.format(a,
    a.transpose(),
    b,
    b.transpose(),
    pd.DataFrame(b).to_html(),
    )


 # matplotlib (rendered properly)
@app.route('/matplotlib')
def hello_word():
    # Generate the figure **without using pyplot**.
    fig = Figure()
    ax = fig.subplots()
    ax.plot([1, 2])
    # Save it to a temporary buffer.
    buf = BytesIO()
    fig.savefig(buf, format="jpg")
    # Embed the result in the html output.
    data = base64.b64encode(buf.getbuffer()).decode("ascii")

    fig = Figure()
    ax = fig.subplots()
    ax.plot([10, 20])
    # Save it to a temporary buffer.
    buf = BytesIO()
    fig.savefig(buf, format="jpg")
    # Embed the result in the html output.
    data1 = base64.b64encode(buf.getbuffer()).decode("ascii")




    return f'''
    <img src='data:image/jpg;base64,{data}'/>
    <img src='data:image/png;base64,{data}'/>
    <img src='data:image/jpg;base64,{data1}'/>
    <img src='data:image/png;base64,{data1}'/>
    '''


# pandas (rendered properly)
@app.route('/pandas')
def pandas():
    data = {
      "calories": [420, 380, 390],
      "duration": [50, 40, 45]
    }

    #load data into a DataFrame object:
    df = pd.DataFrame(data)
    return r'''
    The dataframe is {},
    The dataframe is {},
    '''.format(df.to_html(header="true", table_id="table"),
        df,
    )










