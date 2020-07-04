from flask import Flask

app = Flask(__name__)

# pass parameter through URI
@app.route("/<number>", methods=['GET', 'POST'])
def hello(number):
    return "Hello World. {}".format(number)


if __name__ == "__main__":
    # debug=True allows the page to update automatically
    app.run(debug=True)
