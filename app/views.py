from flask import request,render_template,Blueprint
from app.utils import text_to_morse,morse_to_text

morse = Blueprint("morse",__name__,template_folder="templates")

@morse.route('/')
def index():
    return render_template("morse.html")

@morse.route('/convert', methods=['POST'])
def convert():
    text = request.form.get('text', '')
    result = text_to_morse(text)
    return render_template("morse.html", result=result)

@morse.route('/decode', methods=['POST'])
def decode():
    morse_code = request.form.get('morse', '')
    result = morse_to_text(morse_code)
    return render_template("morse.html", result=result)