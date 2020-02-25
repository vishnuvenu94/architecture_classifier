FROM python:3.6-slim-stretch

RUN apt update
RUN apt install -y python3-dev gcc

# Install pytorch and fastai
RUN pip install torch_nightly -f https://download.pytorch.org/whl/nightly/cpu/torch_nightly.html
RUN pip install fastai


RUN pip install flask waitress


WORKDIR /app
COPY . /app




# Start the server
CMD python3 app.py