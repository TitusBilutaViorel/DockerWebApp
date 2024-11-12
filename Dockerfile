#2. build
FROM python:3.10.12

#seteaza director de lucru în container
WORKDIR /app

#copiaza fisierele aplicatiei în container
COPY . /app

RUN pip install -r requirements.txt

EXPOSE 5000

#rulează aplicatia
CMD ["python", "webapp.py"]
