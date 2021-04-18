# Import some packages
from flask import Flask, render_template, request
from flask_mail import Mail, Message
from forms import ContactForm


# Define flask app
app = Flask(__name__)
app.secret_key = 'dev fao football app'

# Define mail app
mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": 'pruebasolucionestecnologicas@gmail.com',
    "MAIL_PASSWORD": 'rarjdjdfkjdlneym'
}
app.config.update(mail_settings)
mail = Mail(app)

# define sendMail()


def sendMail(mailName, mailMail, mailSubject, mailMessaje):
    if __name__ == '__main__':
        with app.app_context():
            msg = Message(subject=f"Contacto Flask_Mail {mailSubject}",
                          sender=app.config.get("MAIL_USERNAME"),
                          recipients=["brunomleguizamon@gmail.com"],
                          body=f"Mail subject: {mailSubject}. Alquien Quiere contactarse contigo: {mailName} , su email es: {mailMail}, su mensaje es: {mailMessaje}")
            mail.send(msg)
    return "mail enviado"

# Render error page


@app.errorhandler(404)
def not_found(error):
    return "Not Found."

# Render Contact page


@app.route('/', methods=["GET", "POST"])
def get_contact():
    form = ContactForm()
    if request.method == 'POST':
        name = request.form["name"]
        email = request.form["email"]
        subject = request.form["subject"]
        message = request.form["message"]
        sendMail(name, email, subject, message)
        return render_template('returnhome.html', form=form)
    else:
        return render_template('contact.html', form=form)


# Run app
if __name__ == '__main__':
    app.run(port=5000, debug=True)
