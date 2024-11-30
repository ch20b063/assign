from fastapi import FastAPI
from app.agents.user_interaction_agent import UserInteractionAgent
from app.agents.itinerary_generation_agent import ItineraryGenerationAgent
from app.agents.weather_agent import WeatherAgent

app = FastAPI()

# Initialize agents
user_agent = UserInteractionAgent()
itinerary_agent = ItineraryGenerationAgent()
weather_agent = WeatherAgent()

@app.get("/plan_trip/{city}")
def plan_trip(city: str, start_time: str, end_time: str, budget: float, interests: str):
    # Get user preferences, generate itinerary, etc.
    itinerary = itinerary_agent.generate_itinerary(city, start_time, end_time, budget, interests)
    weather = weather_agent.get_weather(city)
    return {"itinerary": itinerary, "weather": weather}
