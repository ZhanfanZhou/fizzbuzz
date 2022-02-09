FROM jupyter/scipy-notebook

RUN mkdir hugging-models

COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt 

COPY app.py ./app.py

RUN python3 app.py