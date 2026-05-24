from flask import Blueprint, request, jsonify, current_app
from app.utils import is_relevant, personal_info
import requests

chat_bp = Blueprint('chat', __name__)

@chat_bp.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        user_message = data.get('message', '').strip()
        
        if not user_message:
            return jsonify({'response': 'Please enter a message.'})
        
        # Check if question is relevant
        if not is_relevant(user_message, personal_info):
            return jsonify({'response': 'Sorry, this is not related to my information. Please ask something about me.'})
        
        # Prepare request for Gemini API
        headers = {"Content-Type": "application/json"}
        data = {
            "contents": [{
                "parts": [{
                    "text": f"Based on the following personal information, answer the question:\n\n{personal_info}\n\nUser Question: {user_message}"
                }]
            }]
        }
        
        # Send request to Gemini API
        response = requests.post(current_app.config['GEMINI_URL'], headers=headers, json=data)
        
        if response.status_code == 200:
            response_data = response.json()
            try:
                answer = response_data["candidates"][0]["content"]["parts"][0]["text"]
                return jsonify({'response': answer})
            except KeyError:
                return jsonify({'response': 'Sorry, I couldn\'t generate a response.'})
        else:
            return jsonify({'response': 'Error! Please try again later.'})
            
    except Exception as e:
        current_app.logger.error(f"Chat error: {e}")
        return jsonify({'response': 'Sorry, an error occurred. Please try again later.'})