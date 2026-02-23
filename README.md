# AgriBazaar AI Backend

A FastAPI-based backend service for the AgriBazaar AI platform, designed to provide APIs for agricultural services including email notifications.

## Features

- **Email Service**: Send emails with customizable subject and message content
- **CORS Support**: Cross-origin resource sharing enabled for all domains
- **Interactive API Documentation**: Auto-generated Swagger UI and ReDoc documentation
- **Environment Configuration**: Easy configuration using `.env` file

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)
- Virtual environment (recommended)

## Installation

### 1. Clone or navigate to the project directory
```bash
cd agribazaar-ai-backend
```

### 2. Create and activate virtual environment (recommended)
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

## Configuration

### Environment Variables

Create a `.env` file in the root directory with the following variables:

```env
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your-email@gmail.com
SMTP_PASSWORD=your-app-password
```

**Note**: For Gmail, use an [App Password](https://support.google.com/accounts/answer/185833) instead of your regular password.

## Running the Application

Start the FastAPI server:

```bash
python run.py
```

The application will be available at:
- **API Base URL**: `http://localhost:8000`
- **Swagger UI**: `http://localhost:8000/api/docs`
- **ReDoc**: `http://localhost:8000/api/redoc`

## Project Structure

```
agribazaar-ai-backend/
├── app.py                          # FastAPI application setup
├── run.py                          # Application entry point
├── requirements.txt                # Python dependencies
├── .env                           # Environment configuration (not versioned)
│
├── apis/                          # API route controllers
│   ├── __init__.py
│   ├── send_email_controller.py   # Email sending endpoints
│  
│
├── models/                        # Pydantic data models
│   ├── __init__.py
│   ├── notification.py            # Email request models
│  
│
└── service/                       # Business logic services
    ├── __init__.py
    └── email_service.py           # Email sending service
```

## API Endpoints

### Email Service

#### Send Email
- **Endpoint**: `POST /api/email/send`
- **Description**: Send an email to a specified recipient
- **Request Body**:
  ```json
  {
    "to": "recipient@example.com",
    "subject": "Email Subject",
    "message": "Email message content in HTML"
  }
  ```
- **Response**:
  ```json
  {
    "message": "Email sent successfully"
  }
  ```
- **Error Response** (HTTP 500):
  ```json
  {
    "detail": "Error sending email"
  }
  ```





### Using Postman

1. Set request type to **POST**
2. Enter URL: `http://localhost:8000/api/email/send`
3. Go to **Body** tab and select **raw** -> **JSON**
4. Paste the JSON payload:
   ```json
   {
     "to": "recipient@example.com",
     "subject": "Email Subject",
     "message": "Email message"
   }
   ```
5. Click **Send**

## Dependencies

- **FastAPI**: Modern web framework for building APIs
- **Uvicorn**: ASGI web server for running FastAPI
- **python-dotenv**: Environment variable management
- **requests**: HTTP library for making requests


## Development

## License

This project is part of the AgriBazaar AI initiative.


