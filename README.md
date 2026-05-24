# Portfolio

## Features

- **Responsive Design:** Fully responsive pages (Home, Projects, Skills, Education, Experience) optimized for both desktop and mobile.
- **Contact Form Integration:** Functional contact form with live email routing powered by `Flask-Mail`.
- **Modular Architecture:** Built using Flask Blueprints for clean routing, scalability, and separation of concerns.
- **Smooth Animations:** Integrated with AOS (Animate On Scroll) for dynamic UI interactions as users scroll.
- **Production Ready:** Fully containerized with a `Dockerfile` and dynamic port configuration for seamless deployment to platforms like Render or Railway.

## Project Structure
```text
Govind-Portfolio/
├── app/
│   ├── __init__.py          # Flask app factory & blueprint registration
│   ├── config.py            # Configuration settings
│   ├── forms.py             # WTForms for the contact form
│   └── routes/
│       ├── main.py          # Main portfolio UI routes
│       └── contact.py       # Contact form and email logic
├── templates/               # Jinja2 HTML templates
├── static/                  # CSS, JS, and image assets
├── main.py                  # Application entry point
├── requirements.txt         # Python dependencies
├── Dockerfile               # Containerization instructions
└── .gitignore               # Git ignore rules

## Setup

1. Create and activate a virtual environment (Recommended):
   ```bash
   python -m venv .venv
   # On Windows:
   .venv\Scripts\activate
   # On Mac/Linux:
   source .venv/bin/activate
Install dependencies:

Bash
pip install -r requirements.txt
Set up environment variables in a .env file:

Code snippet
SESSION_SECRET=your_secret_key
MAIL_USERNAME=your_email@gmail.com
MAIL_PASSWORD=your_app_password
MAIL_DEFAULT_SENDER=your_email@gmail.com
PORT=5000
Run the application:

Bash
python main.py
The app will run locally at http://127.0.0.1:5000.