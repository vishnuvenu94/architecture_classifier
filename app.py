
from flask import Flask, request, jsonify

import os
from fastai.vision import *

from io import BytesIO
import sys
from waitress import serve



PORT = 5000




app = Flask(__name__)





cwd = os.getcwd()
model_path = cwd + '/models'

learner = load_learner(model_path, 'model.pkl')







def predict_image_from_bytes(bytes):
    img = open_image(BytesIO(bytes))
    pred_class= str(learner.predict(img))

    return pred_class



@app.route("/")
def form():
    return """
        <!DOCTYPE html>
        <h2>Predict Architecture styles</h2>
        
        <form action="/upload" method="post" enctype="multipart/form-data">
            Select image to upload:
            <input type="file" name="image">
            <input type="submit" value="Upload Image">
        </form>
       
    """


@app.route("/upload", methods=["POST"])
def upload():

    try:
        image = request.files["image"].read()
    except:
        pass
        
        
    return predict_image_from_bytes(image)








    



if __name__ == '__main__':
    # app.run(debug=True)
    serve(app, listen='*:{}'.format(str(PORT)))
