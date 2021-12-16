"""A simple flask web app"""
# pylint: disable=(no-name-in-module)
# pylint: disable=(import-error)
from flask import Flask, render_template
from werkzeug.debug import DebuggedApplication
from app.controllers.calculator_controller import CalculatorController
from app.controllers.index_controller import IndexController
from app.controllers.history_controller import HistoryController

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.wsgi_app = DebuggedApplication(app.wsgi_app, True)

@app.route("/", methods=['GET'])
def index_get():
    """R"""
    return IndexController.get()


@app.route("/calculator", methods=['GET'])
def calculator_get():
    """R"""
    return CalculatorController.get()


@app.route("/calculator", methods=['POST'])
def calculator_post():
    """R"""
    return CalculatorController.post()

@app.route("/history", methods=['GET'])
def table_get():
    """R"""
    return HistoryController.get()

@app.route("/page1")
def page1():
    """A simple flask web app"""
    return render_template('page1.html')


@app.route("/page2")
def page2():
    """A simple flask web app"""
    return render_template('page2.html')


@app.route("/page3")
def page3():
    """A simple flask web app"""
    return render_template('page3.html')


@app.route("/page4")
def page4():
    """A simple flask web app"""
    return render_template('page4.html')
