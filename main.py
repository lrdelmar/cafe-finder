from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TimeField, URLField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
bootstrap = Bootstrap5(app)


# the wtform fields that are generated in cafes.html
class CafeForm(FlaskForm):
    name = StringField('Cafe name', validators=[DataRequired()], render_kw={'class': 'mb-3'})
    location = URLField('Location', validators=[DataRequired(), URL()], render_kw={'class': 'mb-3'})
    open_hour = TimeField(label='Opening Time eg. 08:00', validators=[DataRequired()], render_kw={'class': 'mb-3'})
    close_hour = TimeField(label='Closing Time e.g. 18:00',  validators=[DataRequired()], render_kw={'class': 'mb-3'})
    coffee_rating = SelectField(choices=['☕', '☕☕', '☕☕☕', '☕☕☕☕', '☕☕☕☕☕'], render_kw={'class': 'mb-3'})
    wifi_strength = SelectField(choices=['💪', '💪💪', '💪💪💪', '💪💪💪💪', '💪💪💪💪💪', '✘'], render_kw={'class': 'mb-3'})
    power = SelectField(choices=['🔌', '🔌🔌', '🔌🔌🔌'], render_kw={'class': 'mb-3'})
    submit = SubmitField('Submit', render_kw={'class': 'mt-2'})


# displays the home page
@app.route("/")
def home():
    return render_template("index.html")


# accessing the /add path allows you to add your own cafe entries
@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        print("True")
        with open('cafe-data.csv', mode='a', encoding="utf8") as csv_file:
            new_cafe = f"\n{form.name.data}, {form.location.data}, {form.open_hour.data}, {form.close_hour.data}, " \
                       f"{form.coffee_rating.data}, {form.wifi_strength.data}, {form.power.data}"
            csv_file.write(new_cafe)
        return redirect(url_for('cafes'))
    return render_template('add.html', form=form)


# displays a wtform table of cafes pulled from cafe-data.csv
@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding="utf8") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
