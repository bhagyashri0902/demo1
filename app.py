from flask import Flask, render_template, request
import pickle
import numpy as np
app = Flask(__name__)
model = pickle.load(open('used_cars.pkl', 'rb'))
brand_map = {
    'Ambassador': 0, 'Ashok': 1, 'Aston Martin': 2, 'Audi': 3, 'Bajaj': 4, 'Bentley': 5, 'BMW': 6, 'Chevrolet': 7,
    'Datsun': 8, 'Fiat': 9, 'Force': 10, 'Ford': 11, 'Honda': 12, 'Hyundai': 13, 'ICML': 14, 'Isuzu': 15,
    'Jaguar': 16, 'Jeep': 17, 'Kia': 18, 'Land Rover': 19, 'Lexus': 20, 'Mahindra': 21, 'Maruti Suzuki': 22,
    'Maserati': 23, 'Mercedes-Benz': 24, 'MG': 25, 'Mini': 26, 'Mitsubishi': 27, 'Nissan': 28, 'Opel': 29,
    'Porsche': 30, 'Renault': 31, 'Rolls-Royce': 32, 'Skoda': 33, 'Ssangyong': 34, 'Tata': 35, 'Toyota': 36,
    'Volkswagen': 37, 'Volvo': 38
}
@app.route('/')
def home():
    return render_template('index.html', brands=list(brand_map.keys()), prediction=None)
@app.route('/predict', methods=['POST'])
def predict():
    brand = request.form['brand']
    year = int(request.form['year'])
    kms = int(request.form['kms'])
    vehicle_type = 0 if request.form['vehicle_type'] == 'Manual' else 1
    owner = 0 if request.form['owner'] == 'first' else 1
    fuel_type = 0 if request.form['fuel_type'] == 'Petrol' else 1 if request.form['fuel_type'] == 'Diesel' else 2
    brand_encoded = brand_map[brand] 
    X_test= np.array([[brand_encoded, year, kms, vehicle_type, owner, fuel_type]])
    yp = model.predict(X_test)[0]
    return render_template('index.html', brands=list(brand_map.keys()), prediction=round(yp, 2))
if __name__ == '__main__':
    app.run(debug=True)