
FROM python:3.6
WORKDIR /app
ADD . /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["Main/bakend.py"]