from flask import Flask, render_template
from flask_mail import Mail
import logging

mail = Mail()

def create_app():
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    app.config.from_object('app.config.Config')

    # Initialize extensions
    mail.init_app(app)

    # Configure logging
    logging.basicConfig(level=logging.DEBUG)

    # Register blueprints (Notice: chat is gone!)
    from app.routes.main import main
    from app.routes.contact import contact_bp

    app.register_blueprint(main)
    app.register_blueprint(contact_bp)

    # Error handlers
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html'), 404

    @app.errorhandler(500)
    def server_error(e):
        return render_template('500.html'), 500

    return app