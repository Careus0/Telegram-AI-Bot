#!/bin/bash

echo "Merestart bot Telegram..."

# Restart container tanpa rebuild
docker-compose restart

echo "Bot Telegram berhasil direstart!"
