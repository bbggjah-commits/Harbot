from flask import Flask
import requests
import time
import threading
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "🤖 البوت السري يعمل 24/7 على Render! أرسل Xcvb101g إلى @Hacrbbot"

BOT_TOKEN = "8434458334:AAEwfSiu06rwBzPbe-8aRhNCpWW2F7eVll8"

def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": chat_id, "text": text, "parse_mode": "HTML"}
    try:
        requests.post(url, json=data, timeout=10)
    except:
        pass

def telegram_bot():
    print("🚀 البوت يعمل على Render...")
    last_update_id = 0
    
    while True:
        try:
            url = f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates"
            params = {"offset": last_update_id + 1, "timeout": 50}
            response = requests.get(url, params=params, timeout=60)
            
            if response.status_code == 200:
                data = response.json()
                if data.get("ok"):
                    for update in data["result"]:
                        last_update_id = update["update_id"]
                        message = update.get("message", {})
                        text = message.get("text", "")
                        chat_id = message.get("chat", {}).get("id")
                        user_name = message.get("from", {}).get("first_name", "صديقي")
                        
                        if text == "/start":
                            welcome = f"🎮 <b>مرحباً {user_name}!</b>\n\n🔐 اكتب <code>Xcvb101g</code> للقائمة السرية\n🌐 يعمل 24/7 على Render"
                            send_message(chat_id, welcome)
                        
                        elif text == "Xcvb101g":
                            menu = f"""
🔐 <b>القائمة السرية لـ {user_name}</b> 🎯

📁 <b>البرامج الآمنة:</b>
• 🛡️ برنامج الحماية
• ⚡ أداة التحسين  
• 📁 مدير الملفات

⚡ <b>سكربتات Roblox:</b>
• 🎮 سكربت الواجهة
• 🚀 سكربت الحركة
• ⚙️ سكربت الأدوات

✅ <b>البوت يعمل 24/7 على Render!</b>
                            """
                            send_message(chat_id, menu)
            
            time.sleep(3)
        except Exception as e:
            print(f"خطأ: {e}")
            time.sleep(10)

if __name__ == "__main__":
    bot_thread = threading.Thread(target=telegram_bot)
    bot_thread.daemon = True
    bot_thread.start()
    
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
