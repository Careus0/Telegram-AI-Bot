#!/bin/bash

echo "Mulai proses deployment bot Telegram..."

# Bangun image docker
docker-compose build

# Jalankan container dengan Docker Compose
docker-compose up -d

echo "Bot Telegram berhasil dideploy dan berjalan dengan Docker!"
