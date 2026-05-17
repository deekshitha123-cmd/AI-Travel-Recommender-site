# Intelligent Travel Recommendation System

This is a Python-based travel recommendation system that suggests personalized travel destinations based on user preferences.

## Features

The system recommends destinations based on:
- Budget range
- Weather preferences
- Activity interests (adventure, relaxation, culture, nature, nightlife)
- Travel duration
- Preferred season

For each recommendation, the system provides:
- Destination Name
- Short Description (2-3 lines)
- Why It Matches Your Preferences
- Estimated Cost Range
- Best Time to Visit
- Top 3 Activities or Attractions

## How to Use

1. Run the script:
   ```
   python travel_recommender.py
   ```

2. Answer the prompts to specify your travel preferences:
   - Budget range
   - Preferred weather
   - Activities of interest
   - Travel duration
   - Preferred season

3. Receive personalized travel recommendations based on your preferences.

## Requirements

- Python 3.x

## Destinations Database

The system includes 10 diverse global destinations:
- Bali, Indonesia
- Kyoto, Japan
- Santorini, Greece
- Banff National Park, Canada
- Marrakech, Morocco
- Queenstown, New Zealand
- Barcelona, Spain
- Patagonia, Chile/Argentina
- Reykjavik, Iceland
- Phuket, Thailand

Each destination has detailed information about weather, activities, costs, and attractions.

## Customization

To add new destinations or modify existing ones, edit the `destinations` list in the `TravelRecommender` class in `travel_recommender.py`.