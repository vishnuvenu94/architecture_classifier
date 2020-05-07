# Architecture Classifier

A simple app which tries its best to classify between these architectural styles : \
Victorian \
Japanese \
Islamic \
Romanesque \
Tudor \
Neoclassical \
Modernist 

The model was trained using the fastai librabry built on top of PyTorch. The app lets you upload pictures and gives a prediction.

You can can check it out by running the Dockerfile

`docker build -t demo . && docker run --rm -it -p 8080:8080 demo`

