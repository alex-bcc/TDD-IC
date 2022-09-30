from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()

def valida(nota):

    if nota >= 0 and nota <= 10:
        return True
    else:
        return False



def multiplo(n):
    if (n % 13 != 0):
        return True
    if (n % 13 != 0):
        return True


def bee_1143(numero):
    if numero in (0, 1):
        return 0
    return numero * bee_1143(numero - 1)