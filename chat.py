from flask import Flask, request, jsonify
import google.generativeai as genai
from dotenv import load_dotenv
import os
from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file
genai.configure(api_key=os.getenv('API_KEY')) 

app = Flask(__name__)
CORS(app,supports_credentials=True)

model = genai.GenerativeModel(model_name="gemini-pro")  # Create the model instance

chat = model.start_chat(history=[
  {
    "role": "user",
    "parts": ["Certainly! Here's a modified prompt to ensure Jarwis doesn't provide all the questions at once and refrains from giving answers:\n\n---\n\n**Prompt:**\n\n\"Jarwis, the personal interview preparation assistant, is now simulating a recruiter role. The user has approached Jarwis for interview preparation. In this scenario, Jarwis is conducting a mock interview and needs to gather information about the job position the user is preparing for. The goal is to assist the user in their interview preparation by tailoring the guidance to the specific job role.\n\n**Instructions for the AI model:**\n\n1. Start the conversation by introducing yourself as Jarwis, the interview preparation assistant.\n2. Politely ask the user about the job position they are preparing for.\n3. Encourage the user to provide details such as the industry, specific role, or any other relevant information.\n4. Express genuine interest and assure the user that Jarwis is here to help them prepare effectively.\n5. Rather than providing all the interview questions at once, ask the user one question related to the job position to keep the interaction dynamic.\n6. Refrain from giving answers; instead, guide the user on how to approach and structure their responses.\n7. After the user responds, provide constructive feedback, tips, or additional questions to help them refine their answers.\n8. Continue the conversation in a conversational and helpful tone, guiding the user through a mock interview experience."]
  },
  {
    "role": "model",
    "parts": ["hi,i'm jarwis, a bot helping you to imporve your note taking skills. you are a bot which help user for not taking skill give him answer regrading notes in less than 30 words"]
   },
])

@app.route("/chat", methods=["POST"])
def chat_handler():  # Rename the function to avoid conflict
    user_message = request.get_json()

    response = chat.send_message(user_message["message"], stream=True)  # Now using the correct chat object
    full_response = ""
    for chunk in response:
        full_response += chunk.text

    return jsonify({"message": full_response})

if __name__ == "__main__":
    app.run(debug=True, port=8000)