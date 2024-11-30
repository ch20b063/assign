import streamlit as st
import requests

st.title("One-Day Tour Planner")

# User input for trip details
city = st.text_input("Enter City", "Rome")
start_time = st.time_input("Start Time", value="09:00")
end_time = st.time_input("End Time", value="18:00")
budget = st.number_input("Enter Your Budget", min_value=0, value=150)
interests = st.selectbox("Select Your Interests", ["History", "Food", "Nature", "Adventure"])

# Trigger to generate itinerary
if st.button("Generate Itinerary"):
    response = requests.get(f"http://localhost:8000/plan_trip/{city}",
                            params={"start_time": str(start_time), "end_time": str(end_time),
                                    "budget": budget, "interests": interests})
    
    if response.status_code == 200:
        data = response.json()
        st.write("Itinerary:", data['itinerary'])
        st.write("Weather:", data['weather'])
    else:
        st.write("Error generating itinerary")
