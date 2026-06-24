from flask import Flask

app=Flask(__name__)
def home():
    return '<p>Dit is huiswerk voor les 11.</p>'
