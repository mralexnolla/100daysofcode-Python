from flask import Flask


def make_bold(function):
    def wrapper():
        return f'<u><em><b>{function()}</b></em></u>'
    return wrapper


app = Flask(__name__)


@app.route('/bye')
@make_bold
def bye():
    return 'Bye'


if __name__ == "__main__":
    app.run(debug=True)
