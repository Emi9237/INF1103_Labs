FROM python:3.14.7-slim
WORKDIR /app
COPY inventory_auditor.py .
CMD ["python", "inventory_auditor.py"]