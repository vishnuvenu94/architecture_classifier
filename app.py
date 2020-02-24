import numpy as np
from flask import Flask, request, jsonify
import pickle
from fastai.tabular import *
import os
from fastai.vision import *
from fastai.metrics import error_rate
from fastai.widgets import *
from io import BytesIO



app = Flask(__name__)


bs = 64

cwd = os.getcwd()
model_path = cwd + '/models'

path=cwd + '/data'



np.random.seed(42)
data = ImageDataBunch.from_folder(path, train=".", valid_pct=0.2,
        ds_tfms=get_transforms(), size=224, num_workers=4).normalize(imagenet_stats)

learn = cnn_learner(data, models.resnet34, metrics=error_rate)

learn.model

learn.fit_one_cycle(4)

learn.export()











model = load_learner(model_path, 'export.pkl')


@app.route("/classify-url", methods=["POST"])
def classify_url():
    img = request.files["image"].read()
    img = open_image(io.BytesIO(img))
    pred_class= str(model.predict(img))
    
    return pred_class




    



if __name__ == '__main__':
    app.run(debug=True)
