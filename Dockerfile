# Gunakan image Python terbaru
FROM python:3.12.3

# Set working directory
WORKDIR /app

# Salin semua file ke dalam container
COPY . .

# Install dependencies dari requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Jalankan bot
CMD ["python", "main.py"]
