# coffee-and-wifi
Find your nearest coffee shop and see their wifi and coffee ratings as well as their power-socket availability.

Please create a venv folder before initialising this program locally.

This program allows you to look at local cafes and view their Wi-Fi strength, the quality of their coffee and the availability of power sockets for working remotely.

This website was written using Python, HTML, CSS and Jinja in PyCharm using Flask, Boostrap5, FlaskForm and csv libraries.

The /cafes path shows a table containing data that has been pulled from the cafe-data.csv using Python and Jinja.

There is also a hidden /add path which allows you to add any local cafes you have found and add their ratings.
The form on this page was creating using flask_wtf and uses StringField, SubmitField, SelectField, TimeField and URLField fields, it is validated using DataRequired and URL validators.
The data entererd into the form is validated and then added to the cafe-data.csv, you are then redirected back to the /cafes page.
