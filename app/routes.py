
from datetime import date

from app.summarizer import summarizer

from flask import render_template, url_for, redirect, request, flash, abort
from app import app

# from app.forms import RegistrationForm, LoginForm, MedicineForm
# from app.models import User, Medicines, Data


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/summarize", methods=['GET', 'POST'])
def summarize():
    if request.method == 'POST':
        raw_text = request.form['raw_text']
        summarized_text = summarizer(raw_text)

    return render_template('index.html', summarized_text=summarized_text, raw_text=raw_text)


