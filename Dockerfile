FROM python:3.8.13-slim-buster

RUN mkdir -p /app
COPY . main.py /app/
WORKDIR /app
RUN pip install -r requirements.txt
RUN python -m textblob.download_corpora
EXPOSE 8080
CMD [ "main.py" ]
<<<<<<< HEAD
ENTRYPOINT [ "python" ]
=======
ENTRYPOINT [ "python"]
>>>>>>> 5f9547ea324508f256dd38e50e6fc3520d060bc6
