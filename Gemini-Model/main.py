import google.generativeai as genai
import api  

api_keyai = api.API_KEY

genai.configure(api_key=api_keyai) # get your api key from "https://aistudio.google.com/app/api-keys" and set it here

model = genai.GenerativeModel("gemini-2.0-flash")
chat = model.start_chat()

print ("Welcome to the Quiz AI-GOOGLE! Type 'exit' to quit.")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    response = chat.send_message(user_input)
    print("\n")
    print("AI:", response.text)

 