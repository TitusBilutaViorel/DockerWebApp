FROM python:3.10.12 as builder

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN rm requirements.txt

FROM builder

WORKDIR /app

COPY --from=builder /app /app

EXPOSE 5000

CMD ["python", "webapp.py"]
