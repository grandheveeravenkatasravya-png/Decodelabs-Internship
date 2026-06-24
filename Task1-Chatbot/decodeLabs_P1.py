from PIL import Image
from datetime import datetime

while True:
    user = input("👤 You: ").lower().strip()

    # Exit
    if user == "exit":
        print("🤖 Bot: Goodbye 👋")
        print("🤖 Bot: Keep learning and keep growing 🚀")
        break

    # ---------------- GREETINGS ----------------
    elif user in ["hi", "hello", "hey"]:
        print("🤖 Bot: Hey there! 😊")
        print("🤖 Bot: I'm really happy to talk with you!")
        print("🤖 Bot: What would you like to explore today?")

    elif "how are you" in user:
        print("🤖 Bot: I'm doing great 😄")
        print("🤖 Bot: Talking with you makes it even better!")

    elif "good morning" in user:
        print("🤖 Bot: Good morning 🌅")
        print("🤖 Bot: Start your day with confidence 💪")

    elif "good night" in user:
        print("🤖 Bot: Good night 🌙")
        print("🤖 Bot: Rest well and recharge!")

    # ---------------- GENERAL CHAT ----------------
    elif "what are you doing" in user:
        print("🤖 Bot: I'm chatting with you 😄")
        print("🤖 Bot: And I enjoy it!")

    elif "are you real" in user:
        print("🤖 Bot: I'm not human 😅")
        print("🤖 Bot: But I try to talk like one!")

    elif "bored" in user:
        print("🤖 Bot: Feeling bored? 😴")
        print("🤖 Bot: Try learning something new or watch a movie 🎬")

    # ---------------- HISTORY ----------------
    elif "independence day" in user:
        print("🤖 Bot: 🇮🇳 Independence Day is August 15")
        print("🤖 Bot: India got freedom in 1947 🎉")

    elif "gandhi" in user:
        print("🤖 Bot: Mahatma Gandhi believed in non-violence ✨")
        print("🤖 Bot: He inspired millions!")

    # ---------------- ECONOMICS ----------------
    elif "inflation" in user:
        print("🤖 Bot: Inflation means prices increase 📈")
        print("🤖 Bot: Things become more expensive over time 💰")

    elif "gdp" in user:
        print("🤖 Bot: GDP shows economic growth 🌍")
        print("🤖 Bot: It measures total production 📊")

    # ---------------- EXAMS ----------------
    elif "upsc" in user:
        print("🤖 Bot: UPSC is one of the toughest exams 💪")
        print("🤖 Bot: Requires consistency and focus 📖")

    elif "ssc" in user:
        print("🤖 Bot: SSC exams are for government jobs 📚")

    elif "preparation" in user:
        print("🤖 Bot: Study daily 📖")
        print("🤖 Bot: Practice and revise regularly 🧠")

    elif "how to study" in user:
        print("🤖 Bot: Understand concepts clearly 🧠")
        print("🤖 Bot: Practice regularly and revise!")

    elif "exam fear" in user:
        print("🤖 Bot: Fear is normal 😌")
        print("🤖 Bot: Preparation reduces fear 💯")

    # ---------------- AI ----------------
    elif "who invented ai" in user:
        print("🤖 Bot: AI was introduced by John McCarthy in 1956 🧠")
        print("🤖 Bot: He is called father of AI!")

    elif "when was ai invented" in user:
        print("🤖 Bot: AI started in 1956 at Dartmouth Conference 📅")

    elif "ai" in user:
        print("🤖 Bot: AI makes machines intelligent 🤖")
        print("🤖 Bot: It helps computers learn and think 🧠")

    elif "future of ai" in user:
        print("🤖 Bot: AI will shape the future 🚀")
        print("🤖 Bot: It will change many industries!")

    elif "chatbot" in user:
        print("🤖 Bot: Chatbot talks with users 💬")
        print("🤖 Bot: Just like me talking to you 😄")

    # ---------------- MOTIVATION ----------------
    elif "motivate" in user:
        print("🤖 Bot: You are stronger than you think 💪🔥")
        print("🤖 Bot: Keep going!")

    elif "failure" in user:
        print("🤖 Bot: Failure is a step to success 🚀")
        print("🤖 Bot: Learn and grow!")

    elif "success" in user:
        print("🤖 Bot: Success comes with hard work ⭐")

    elif "goal" in user:
        print("🤖 Bot: Set clear goals 🎯")
        print("🤖 Bot: Work on them daily!")

    elif "tired" in user:
        print("🤖 Bot: Take rest 😴")
        print("🤖 Bot: Come back stronger 💪")

    # ---------------- FUN ----------------
    elif "joke" in user:
        print("🤖 Bot: 😂 Why did the computer go to school?")
        print("🤖 Bot: To improve its memory! 🤣")

    elif "fun fact" in user:
        print("🤖 Bot: 🤯 First computer was huge and heavy!")

    # ---------------- GENERAL ----------------
    elif "time" in user:
        now = datetime.now()
        print("🤖 Bot: ⏰ Time:", now.strftime("%H:%M:%S"))

    elif "date" in user:
        today = datetime.now()
        print("🤖 Bot: 📅 Date:", today.strftime("%d-%m-%Y"))

    # ---------------- IMAGE ----------------
    elif "upload" in user:
        path = input("📂 Enter image path: ")
        try:
            img = Image.open(path)
            print("🤖 Bot: 🖼️ Image loaded successfully!")
            print("🤖 Bot: Size:", img.size)
            print("🤖 Bot: Nice image 😄")
        except:
            print("🤖 Bot: ❌ Couldn't open image")

    # ---------------- HELP ----------------
    
 
    elif "help" in user:
        print("🤖 Bot: Try keywords like → history, gdp, upsc, ai, motivate, joke, upload, time")
        print("----------------------------------------------------------------------------------")
        print("🤖 Bot: Or ask naturally like → 'who invented ai', 'independence day', etc.")

    # Default
    else:
        print("🤖 Bot: Hmm 🤔 I didn’t get that.")
        print("👉 Try 'help' to see commands or 'exit' to quit")
