FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0"]
# Modified 2025-06-13
# Modified 2025-07-21
# Modified 2023-02-03
# Modified 2023-04-10
# Modified 2023-05-25
# Modified 2023-08-06
