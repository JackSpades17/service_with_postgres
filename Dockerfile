FROM python:3

WORKDIR /opt/app
COPY requirements.txt .
COPY app.py .
RUN pip3 install -r /opt/app/requirements.txt
EXPOSE 1717
CMD python3 ./app.py