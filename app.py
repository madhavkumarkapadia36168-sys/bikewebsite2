from flask import Flask, render_template, request, redirect, url_for
import json, os

app = Flask(__name__)
DATA_PATH = os.path.join(os.path.dirname(__file__), 'data', 'bikes.json')

def load_bikes():
    if not os.path.exists(DATA_PATH):
        return []
    with open(DATA_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_bikes(bikes):
    os.makedirs(os.path.dirname(DATA_PATH), exist_ok=True)
    with open(DATA_PATH, 'w', encoding='utf-8') as f:
        json.dump(bikes, f, indent=2, ensure_ascii=False)

@app.route('/')
def index():
    bikes = load_bikes()
    return render_template('index.html', bikes=bikes)

@app.route('/bike/<int:bike_id>')
def bike_detail(bike_id):
    bikes = load_bikes()
    bike = next((b for b in bikes if b['id']==bike_id), None)
    if not bike:
        return "Bike not found", 404
    return render_template('bike.html', bike=bike)

@app.route('/add', methods=['GET','POST'])
def add_bike():
    if request.method == 'POST':
        bikes = load_bikes()
        new_id = max([b['id'] for b in bikes], default=0) + 1
        bike = {
            'id': new_id,
            'name': request.form.get('name','').strip(),
            'brand': request.form.get('brand','').strip(),
            'price': request.form.get('price','').strip(),
            'description': request.form.get('description','').strip(),
            'image_url': request.form.get('image_url','').strip()
        }
        bikes.append(bike)
        save_bikes(bikes)
        return redirect(url_for('index'))
    return render_template('add_bike.html')

if __name__ == '__main__':
    app.run(debug=True)
