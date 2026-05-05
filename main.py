import telebot
import threading
from kivy.app import App
from kivy.uix.label import Label

# আপনার তথ্য (টোকেন ও আইডি বসানো আছে)
BOT_1_TOKEN = "8716634550:AAHZv-G0WYziV4DAysOFwA6IzmfEkttprsY"
ID_1 = "7577845841"

# ২য় বটের তথ্য (আপাতত ১ম বটেরটিই দিয়ে রাখলাম, পরে এডিট করতে পারবেন)
BOT_2_TOKEN = "8716634550:AAHZv-G0WYziV4DAysOFwA6IzmfEkttprsY"
ID_2 = "7577845841"

bot1 = telebot.TeleBot(BOT_1_TOKEN)
bot2 = telebot.TeleBot(BOT_2_TOKEN)

class DualBotApp(App):
    def build(self):
        threading.Thread(target=self.run_bot1, daemon=True).start()
        threading.Thread(target=self.run_bot2, daemon=True).start()
        return Label(text="System Initializing...")

    def run_bot1(self):
        try:
            bot1.send_message(ID_1, "🛰️ Bot 1: Online")
            bot1.infinity_polling()
        except: pass

    def run_bot2(self):
        try:
            bot2.send_message(ID_2, "🛰️ Bot 2: Online")
            bot2.infinity_polling()
        except: pass

if __name__ == "__main__":
    DualBotApp().run()
