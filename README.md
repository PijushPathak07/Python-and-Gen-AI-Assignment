# Python-and-Gen-AI-Assignment
I have developed a RESTful API using Flask. It can summarize earnings call transcripts for companies using Gemini 1.5 Flash. The API acceptS a company transcript in JSON format and return a structured  summary with specific categories.

# Earnings Call Transcript Summary API Documentation

## API Base URL
```
https://YOUR_USERNAME.pythonanywhere.com
```

## Authentication
No authentication required for demo purposes. In production, implement API key authentication.

## Endpoints

### 1. Health Check
- **URL:** `/health`
- **Method:** GET
- **Response:**
```json
{
    "status": "healthy"
}
```

### 2. Earnings Transcript Summary
- **URL:** `/earnings_transcript_summary`
- **Method:** POST
- **Headers:** 
  - Content-Type: application/json
- **Request Body:**
```json
{
    "company_name": "Company Name",
    "transcript_text": "Earnings call transcript..."
}
```
- **Response:**
```json
{
    "company_name": "Company Name",
    "financial_performance": "Summary...",
    "market_dynamics": "Summary...",
    "expansion_plans": "Summary...",
    "environmental_risks": "Summary...",
    "regulatory_or_policy_changes": "Summary..."
}
```

## Error Responses
- **400 Bad Request:** Invalid input data
- **500 Internal Server Error:** Server processing error

## Rate Limits
- Free tier limitations apply
- Maximum transcript length: 20,000 tokens

## Example Usage
```python
import requests

url = "https://YOUR_USERNAME.pythonanywhere.com/earnings_transcript_summary"
data = {
    "company_name": "Test Company",
    "transcript_text": "Your transcript text here..."
}

response = requests.post(url, json=data)
print(response.json())
```

## Source Code
The complete source code is available at: [GitHub Repository URL]

## Deployment
The API is deployed on PythonAnywhere. For local development:
1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Set up environment variables in `.env`
4. Run: `python app.py`
