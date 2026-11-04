FROM python:3.11-slim

WORKDIR ./app

COPY . .

CMD ["python", "zoo_manager.py"]