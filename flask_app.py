
# A very simple Flask Hello World app for you to get started with...

from flask import Flask
# import pyqrcode # pip install PyQRCode
import numpy as np
from skimage import io # pip install scikit-image
# import urllib
# import urllib.request
import pandas as pd, seaborn as sns, matplotlib.pyplot as plt
from IPython.display import display,HTML
import base64
from PIL import Image
import requests
from io import BytesIO
from flask import Response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
#import sys # to access the system
import cv2   # pip install opencv-python
import os
from sklearn import datasets #  pip install scikit-learn

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
    b transpose is {},
    os.getcwd() is {},
    os.listdir() is {},
    '''.format(a,
    a.transpose(),
    b,
    b.transpose(),
    pd.DataFrame(b).to_html(),
    os.getcwd(),
    os.listdir(),
    # os.listdir("/home/sree8pythonanywhere/mysite/"),
    # os.path.join('static', 'IMG'),
    )


 # matplotlib (rendered properly in local, but error for URL)
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


    # https://stackoverflow.com/questions/7391945/how-do-i-read-image-data-from-a-url
    response = requests.get("https://www.pyimagesearch.com/wp-content/uploads/2015/01/google_logo.png")
    data2 = Image.open(BytesIO(response.content))

    buffered = BytesIO()
    data2.save(buffered, format="png")
    data2 = base64.b64encode(buffered.getbuffer()).decode("ascii")



    return f'''
    <img src='data:image/jpg;base64,{data}'/>
    <img src='data:image/png;base64,{data}'/>
    <img src='data:image/jpg;base64,{data1}'/>
    <img src='data:image/png;base64,{data1}'/>
    <img src='data:image/png;base64,{data2}'/>
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

# IMG_FOLDER = os.path.join('static', 'IMG')
# app.config['UPLOAD_FOLDER'] = IMG_FOLDER
# Sheep = os.path.join(app.config['UPLOAD_FOLDER'], 'Sheep.png')

# opencv (not rendered properly)
@app.route('/opencv')
def opencv():
    # url = 'https://media.geeksforgeeks.org/wp-content/uploads/20211003151646/geeks14.png'


    # with urllib.request.urlopen(url) as resp:

    #     # read image as an numpy array
    #     image = np.asarray(bytearray(resp.read()), dtype="uint8")

    #     # use imdecode function
    #     image = cv2.imdecode(image, cv2.IMREAD_COLOR)

    #     # display image
    #     cv2.imwrite("result.jpg", image)
    #     image = image.astype(np.uint8)

    #     cv2.imshow("image", image)

    #     # waits for user to press any key
    #     # (this is necessary to avoid Python kernel form crashing)
    #     cv2.waitKey(0)

    #     # closing all open windows
    #     cv2.destroyAllWindows()
    image1 = cv.imread('image1.jpg')
    image2 = cv.imread('image2.jpg')
    plt.subplot(1, 2, 1)
    plt.imshow(image1)
    plt.subplot(1, 2, 2)
    plt.imshow(image2)



    return ''

@app.route('/sklearn')
def sklearn():

    # Load data
    iris= datasets.load_iris()
    # Print shape of data to confirm data is loaded
    #print(iris.data.shape)
    return f'''
    <p>{
        iris.data.shape
        }</p>
    '''





