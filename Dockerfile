FROM python:3.10-slim

WORKDIR /app

# Install build tools required for tgcrypto
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    make \
    && rm -rf /var/lib/apt/lists/*

# Install python deps first (cache-friendly)
COPY requirements.txt .
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Copy app source
COPY . .

CMD ["bash", "start"]
