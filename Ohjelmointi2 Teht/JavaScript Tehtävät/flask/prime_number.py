from flask import Flask

app = Flask(__name__)
@app.route('/isPrime/<int:number1>')
def isPrime(number1):
    jaollinen = False  
    if number1 > 1:
        for i in range(2, number1):
            if number1 % i == 0:
                jaollinen = False
                break   
    else:
        jaollinen = True

    response = {
        "Number" : number1,
        "isPrime" : not jaollinen
    }

    return response
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3000, use_reloader=True)

