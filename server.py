from flask import Flask, request, jsonify, render_template
import os
from fastai.vision import *
from io import BytesIO
import sys
from waitress import serve


PORT = 8080

app = Flask(__name__)


cwd = os.getcwd()
model_path = cwd + '/models'

learner = load_learner(model_path, 'model.pkl')


def predict_image_from_bytes(bytes):
    img = open_image(BytesIO(bytes))
    # print(learner.predict(img))
    pred_class, pred_index, outputs = learner.predict(img)
    int_index = int(pred_index)

    pred_perc = round(float(outputs[int_index])*100)
    if pred_perc < 90:
        result = f"OOPS, Not sure about this one but I think it is {str(pred_class).upper()}"
    else:
        result = f'It is {str(pred_class).upper()} architecture.'

    return jsonify({"result": result})


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyzeImage():
    print(request.files)

    try:
        image = request.files["file"].read()
    except:
        pass

    return predict_image_from_bytes(image)


if __name__ == '__main__':
    serve(app, listen='*:{}'.format(str(PORT)))
