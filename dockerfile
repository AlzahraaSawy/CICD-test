from python:3.9-slim
WORKDIR /CICD
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "ETL.py"]