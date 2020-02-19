FROM python:3

EXPOSE 3000
WORKDIR /app
COPY . .
RUN pip3 install -r requirements.txt
CMD ["python", "main.py"]