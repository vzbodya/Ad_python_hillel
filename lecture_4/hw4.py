from flask import Flask
import string
import random
import csv


app = Flask(__name__)


@app.route("/")
def index():
    return "<p>Hello, World !</p>"


@app.route("/getpass")
def generate_password():
    letters = string.ascii_letters
    result = "".join(random.choice(letters) for _ in range(random.randint(10, 25)))
    return f"{result}"


@app.route("/getaverages")
def calculate_average():

    number_of_rows = 0
    height_sum = 0
    weight_sum = 0

    with open("hw.csv", "r") as file:
        reader = csv.reader(file)

        # Skipping the first row that consists headers
        next(reader)
        for row in reader:
            number_of_rows += 1
            height_sum += float(row[1])
            weight_sum += float(row[2])
    file.close()

    # Calculating the average values
    height_result = height_sum / number_of_rows
    weight_result = weight_sum / number_of_rows

    return f"Height average equals to {height_result} <br>Weight average equals to {weight_result}</br>"


app.run(port=5000, debug=True)

