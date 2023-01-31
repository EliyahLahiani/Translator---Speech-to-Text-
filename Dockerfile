FROM python:3.9
WORKDIR /tmp
COPY requirements.txt /tmp/requirements.txt
RUN python3 -m pip install -r /tmp/requirements.txt
ADD main.py .
CMD ["python3", "./main.py"]
