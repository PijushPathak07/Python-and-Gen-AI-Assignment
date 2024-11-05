# Python and Gen-AI Assignment

This project provides a RESTful API built with Flask to summarize earnings call transcripts for companies using the Gemini 1.5 Flash model. The API accepts a transcript in JSON format and returns a structured summary across specific categories.

## Table of Contents

- [Hosted API](#hosted-api)
- [API Documentation](#api-documentation)
  - [Authentication](#authentication)
  - [Endpoints](#endpoints)
  - [Request and Response Formats](#request-and-response-formats)
  - [Error Handling](#error-handling)
- [Setup Instructions](#setup-instructions)
- [Testing Guidelines](#testing-guidelines)
- [Deployment Information](#deployment-information)
- [Rate Limits](#rate-limits)
- [Source Code](#source-code)
- [Developer Contact](#developer-contact)

---

## Hosted API

Access the hosted API on PythonAnywhere: [Earnings Call Transcript Summary API](https://piijush.pythonanywhere.com/)

## API Documentation

### Authentication

No authentication is required for demo purposes. For production, consider implementing API key authentication to secure endpoints.

### Endpoints

The API provides the following endpoints:

#### 1. Earnings Transcript Summary
- **Endpoint**: `/earnings_transcript_summary`
- **Method**: POST

This endpoint generates a structured summary of an earnings call transcript.

- **Request Format**:
    ```json
    {
        "company_name": "Reliance Industries",
        "transcript_text": "Full transcript text here..."
    }
    ```
  - `company_name`: (string) The name of the company.
  - `transcript_text`: (string) Full earnings call transcript (maximum 20,000 tokens).

- **Response Format**:
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
  - The response includes summaries across categories such as financial performance, market dynamics, expansion plans, environmental risks, and regulatory changes.

#### 2. Health Check
- **Endpoint**: `/health`
- **Method**: GET

This endpoint checks the health status of the API.

- **Response Format**:
    ```json
    {
        "status": "healthy"
    }
    ```

### Request and Response Formats

The API expects and returns JSON-formatted data. Each request and response structure is defined in the endpoint descriptions above.

### Error Handling

The API has robust error handling for various scenarios:
- **400 Bad Request**: Missing or invalid input data.
- **500 Internal Server Error**: Issues with server processing, such as summarization errors.

If an error occurs, the response includes an `error` field with a description of the issue.

---

## Setup Instructions

To set up the API locally:

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/PijushPathak07/Python_and_Gen-AI
    cd Python_and_Gen-AI
    ```

2. **Create a Virtual Environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # For Linux/macOS
    venv\Scripts\activate     # For Windows
    ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set Environment Variables**:
   - Create a `.env` file in the root directory and add your API keys, e.g.:
     ```bash
     GOOGLE_API_KEY="your-google-api-key"
     ```

5. **Run the Application**:
    ```bash
    python app.py
    ```

---

## Testing Guidelines

A test script (`test_api.py`) is included for validation:

- **Health Check**: Verifies the `/health` endpoint.
- **Main Endpoint Test**: Sends a sample request to `/earnings_transcript_summary`.
- **Error Scenarios**: Tests cases like invalid data or empty fields.

Run the script using:
```bash
python test_api.py
```

---

## Deployment Information

The API is deployed on PythonAnywhere. For local development:

1. Clone the repository.
2. Install dependencies using:
   ```bash
   pip install -r requirements.txt
   ```
3. Configure environment variables in a `.env` file.
4. Start the application locally with:
   ```bash
   python app.py
   ```

---

## Rate Limits

- **Free Tier Limitations**: The hosted API is limited to demo usage.
- **Transcript Length**: Maximum length of 20,000 tokens per request.

---

## Source Code

The complete codebase is available on GitHub: [GitHub Repository](https://github.com/PijushPathak07/Python_and_Gen-AI)

### Codebase Overview

1. **app.py**: The main Flask app defining the API endpoints.
2. **config.py**: Configuration file for environment variables, such as API keys.
3. **test_api.py**: A testing script for validating endpoints.
4. **requirements.txt**: List of dependencies.
5. **templates/index.html**: A simple web interface for testing the API.

---

## Developer Contact

- **Name**: *Pijush Pathak*
- **Email**: *[pijushpathak94@gmail.com](mailto:pijushpathak94@gmail.com)*
