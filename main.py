"""
WhatsApp Health Chatbot - Hackathon Demo

This chatbot simulates a basic WhatsApp-like interaction to help users in Tier 3 cities
access affordable and understandable health services from home.

How it works:
1. User sends symptoms through a simple message (text input).
2. Chatbot analyzes and provides basic guidance.
3. If necessary, it offers free/low-cost home sample collection (blood, urine, etc.).
4. Reports are explained simply with health tips.

Run using: python main.py
"""

def chatbot_response(user_input):
    user_input = user_input.lower()
    
    if "fever" in user_input or "cold" in user_input or "cough" in user_input:
        return ("It seems like you're experiencing common symptoms.\n"
                "Please rest, drink warm fluids, and monitor your temperature.\n"
                "Would you like to schedule a free home test?")
    
    elif "yes" in user_input or "test" in user_input:
        return ("Great! A testing agent will visit your home soon to collect samples "
                "(blood, urine, BP, sugar, etc.).\n"
                "You'll receive your report on WhatsApp with clear explanations.")
    
    elif "report" in user_input or "result" in user_input:
        return ("Here’s your test report:\n- Sugar: Normal\n- BP: Slightly High\n"
                "Recommendation: Reduce salt, daily 30-min walk, stay hydrated.\n"
                "Would you like a follow-up in a week?")
    
    elif "thank" in user_input:
        return ("You're welcome! I'm always here to help with your health. Stay safe!")
    
    else:
        return ("Hi! I’m your HealthBot.\nPlease share your symptoms or upload a photo of a report.\n"
                "I’ll guide you with care in your preferred language.")

if __name__ == "__main__":
    print("Welcome to HealthBot (Hackathon Demo)")
    print("Type 'exit' to end the chat.")
    
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() == "exit":
            print("HealthBot: Take care! Goodbye.")
            break
        response = chatbot_response(user_input)
        print(f"HealthBot: {response}")
