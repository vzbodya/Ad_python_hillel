import csv
import requests
import pandas

from faker import Faker
from flask import Flask
from webargs import validate, fields
from webargs.flaskparser import use_kwargs


def create_single_student():
    result = []
    fake_person = Faker("UK")
    result.append(fake_person.first_name())
    result.append(fake_person.last_name())
    result.append(fake_person.email())
    result.append(fake_person.password())
    result.append(fake_person.date_of_birth())
    return result


app = Flask(__name__)


@app.route("/")
def index_page():
    return "<h1>Hello!</h1><h2>It is a home page</h2>"


@app.route("/bitcoin_rate")
@use_kwargs(
    {
        "currency": fields.String(missing="USD")
    },
    location="query"
)
def get_bitcoin_value(currency):

    url = "https://bitpay.com/api/rates"
    result = requests.get(url)
    result_json = result.json()

    for element in result_json:
        if element["code"] == currency:
            return f"The bitcoin price in {currency} is {str(element['rate'])}"

    return "nothing been found"


@app.route("/get_students")
@use_kwargs(
    {
        "number": fields.Int(missing=1, validate=[validate.Range(min=1, max=1000)])
    },
    location="query"
)
def generate_students(number):

    headers = ["Name", "Surname", "Email", "Password", "Date of birth"]
    with open("students_data.csv", "w", encoding="UTF-8") as file:

        writer = csv.writer(file)

        # Adding headers as the first row of the table
        writer.writerow(headers)

        # Creating fake students and saving theirs data to a csv file
        for student in range(int(number)):
            data = create_single_student()
            writer.writerow(data)

    # Reads a csv file and returns html table with data from the file
    result = pandas.read_csv("students_data.csv")
    return result.to_html()


app.run(debug=True)
