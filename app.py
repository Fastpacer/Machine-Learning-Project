import streamlit as st
import joblib
import numpy as np

scaler=joblib.load("scaler.pkl")
model=joblib.load("model.pkl")


st.title("Customer Car Price Estimator App")

st.divider()

st.write("""This application assists customers in obtaining price estimates for vehicles within their desired price range, 
         enabling them to receive tailored recommendations for suitable car options that align with their budget.""")



age=st.number_input(" Enter your age",min_value=18,max_value=90,value=40,step=1)

salary=st.number_input(" Enter your salary",min_value=1000,max_value=9999999999,step=5000,value=30000)


networth=st.number_input(" Enter your networth",min_value=0,max_value=9999999999, step=20000 , value= 100000)

X=[age,salary,networth]

calculatebutton=st.button("Calculate")

if calculatebutton:
       st.balloons()
       X_2 = np.array(X)
       X_array = scaler.transform([X_2])

    # Reshape X_array to have 2 dimensions
       X_array = X_array.reshape(1, -1)

       prediction = model.predict(X_array)
       st.write(f"Prediction is {prediction[0]:,.2f}")
       st.write("Cars advisable in the following range")

else:
   st.write("Please enter the values and press the calculate button ")


