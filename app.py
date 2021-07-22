from flask import Flask, render_template, request
from wtforms import StringField, SubmitField, IntegerField
from wtforms.form import Form

app = Flask(__name__)

app.config['SECRET_KEY']