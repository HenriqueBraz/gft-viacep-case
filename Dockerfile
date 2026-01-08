FROM python:3.11-slim

# Evita arquivos .pyc e força stdout direto (logs aparecem imediatamente)
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /gft-viacep-case
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENV PYTHONPATH=/gft-viacep-case
ENV USE_MOCK_VIACEP=true
CMD ["python", "app/main.py"]
