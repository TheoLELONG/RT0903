FROM python:3.9

WORKDIR /app

COPY . .

RUN pip install flask

ENV MESSAGE "Bip bip boup boup"
ENV APP_PORT 8080

EXPOSE 8080

CMD ["python3", "motd_api.py"]
