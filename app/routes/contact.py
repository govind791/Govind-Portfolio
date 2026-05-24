from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app
from flask_mail import Message
from app.forms import ContactForm
from app import mail

contact_bp = Blueprint('contact', __name__)

@contact_bp.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if request.method == 'POST' and form.validate_on_submit():
        try:
            msg = Message(
                subject=f"Portfolio Contact: {form.subject.data}",
                recipients=["sachinkumar18449@gmail.com"],
                body=f"Name: {form.name.data}\nEmail: {form.email.data}\nMessage: {form.message.data}"
            )
            mail.send(msg)
            flash('Your message has been sent successfully!', 'success')
            return redirect(url_for('contact.contact'))
        except Exception as e:
            current_app.logger.error(f"Error sending email: {e}")
            flash('Sorry, there was an error sending your message. Please try again later.', 'danger')

    return render_template('contact.html', form=form, active='contact')