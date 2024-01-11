import streamlit as st
import pandas as pd
import numpy as np
import sklearn
import joblib
import category_encoders as ce


st.title("Flight-Tickets App")


Model = joblib.load("Model.pkl")
Inputs = joblib.load("Inputs.pkl")
def make_pred(Airline,Source,Destination,Total_Stops,Day_of_Journey,Number_of_Dep_Time,Number_Duration,Day_Arrival):
    
    df_pred = pd.DataFrame(columns=Inputs)
    df_pred.at[0,"Airline"] = Airline
    df_pred.at[0,"Source"] = Source
    df_pred.at[0,"Destination"] = Destination
    df_pred.at[0,"Total_Stops"] = Total_Stops
    df_pred.at[0,"Day_of_Journey"] = Day_of_Journey
    df_pred.at[0,"Number_of_Dep_Time"] = Number_of_Dep_Time
    df_pred.at[0,"Number_Duration"] = Number_Duration
    df_pred.at[0,"Day_Arrival"] = Day_Arrival
    result = Model.predict(df_pred)
    return result[0]

def main():
    
    Airline = st.selectbox("Airline", ['IndiGo', 'Air India', 'Jet Airways', 'SpiceJet',
       'Multiple carriers', 'GoAir', 'Vistara', 'Air Asia',
       'Vistara Premium economy', 'Jet Airways Business',
       'Multiple carriers Premium economy', 'Trujet'])
    Source = st.selectbox("Source", ['Banglore', 'Kolkata', 'Delhi', 'Chennai', 'Mumbai'])
    Destination = st.selectbox("Destination", ['New Delhi', 'Banglore', 'Cochin', 'Kolkata', 'Delhi', 'Hyderabad'])
    Total_Stops = st.slider("Total_Stops", min_value=0 , max_value =10 ,  step = 1)
    Day_of_Journey = st.slider("Day_of_Journey", min_value=1 , max_value =30 ,  step = 1)
    Number_of_Dep_Time = st.slider("Number_of_Dep_Time", min_value=0.0 , max_value =24.0 ,  step = 0.1)
    Number_Duration = st.slider("Number_Duration", min_value=1.0 , max_value =100.0 ,  step = 0.1)
    Day_Arrival = st.slider("Day_Arrival", min_value=1 , max_value =30 ,  step = 1)
    if st.button("Predict"):
            results= make_pred(Airline,Source,Destination,Total_Stops,Day_of_Journey,Number_of_Dep_Time,Number_Duration,Day_Arrival)
#             results = make_pred(Airline, Date_of_Journey, Source, Destination, Total_Stops, Day_of_Journey, Number_of_Dep_Time, Number_Duration, Day_Arrival)

            List_Types = ["Your Resturant may fail" , "Your Resturant will success"]
            st.info("Important Note: this price may be not acuarte however you can use it to make a range of correct values for the best appropiate Price Values ")

            st.text(f" Your ticket is {results}$  ")
            if results >= 10000:
                st.warning(f"  For more cheap price than {results}$, you might minmize the number of duration from {Number_Duration} to under 5-Hours or their may be another selected feature that causes this high value as the destination  ")
                
        
main()
    
    
    