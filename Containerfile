FROM python:3.13.9-alpine

WORKDIR /app

COPY banner.py .

RUN chmod +x banner.py

EXPOSE 8080

CMD ["python3", "banner.py"]
