# Python-and-Gen-AI-Assignment
I have developed a RESTful API using Flask. It can summarize earnings call transcripts for companies using Gemini 1.5 Flash. The API acceptS a company transcript in JSON format and return a structured  summary with specific categories.

# Earnings Call Transcript Summary API Documentation

## Hosted API
You can access the hosted API here: [PYTHON-ANYWHERE-LINK](https://piijush.pythonanywhere.com/)

## Authentication
No authentication required for demo purposes. In production, implement API key authentication.

# Earnings Call Transcript Summary API Documentation

## 1. API Endpoints

The API exposes two endpoints:

### 1.1. Earnings Transcript Summary
**Endpoint:** `/earnings_transcript_summary`
**Method:** POST

This is the main endpoint responsible for summarizing the earnings call transcript.

#### Request Format
The request body should be a JSON object with the following fields:
```json
{
    "company_name": "Reliance Industries",
    "transcript_text": "Full transcript text here..."
}
```
- `company_name`: The name of the company (string).
- `transcript_text`: The full text of the earnings call transcript (string, maximum 20,000 tokens).

#### Response Format
The response will be a JSON object with the following structure:
```json
{
    "company_name": "Reliance Industries",
    "financial_performance": "Summary of financial metrics...",
    "market_dynamics": "Summary of market trends...",
    "expansion_plans": "Summary of growth plans...",
    "environmental_risks": "Summary of environmental concerns...",
    "regulatory_or_policy_changes": "Summary of regulatory updates..."
}
```
- `company_name`: The name of the company.
- `financial_performance`: A summary of the company's financial performance, including key metrics and statements.
- `market_dynamics`: A summary of the market trends, demand shifts, and competitive landscape discussed in the transcript.
- `expansion_plans`: A summary of any growth or expansion plans mentioned in the transcript, such as new markets, products, or initiatives.
- `environmental_risks`: A summary of any environmental issues, sustainability initiatives, or ESG concerns discussed in the transcript.
- `regulatory_or_policy_changes`: A summary of any regulatory changes or policy updates mentioned in the transcript and their potential impact on the company.

### 1.2. Health Check
**Endpoint:** `/health`
**Method:** GET

This endpoint can be used to check the health status of the API.

#### Response Format
The response will be a JSON object with the following structure:
```json
{
    "status": "healthy"
}
```

## 2. Request/Response Formats

The API expects and returns data in JSON format. The request body should be a valid JSON object with the required fields, as specified in the endpoint descriptions.

## 3. Error Handling

The API includes comprehensive error handling for various scenarios:

- **400 Bad Request**: This error will be returned if the input data is invalid, such as missing required fields or empty transcript text.
- **500 Internal Server Error**: This error will be returned if there is an issue with the server-side processing, such as an exception during the summarization process.

In case of an error, the response will include a JSON object with an `error` field containing a descriptive error message.

## 4. Setup Instructions

To set up the API locally, follow these steps:

1. Clone the repository and navigate to the project directory.
2. Create a virtual environment and activate it.
3. Install the required dependencies from the `requirements.txt` file.
4. Set up the environment variables, including the Google API key, in a `.env` file.
5. Run the Flask application using the provided `app.py` file.

Detailed instructions, including directory structure, virtual environment setup, and testing procedures, are available in the `setup-instructions` artifact.

## 5. Testing Guidelines

The project includes a comprehensive test script (`test_api.py`) that can be used to validate the API's functionality. The test script covers the following:

- Testing the health check endpoint
- Sending a sample request to the main API endpoint
- Handling various error scenarios

You can run the test script to ensure the API is working as expected. Detailed instructions for running the tests are provided in the `setup-instructions` artifact.

## 6. Deployment Information

The API is deployed to hosting platform - PythonAnywhere. 

## Rate Limits
- Free tier limitations apply
- Maximum transcript length: 20,000 tokens

## Source Code
The complete source code is available at: [GitHub Repository URL](https://github.com/PijushPathak07/Python_and_Gen-AI)

The codebase includes the following files:
1.	app.py: The main Flask application that defines the API endpoints and handles the request/response logic.
2.	config.py: The configuration file that manages environment variables, such as the Google API key.
3.	test_api.py: A script for testing the API endpoints locally.
4.	requirements.txt: The list of Python dependencies required to run the application.
5.	templates/index.html: Web interface for testing the API.

## Deployment
The API is deployed on PythonAnywhere. For local development:
1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Set up environment variables in `.env`
4. Run: `python app.py`
