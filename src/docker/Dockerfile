FROM python:3.14-slim-trixie

COPY ./src/ ./

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "main.py"]