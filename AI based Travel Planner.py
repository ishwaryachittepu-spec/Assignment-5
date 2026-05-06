# AI BASED TRAVEL PLANNER
# --------------------------------------------
# Features:
# 1. Uses existing knowledge bases (tourist places, food, hotels)
# 2. Personalized recommendations
# 3. Budget assessment
# 4. Suggests food and attractions
# 5. Generates travel plan automatically
#
# Python Version: 3.x

import random

# -------------------------------
# KNOWLEDGE BASES
# -------------------------------

tourist_places = {
    "Goa": {
        "type": "Beach",
        "budget": "Medium",
        "activities": ["Beach", "Water Sports", "Nightlife"],
        "food": ["Seafood", "Goan Curry", "Bebinca"],
        "hotel_cost": 2500
    },

    "Manali": {
        "type": "Hill Station",
        "budget": "Medium",
        "activities": ["Snow", "Trekking", "Adventure Sports"],
        "food": ["Trout Fish", "Siddu", "Thukpa"],
        "hotel_cost": 2000
    },

    "Jaipur": {
        "type": "Historical",
        "budget": "Low",
        "activities": ["Fort Visit", "Shopping", "Camel Ride"],
        "food": ["Dal Baati", "Ghewar", "Kachori"],
        "hotel_cost": 1500
    },

    "Kerala": {
        "type": "Nature",
        "budget": "High",
        "activities": ["Backwaters", "Ayurveda", "Houseboat"],
        "food": ["Appam", "Fish Curry", "Puttu"],
        "hotel_cost": 4000
    },

    "Hyderabad": {
        "type": "City",
        "budget": "Low",
        "activities": ["Charminar", "Museums", "Shopping"],
        "food": ["Biryani", "Haleem", "Double Ka Meetha"],
        "hotel_cost": 1800
    }
}

# -------------------------------
# FUNCTION: USER INPUT
# -------------------------------

def get_user_preferences():
    print("\n===== AI TRAVEL PLANNER =====")

    budget = input("Enter your budget (Low/Medium/High): ")
    interest = input("Enter your interest (Beach/Hill Station/Historical/Nature/City): ")
    days = int(input("Enter number of travel days: "))

    return budget, interest, days

# -------------------------------
# FUNCTION: RECOMMEND DESTINATION
# -------------------------------

def recommend_destination(budget, interest):

    recommendations = []

    for place, details in tourist_places.items():

        if details["budget"].lower() == budget.lower() and \
           details["type"].lower() == interest.lower():

            recommendations.append(place)

    return recommendations

# -------------------------------
# FUNCTION: COST ESTIMATION
# -------------------------------

def estimate_cost(place, days):

    hotel = tourist_places[place]["hotel_cost"] * days
    food = 800 * days
    travel = 3000

    total = hotel + food + travel

    return total

# -------------------------------
# FUNCTION: GENERATE TOUR PLAN
# -------------------------------

def generate_plan(place, days):

    details = tourist_places[place]

    print("\n===== PERSONALIZED TOUR PLAN =====")

    print(f"\nDestination: {place}")
    print(f"Place Type: {details['type']}")

    print("\nRecommended Activities:")

    for activity in details["activities"]:
        print("-", activity)

    print("\nFood Recommendations:")

    for item in details["food"]:
        print("-", item)

    total_cost = estimate_cost(place, days)

    print(f"\nEstimated Total Cost for {days} days: ₹{total_cost}")

    print("\nDaily Schedule:")

    for day in range(1, days + 1):

        activity = random.choice(details["activities"])
        food = random.choice(details["food"])

        print(f"\nDay {day}:")
        print(" Activity:", activity)
        print(" Try Food:", food)

# -------------------------------
# MAIN PROGRAM
# -------------------------------

budget, interest, days = get_user_preferences()

results = recommend_destination(budget, interest)

if len(results) == 0:

    print("\nNo exact match found.")
    print("Showing alternative destinations:\n")

    for place in tourist_places:
        print("-", place)

else:

    print("\nRecommended Destinations:")

    for i, place in enumerate(results):
        print(f"{i+1}. {place}")

    choice = int(input("\nChoose destination number: "))

    selected_place = results[choice - 1]

    generate_plan(selected_place, days)

print("\nThank you for using AI Travel Planner!")
