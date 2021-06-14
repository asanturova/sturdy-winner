from flask import Flask, url_for,  render_template, request
from flask_mail import Mail, Message
app=Flask(__name__)


app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_DEBUG'] = True
app.config['MAIL_USERNAME'] = 'butterisflying21@gmail.com'
app.config['MAIL_PASSWORD'] = '21flyingisbutter'
app.config['MAIL_DEFAULT_SENDER'] = 'Visitor from Heroku-website','butterisflying@gmail.com'


mail = Mail(app)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/work/')
def work():
    return render_template("work.html")

@app.route('/contact/', methods=['GET','POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        msg = Message(
            subject=f"Mail from {name}", 
            body=f"Name: {name}\nE-Mail: {email}\nMessage:\n\n{message}", 
            recipients = ['asanturovaaidanai@gmail.com'])
        mail.send(msg)
        return render_template("contact.html", success=True)
    
    return render_template("contact.html")
    
if __name__ == "__main__":
    app.run(debug=True)