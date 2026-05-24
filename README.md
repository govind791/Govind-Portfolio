# Portfolio

## Features

- Responsive portfolio pages (Home, Projects, Skills, Education, Experience)
- Contact form with email functionality
- AI-powered chat feature using Google Gemini API
- Modular architecture with Flask Blueprints

## Project Structure

```
portfolio/
├── app/
│   ├── __init__.py          # Flask app factory
│   ├── config.py            # Configuration settings
│   ├── forms.py             # WTForms for contact form
│   ├── utils.py             # Utility functions (AI chat logic)
│   └── routes/
│       ├── main.py          # Main portfolio routes
│       ├── contact.py       # Contact form routes
│       └── chat.py          # AI chat routes
├── templates/               # Jinja2 templates
├── static/                  # CSS, JS, images
├── main.py                  # Application entry point
├── requirements.txt         # Python dependencies
├── pyproject.toml           # Project metadata
└── some_information.txt     # Personal info for AI chat
```

## Setup

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
2. Set up environment variables in a `.env` file:

   ```
   GEMINI_API_KEY=your_gemini_api_key
   SESSION_SECRET=your_secret_key
   MAIL_USERNAME=your_email@gmail.com
   MAIL_PASSWORD=your_email_password
   MAIL_DEFAULT_SENDER=your_email@gmail.com
   ```
3. Run the application:

   ```bash
   python main.py
   ```

The app will run on `http://localhost:8080`.

## Deployment
