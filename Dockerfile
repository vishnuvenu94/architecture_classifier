FROM tiangolo/uwsgi-nginx:python3.6

RUN apt update
RUN apt install -y python3-dev gcc

# Install pytorch and fastai
RUN pip install torch_nightly -f https://download.pytorch.org/whl/nightly/cpu/torch_nightly.html


COPY requirements.txt .
RUN pip install --upgrade -r requirements.txt


WORKDIR /app
COPY . /app




# Start the server
CMD python3 server.py