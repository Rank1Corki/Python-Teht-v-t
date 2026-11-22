import json
import os
from flask import Flask

app = Flask(__name__)

folder = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(folder, 'dictionary.json')

with open(file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

@app.route('/sanakirja/<sana>')
def sanakirja(sana):
    
    response = {
        "Enlish": f"{sana}",
        "Finnish": f"{data[sana]}"
    }
    return response

@app.route('/words')
def words():
    response = data
    return response

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3000)