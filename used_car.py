import streamlit as st
import pickle
import pandas as pd
page_bg_img = '''
<style>
[data-testid="stAppViewContainer"] {
    background-image:url("https://img.freepik.com/free-vector/lightened-luxury-sedan-car-darkness-with-headlamps-rear-lights-lit-realistic-image-reflection_1284-28803.jpg?semt=ais_hybrid&w=740");
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

model=pickle.load(open('used_cars.pkl','rb'))
st.title("Used car Price Prediction app")
brand_map = {
    'Ambassador': 0, 'Ashok': 1, 'Aston Martin': 2, 'Audi': 3, 'Bajaj': 4, 'Bentley': 5, 'BMW': 6, 'Chevrolet': 7,
    'Datsun': 8, 'Fiat': 9, 'Force': 10, 'Ford': 11, 'Honda': 12, 'Hyundai': 13, 'ICML': 14, 'Isuzu': 15,
    'Jaguar': 16, 'Jeep': 17, 'Kia': 18, 'Land Rover': 19, 'Lexus': 20, 'Mahindra': 21, 'Maruti Suzuki': 22,
    'Maserati': 23, 'Mercedes-Benz': 24, 'MG': 25, 'Mini': 26, 'Mitsubishi': 27, 'Nissan': 28, 'Opel': 29,
    'Porsche': 30, 'Renault': 31, 'Rolls-Royce': 32, 'Skoda': 33, 'Ssangyong': 34, 'Tata': 35, 'Toyota': 36,
    'Volkswagen': 37, 'Volvo': 38
}
brand = st.selectbox("Select Car Brand", options=list(brand_map.keys()))
Year=st.text_input('Enter year of manufacturing:')
Kilometers=st.text_input('Enter Kms:')
vehicle_type=st.selectbox('What is vehicle type?',['Automatic','Manual'])
vehicle_type=0 if vehicle_type=='Manual'else 1
Owner=st.selectbox('What is vehicle type?',['first','second'])
Owner= 0 if Owner=='first' else 1
Fuel_type=st.selectbox('What is fuel type?',['Petrol','Diesel','Hybrid/CNG'])
Fuel_type = 0 if Fuel_type == 'Petrol' else 1 if Fuel_type == 'Diesel' else 2
brand_encoded = brand_map[brand]
if st.button("Predict Price"):
    input_df = pd.DataFrame([[brand_encoded, Year,Kilometers,vehicle_type,Owner,Fuel_type]],
                            columns=['brand_enc', 'Year', 'Kms_enc','Transmission_enc','Owner_enc','Fuel_enc'])
    yp = model.predict(input_df)[0]
    st.markdown(f"""
    <h3 style='text-align: center; color: white;'>
        ✅ Charges: ₹{yp.item():.2f}
    </h3>
""", unsafe_allow_html=True)