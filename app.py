import numpy as np
from flask import Flask, request, jsonify
import pickle
from fastai.tabular import *
import os
from fastai.vision import open_image
from io import BytesIO


app = Flask(__name__)


cwd = os.getcwd()
path = cwd + '/models'





model = load_learner(path, 'export.pkl')


@app.route("/classify-url", methods=["POST"])
def classify_url():
    img = request.files["image"].read()
    img = open_image(io.BytesIO(img))
    pred_class= str(model.predict(img))
    
    return pred_class




    



if __name__ == '__main__':
    app.run(debug=True)
