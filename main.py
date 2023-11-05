from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flask import Flask, render_template, request
from calorie import Calorie
from temperature import Temperature

app = Flask(__name__)

class HomePage(MethodView):

    def get(self):
        return render_template('index.html')
    


class FormPage(MethodView):

    def get(self):
        user_form = UserForm()
        return render_template('calories.html',
                               user_form=user_form)
    
    def post(self):
        user_form = UserForm(request.form)
        weight, height, age, country, city = [x.data for x in user_form][:-1]
        temperature = Temperature(country, city).get()
        calorie_amount = Calorie(weight, height, age, temperature).calculate()
        return render_template('calories.html',
                               user_form=user_form,
                               result = True,
                               calorie_amount=calorie_amount)
    

class UserForm(Form):
    weight = StringField('Your weight: ', default=87)
    height = StringField('Your height: ', default=175)
    age = StringField('Your age: ', default=37)
    country = StringField('Country: ', default='Russia')
    city = StringField('City: ', default='Vladivostok')

    button = SubmitField('SUBMIT')

app.add_url_rule('/', view_func=HomePage.as_view('home_page'))
app.add_url_rule('/calories', view_func=FormPage.as_view('form_page'))

app.run(debug=True)