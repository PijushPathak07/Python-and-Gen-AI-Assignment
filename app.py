from flask import Flask, request, jsonify
import google.generativeai as genai
from config import Config
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Configure Gemini
genai.configure(api_key=Config.GOOGLE_API_KEY)
model = genai.GenerativeModel(Config.MODEL_NAME)

def validate_input(data):
    """Validate input data"""
    if not data:
        return False, "No data provided"
    
    required_fields = ['company_name', 'transcript_text']
    for field in required_fields:
        if field not in data:
            return False, f"Missing required field: {field}"
        
    if not data['transcript_text'].strip():
        return False, "Transcript text cannot be empty"
        
    if len(data['transcript_text']) > Config.MAX_TOKENS:
        return False, f"Transcript text exceeds maximum length of {Config.MAX_TOKENS} tokens"
        
    return True, None

def generate_category_prompt(category, transcript):
    """Generate prompt for each category"""
    prompts = {
        'financial_performance': f"Analyze and summarize the key financial metrics and performance statements from this earnings call transcript. Focus on revenue, profit, growth rates, and other financial indicators. Limit response to 2-3 sentences. Transcript: {transcript}",
        'market_dynamics': f"Summarize the market trends, demand shifts, and competitive landscape discussed in this earnings call transcript. Limit response to 2-3 sentences. Transcript: {transcript}",
        'expansion_plans': f"Extract and summarize any growth or expansion plans mentioned in this earnings call transcript. Include new markets, products, or initiatives. Limit response to 2-3 sentences. Transcript: {transcript}",
        'environmental_risks': f"Identify and summarize any environmental issues, sustainability initiatives, or ESG concerns mentioned in this earnings call transcript. Limit response to 2-3 sentences. Transcript: {transcript}",
        'regulatory_or_policy_changes': f"Summarize any regulatory changes or policy updates that were discussed in this earnings call transcript and their potential impact on the company. Limit response to 2-3 sentences. Transcript: {transcript}"
    }
    return prompts.get(category)

def get_category_summary(category, transcript):
    """Get summary for a specific category using Gemini"""
    try:
        prompt = generate_category_prompt(category, transcript)
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error generating summary for {category}: {str(e)}"

@app.route('/earnings_transcript_summary', methods=['POST'])
def summarize_transcript():
    """Endpoint to summarize earnings call transcript"""
    try:
        data = request.get_json()
        
        # Validate input
        is_valid, error_message = validate_input(data)
        if not is_valid:
            return jsonify({'error': error_message}), 400
        
        # Initialize response structure
        response = {
            'company_name': data['company_name']
        }
        
        # Generate summaries for each category
        categories = ['financial_performance', 'market_dynamics', 'expansion_plans', 
                     'environmental_risks', 'regulatory_or_policy_changes']
        
        for category in categories:
            response[category] = get_category_summary(category, data['transcript_text'])
        
        return jsonify(response), 200
        
    except Exception as e:
        return jsonify({'error': f'Internal server error: {str(e)}'}), 500

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({'status': 'healthy'}), 200

if __name__ == '__main__':
    app.run(debug=True)