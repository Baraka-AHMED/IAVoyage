# tools/travel.py

def find_restaurants_near(location: str):
    # TODO: intégrer Google Maps API
    return {
        "type": "restaurants",
        "location": location,
        "results": [
            {"name": "Restaurant A", "rating": 4.5},
            {"name": "Restaurant B", "rating": 4.2}
        ]
    }


def find_tourist_attractions_near(location: str):
    return {
        "type": "tourist_attractions",
        "location": location,
        "results": [
            {"name": "Museum A"},
            {"name": "Monument B"}
        ]
    }


def suggest_places_to_visit(location: str):
    return {
        "location": location,
        "suggestions": [
            "Centre historique",
            "Quartier local populaire",
            "Parc principal"
        ]
    }


def suggest_activities(location: str):
    return {
        "location": location,
        "activities": [
            "Balade dans le centre-ville",
            "Visite culturelle",
            "Restaurant local",
            "Excursion proche"
        ]
    }
