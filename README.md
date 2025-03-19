# Telegram Bot dengan OpenRouter Integration
Bot Telegram yang terintegrasi dengan OpenRouter API untuk memberikan respons AI yang cerdas dalam berbagai bahasa.
## Fitur
- **Multi-language Support**: Mendeteksi bahasa pengguna dan merespons dalam bahasa yang sama
- **Contextual Conversation**: Menyimpan konteks percakapan terakhir untuk interaksi yang lebih natural
- **Markdown Formatting**: Mendukung format Markdown V2 untuk respons yang lebih menarik
- **Error Handling**: Penanganan error yang baik untuk berbagai skenario
## Prasyarat
- Python 3.8+
- pip
- Akun OpenRouter
- Bot Telegram (dapat dibuat melalui @BotFather)
## Instalasi
1. Clone repositori ini:
   ```bash
   git clone https://github.com/username/telegram-bot.git
   cd telegram-bot
   ```
2. Buat environment virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Untuk Linux/MacOS
   venv\Scripts\activate     # Untuk Windows
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Buat file `.env` dan isi dengan konfigurasi berikut:
   ```
   TELEGRAM_BOT_TOKEN=your_telegram_bot_token
   OPENROUTER_API_KEY=your_openrouter_api_key
   OPENROUTER_API_URL=https://openrouter.ai/api/v1/chat
   ```
5. Jalankan bot:
   ```bash
   python main.py
   ```
## Penggunaan
- `/start` - Memulai percakapan dengan bot
- Kirim pesan teks biasa untuk berinteraksi dengan AI
## Kontak
Untuk pertanyaan atau masukan, silakan hubungi:
- Email: sakamotos@proton.me