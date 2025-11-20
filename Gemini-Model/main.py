import google.generativeai as genai
import api

api_keyai = api.API_KEY

genai.configure(api_key=api_keyai)

model = genai.GenerativeModel("gemini-2.5-flash")
chat = model.start_chat()

print("=== TERMINAL BASED - GOOGLE GEMINI 2.5 FLASH ===")
print("Type 'exit' to quit\n")

while True:
    user_input = input("You: ")
    print("\n")
    
    if user_input.lower() == "exit":
        print("Goodbye!")
        break
    
    if not user_input.strip():
        print("Please enter a message!\n")
        continue
    
    try:
        response = chat.send_message(user_input)
        print(f"AI: {response.text}\n")
    except Exception as e:
        print(f"Error: {str(e)}\n")

