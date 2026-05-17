import random
import json
from datetime import datetime

class TravelRecommender:
    def __init__(self):
        # Database of destinations with their attributes
        self.destinations = [
            {
                "name": "Bali, Indonesia",
                "description": "Tropical paradise island known for its volcanic mountains, iconic rice paddies, pristine beaches, and coral reefs.",
                "weather": ["tropical", "warm"],
                "activities": ["relaxation", "nature", "culture", "adventure"],
                "season": ["summer", "winter"],
                "cost_range": "$1000-$2000",
                "best_time": "April to October",
                "attractions": [
                    "Ubud Monkey Forest",
                    "Tanah Lot Temple",
                    "Seminyak Beach"
                ],
                "ai_personality_match": ["creative", "spiritual", "adventurous"]
            },
            {
                "name": "Kyoto, Japan",
                "description": "Historic city famous for its classical Buddhist temples, gardens, imperial palaces, and traditional wooden houses.",
                "weather": ["temperate", "cool"],
                "activities": ["culture", "nature", "relaxation"],
                "season": ["spring", "autumn"],
                "cost_range": "$1500-$3000",
                "best_time": "March to May, September to November",
                "attractions": [
                    "Fushimi Inari Shrine",
                    "Arashiyama Bamboo Grove",
                    "Kinkaku-ji (Golden Pavilion)"
                ],
                "ai_personality_match": ["intellectual", "traditional", "thoughtful"]
            },
            {
                "name": "Santorini, Greece",
                "description": "Picturesque island renowned for its stunning sunsets, white-washed buildings, and crystal-clear Aegean Sea views.",
                "weather": ["mediterranean", "warm"],
                "activities": ["relaxation", "culture", "nightlife"],
                "season": ["summer"],
                "cost_range": "$2000-$4000",
                "best_time": "May to October",
                "attractions": [
                    "Oia Village Sunset",
                    "Red Beach",
                    "Ancient Thera"
                ],
                "ai_personality_match": ["romantic", "luxury", "photography"]
            },
            {
                "name": "Banff National Park, Canada",
                "description": "Canada's oldest national park, featuring majestic Rocky Mountain landscapes, turquoise glacial lakes, and abundant wildlife.",
                "weather": ["continental", "cool"],
                "activities": ["nature", "adventure", "relaxation"],
                "season": ["summer", "winter"],
                "cost_range": "$1500-$2500",
                "best_time": "June to August, December to March",
                "attractions": [
                    "Lake Louise",
                    "Moraine Lake",
                    "Johnston Canyon"
                ],
                "ai_personality_match": ["outdoor", "active", "nature_lover"]
            },
            {
                "name": "Marrakech, Morocco",
                "description": "Vibrant city known for its medina, souks, palaces, and gardens, blending Berber, Arabic, and French cultures.",
                "weather": ["desert", "warm"],
                "activities": ["culture", "adventure", "nightlife"],
                "season": ["spring", "autumn"],
                "cost_range": "$1000-$2000",
                "best_time": "March to May, September to November",
                "attractions": [
                    "Jemaa el-Fnaa Square",
                    "Majorelle Garden",
                    "Bahia Palace"
                ],
                "ai_personality_match": ["cultural", "adventurous", "explorer"]
            },
            {
                "name": "Queenstown, New Zealand",
                "description": "Adventure capital of the world, surrounded by dramatic mountains and set beside Lake Wakatipu.",
                "weather": ["temperate", "cool"],
                "activities": ["adventure", "nature", "relaxation"],
                "season": ["summer", "winter"],
                "cost_range": "$2500-$4000",
                "best_time": "December to February, June to August",
                "attractions": [
                    "Milford Sound",
                    "Skyline Gondola",
                    "Kawarau Gorge Swing"
                ],
                "ai_personality_match": ["thrill_seeker", "outdoor", "adventurous"]
            },
            {
                "name": "Barcelona, Spain",
                "description": "Cosmopolitan city famous for its unique architecture, vibrant arts scene, and Mediterranean beaches.",
                "weather": ["mediterranean", "warm"],
                "activities": ["culture", "nightlife", "relaxation"],
                "season": ["spring", "summer", "autumn"],
                "cost_range": "$1500-$2500",
                "best_time": "May to June, September to October",
                "attractions": [
                    "Sagrada Familia",
                    "Park Güell",
                    "Las Ramblas"
                ],
                "ai_personality_match": ["urban", "artistic", "social"]
            },
            {
                "name": "Patagonia, Chile/Argentina",
                "description": "Remote region at the southern end of South America, known for its dramatic mountain peaks, glaciers, and steppes.",
                "weather": ["cold", "cool"],
                "activities": ["nature", "adventure", "relaxation"],
                "season": ["summer"],
                "cost_range": "$2000-$3500",
                "best_time": "November to March",
                "attractions": [
                    "Torres del Paine",
                    "Perito Moreno Glacier",
                    "El Chaltén"
                ],
                "ai_personality_match": ["remote", "wilderness", "challenge_seeker"]
            },
            {
                "name": "Reykjavik, Iceland",
                "description": "World's northernmost capital, gateway to geysers, waterfalls, volcanoes, and the Northern Lights.",
                "weather": ["cold", "cool"],
                "activities": ["nature", "adventure", "relaxation"],
                "season": ["winter"],
                "cost_range": "$2000-$3500",
                "best_time": "September to March (Northern Lights)",
                "attractions": [
                    "Blue Lagoon",
                    "Golden Circle Route",
                    "Northern Lights Tour"
                ],
                "ai_personality_match": ["unique", "natural_wonder", "photography"]
            },
            {
                "name": "Phuket, Thailand",
                "description": "Largest island in Thailand, famous for its palm-lined beaches, clear waters, and vibrant nightlife.",
                "weather": ["tropical", "warm"],
                "activities": ["relaxation", "nature", "nightlife", "adventure"],
                "season": ["winter"],
                "cost_range": "$800-$1500",
                "best_time": "November to April",
                "attractions": [
                    "Phi Phi Islands",
                    "Big Buddha Phuket",
                    "Patong Beach"
                ],
                "ai_personality_match": ["beach_lover", "budget", "party"]
            }
        ]

        # AI personality traits mapping
        self.personality_traits = {
            "adventurous": ["adventure", "outdoor", "thrill_seeker", "challenge_seeker"],
            "cultural": ["culture", "traditional", "intellectual", "artistic"],
            "relaxed": ["relaxation", "beach_lover", "luxury", "romantic"],
            "nature_lover": ["nature", "wilderness", "natural_wonder", "outdoor"],
            "social": ["nightlife", "urban", "party", "social"],
            "budget_conscious": ["budget", "backpacker", "affordable", "value"]
        }

    def get_user_preferences(self):
        """Collect user preferences for travel recommendations"""
        print("Welcome to the AI-Powered Travel Recommendation System!")
        print("Please answer the following questions to get personalized recommendations:")
        
        preferences = {}
        
        # Budget preference
        budget_options = {
            "1": "Budget ($500-$1500)",
            "2": "Mid-range ($1500-$3000)", 
            "3": "Luxury ($3000+)"
        }
        print("\nWhat is your budget range?")
        for key, value in budget_options.items():
            print(f"{key}. {value}")
        budget_choice = input("Enter your choice (1-3): ")
        preferences['budget'] = budget_choice
        
        # Weather preference
        weather_options = {
            "1": "Tropical/Warm",
            "2": "Temperate/Cool", 
            "3": "Mediterranean",
            "4": "Desert",
            "5": "Cold"
        }
        print("\nWhat weather do you prefer?")
        for key, value in weather_options.items():
            print(f"{key}. {value}")
        weather_choice = input("Enter your choice (1-5): ")
        weather_map = {
            "1": "tropical",
            "2": "temperate",
            "3": "mediterranean",
            "4": "desert",
            "5": "cold"
        }
        preferences['weather'] = weather_map.get(weather_choice, "any")
        
        # Activity preferences (multiple selection)
        activity_options = {
            "1": "Adventure",
            "2": "Relaxation", 
            "3": "Culture",
            "4": "Nature",
            "5": "Nightlife"
        }
        print("\nWhat activities interest you? (Select all that apply)")
        for key, value in activity_options.items():
            print(f"{key}. {value}")
        activity_choices = input("Enter your choices separated by commas (e.g., 1,3,4): ").split(',')
        activity_map = {
            "1": "adventure",
            "2": "relaxation",
            "3": "culture",
            "4": "nature",
            "5": "nightlife"
        }
        preferences['activities'] = [activity_map.get(choice.strip(), "") for choice in activity_choices if choice.strip() in activity_map]
        
        # Travel duration
        duration_options = {
            "1": "Weekend getaway (2-4 days)",
            "2": "Short trip (5-7 days)", 
            "3": "Extended vacation (8-14 days)",
            "4": "Long adventure (15+ days)"
        }
        print("\nHow long do you plan to travel?")
        for key, value in duration_options.items():
            print(f"{key}. {value}")
        duration_choice = input("Enter your choice (1-4): ")
        preferences['duration'] = duration_choice
        
        # Season preference
        season_options = {
            "1": "Spring",
            "2": "Summer", 
            "3": "Autumn/Fall",
            "4": "Winter"
        }
        print("\nWhich season do you prefer to travel in?")
        for key, value in season_options.items():
            print(f"{key}. {value}")
        season_choice = input("Enter your choice (1-4): ")
        season_map = {
            "1": "spring",
            "2": "summer",
            "3": "autumn",
            "4": "winter"
        }
        preferences['season'] = season_map.get(season_choice, "any")
        
        # AI Personality Assessment
        print("\nLet's understand your travel personality for better recommendations!")
        personality_questions = [
            "Do you prefer adrenaline-pumping activities or relaxing on a beach?",
            "Are you more interested in historical sites or modern city experiences?",
            "Would you rather stay in luxury hotels or local accommodations?",
            "Do you enjoy solo travel or traveling with groups?",
            "Are you drawn to remote wilderness areas or popular tourist destinations?"
        ]
        
        personality_scores = {}
        for i, question in enumerate(personality_questions, 1):
            print(f"\n{i}. {question}")
            print("1. Strongly Agree  2. Agree  3. Neutral  4. Disagree  5. Strongly Disagree")
            try:
                answer = int(input("Your answer (1-5): "))
                # Convert to score (-2 to +2)
                score = 3 - answer
                # Map to personality traits (simplified)
                if i == 1:  # Adventure vs Relaxation
                    personality_scores['adventurous'] = personality_scores.get('adventurous', 0) + score
                    personality_scores['relaxed'] = personality_scores.get('relaxed', 0) - score
                elif i == 2:  # Cultural vs Urban
                    personality_scores['cultural'] = personality_scores.get('cultural', 0) + score
                    personality_scores['social'] = personality_scores.get('social', 0) - score
                elif i == 3:  # Luxury vs Budget
                    personality_scores['budget_conscious'] = personality_scores.get('budget_conscious', 0) - score
                elif i == 4:  # Solo vs Group
                    # No direct trait mapping
                    pass
                elif i == 5:  # Remote vs Popular
                    personality_scores['nature_lover'] = personality_scores.get('nature_lover', 0) + score
                    
            except ValueError:
                print("Invalid input. Skipping this question.")
        
        # Determine dominant personality traits
        preferences['personality_traits'] = [trait for trait, score in personality_scores.items() if score > 0]
        
        return preferences
    
    def calculate_match_score(self, destination, preferences):
        """Calculate how well a destination matches user preferences using AI-enhanced matching"""
        score = 0
        
        # Budget matching (weighted)
        budget_map = {
            "1": ["$500-$1500", "$800-$1500", "$1000-$2000"],
            "2": ["$1500-$2500", "$1500-$3000", "$2000-$3500"],
            "3": ["$2500-$4000", "$2000-$4000", "$3000+"]
        }
        user_budget = preferences.get('budget')
        if user_budget and destination['cost_range'] in budget_map.get(user_budget, []):
            score += 3  # Higher weight for budget match
            
        # Weather matching
        user_weather = preferences.get('weather')
        if user_weather != "any" and user_weather in destination['weather']:
            score += 2
            
        # Activity matching (higher weight)
        user_activities = preferences.get('activities', [])
        activity_matches = sum(1 for activity in user_activities if activity in destination['activities'])
        score += activity_matches * 2  # Double weight for activity matches
            
        # Season matching
        user_season = preferences.get('season')
        if user_season != "any" and user_season in destination['season']:
            score += 2
            
        # AI Personality matching
        user_traits = preferences.get('personality_traits', [])
        ai_matches = 0
        for trait in user_traits:
            # Check if this trait maps to any of the destination's personality matches
            if trait in self.personality_traits:
                for dest_trait in destination.get('ai_personality_match', []):
                    if dest_trait in self.personality_traits[trait]:
                        ai_matches += 1
                        
        score += ai_matches * 1.5  # Weight for personality matching
        
        # Duration weighting (longer trips can accommodate more activities)
        duration = preferences.get('duration', '0')
        if duration in ['3', '4'] and len(destination['activities']) >= 4:
            score += 1  # Bonus for destinations with many activities for longer trips
            
        return score
    
    def get_ai_insights(self, destination, preferences):
        """Generate AI-powered insights for why this destination matches the user"""
        insights = []
        
        # Budget insight
        user_budget = preferences.get('budget')
        budget_labels = {"1": "budget-conscious", "2": "mid-range", "3": "luxury"}
        if user_budget:
            insights.append(f"This destination fits your {budget_labels.get(user_budget, 'preferred')} travel style.")
        
        # Activity insight
        user_activities = preferences.get('activities', [])
        matched_activities = [act for act in user_activities if act in destination['activities']]
        if matched_activities:
            activity_str = ", ".join(matched_activities)
            insights.append(f"You'll find plenty of {activity_str} opportunities here.")
        
        # Personality insight
        user_traits = preferences.get('personality_traits', [])
        if user_traits:
            trait_str = ", ".join(user_traits)
            insights.append(f"This destination appeals to {trait_str} travelers like you.")
        
        # Seasonal insight
        user_season = preferences.get('season')
        if user_season and user_season in destination['season']:
            insights.append(f"The timing is perfect for visiting during {user_season}.")
        
        return " ".join(insights)
    
    def recommend_destinations(self, preferences, num_recommendations=3):
        """Recommend destinations based on user preferences with AI enhancements"""
        # Calculate scores for all destinations
        scored_destinations = []
        for destination in self.destinations:
            score = self.calculate_match_score(destination, preferences)
            scored_destinations.append((destination, score))
        
        # Sort by score (descending)
        scored_destinations.sort(key=lambda x: x[1], reverse=True)
        
        # Return top recommendations with AI insights
        recommendations = []
        for dest, score in scored_destinations[:num_recommendations]:
            if score > 0:
                recommendation = dest.copy()
                recommendation['match_score'] = score
                recommendation['ai_insights'] = self.get_ai_insights(dest, preferences)
                recommendations.append(recommendation)
        
        return recommendations
    
    def display_recommendations(self, recommendations):
        """Display the recommended destinations in a formatted way"""
        if not recommendations:
            print("\nSorry, we couldn't find any destinations matching your preferences.")
            print("Try adjusting your criteria for better results.")
            return
            
        print("\n" + "="*60)
        print("AI-PERSONALIZED TRAVEL RECOMMENDATIONS")
        print("="*60)
        
        for i, dest in enumerate(recommendations, 1):
            print(f"\n{i}. {dest['name']}")
            print("-" * 40)
            print(f"Description: {dest['description']}")
            
            # AI-generated insights
            print(f"AI Insights: {dest['ai_insights']}")
            
            print(f"Estimated Cost Range: {dest['cost_range']}")
            print(f"Best Time to Visit: {dest['best_time']}")
            print("Top 3 Activities or Attractions:")
            for j, attraction in enumerate(dest['attractions'], 1):
                print(f"  {j}. {attraction}")
                
            # Additional AI feature: Smart packing suggestions
            self.suggest_packing(dest)
            
            # Additional AI feature: Travel tips
            self.provide_travel_tips(dest)

    def suggest_packing(self, destination):
        """AI-powered packing suggestions based on destination"""
        print("\n🤖 AI Packing Suggestions:")
        
        suggestions = []
        if any(w in destination['weather'] for w in ['tropical', 'warm', 'mediterranean']):
            suggestions.extend(["Light clothing", "Sunscreen", "Swimwear"])
        if any(w in destination['weather'] for w in ['cold', 'cool']):
            suggestions.extend(["Warm jacket", "Layered clothing", "Waterproof shoes"])
        if 'adventure' in destination['activities']:
            suggestions.extend(["Hiking boots", "Backpack", "First aid kit"])
        if 'culture' in destination['activities']:
            suggestions.extend(["Modest clothing for religious sites", "Comfortable walking shoes"])
        if 'beach' in str(destination['attractions']).lower():
            suggestions.extend(["Beach towel", "Hat", "Sunglasses"])
            
        if suggestions:
            print("  • " + "\n  • ".join(set(suggestions)))  # Using set to remove duplicates
        else:
            print("  Based on this destination, pack comfortable clothing and essentials.")

    def provide_travel_tips(self, destination):
        """AI-powered travel tips based on destination"""
        print("\n🤖 AI Travel Tips:")
        
        tips = []
        if destination['name'] == "Bali, Indonesia":
            tips.extend([
                "Respect local customs, especially when visiting temples",
                "Bargain at markets but do so politely",
                "Drink bottled water and be cautious with street food"
            ])
        elif destination['name'] == "Kyoto, Japan":
            tips.extend([
                "Learn basic Japanese phrases",
                "Remove shoes when entering homes/temples",
                "Visit temples early morning to avoid crowds"
            ])
        elif destination['name'] == "Santorini, Greece":
            tips.extend([
                "Wear comfortable shoes for cobblestone streets",
                "Book popular restaurants in advance",
                "Stay hydrated in the summer heat"
            ])
        elif destination['name'] == "Banff National Park, Canada":
            tips.extend([
                "Carry bear spray when hiking",
                "Check weather conditions before outdoor activities",
                "Book accommodations well in advance, especially in summer"
            ])
        elif "Thailand" in destination['name']:
            tips.extend([
                "Negotiate taxi fares before getting in",
                "Carry a copy of your passport",
                "Dress modestly when visiting temples"
            ])
        else:
            # Generic AI tips
            tips.extend([
                "Research local customs and etiquette",
                "Download offline maps of the area",
                "Register with your embassy for safety updates"
            ])
            
        if tips:
            print("  • " + "\n  • ".join(tips))

    def save_preferences(self, preferences, recommendations):
        """Save user preferences and recommendations for future reference"""
        data = {
            "timestamp": datetime.now().isoformat(),
            "preferences": preferences,
            "recommendations": [rec['name'] for rec in recommendations]
        }
        
        filename = f"travel_recommendations_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
        
        print(f"\n💾 Your recommendations have been saved to {filename}")

    def run(self):
        """Main method to run the AI-powered travel recommender"""
        try:
            preferences = self.get_user_preferences()
            recommendations = self.recommend_destinations(preferences)
            self.display_recommendations(recommendations)
            
            # AI feature: Save recommendations
            if recommendations:
                save_choice = input("\nWould you like to save these recommendations? (y/n): ")
                if save_choice.lower() == 'y':
                    self.save_preferences(preferences, recommendations)
            
            # AI feature: Ask for feedback
            print("\n🧠 Help us improve! Rate your experience (1-5 stars): ")
            try:
                rating = int(input("Your rating: "))
                if 1 <= rating <= 5:
                    print(f"Thank you for your {rating}-star rating! We'll use this feedback to improve our AI recommendations.")
                else:
                    print("Thanks for your feedback!")
            except ValueError:
                print("Thanks for trying our AI-powered travel recommender!")
                
        except KeyboardInterrupt:
            print("\n\nThank you for using the AI-Powered Travel Recommendation System. Safe travels! 🌍✈️")
        except Exception as e:
            print(f"\nAn error occurred: {str(e)}")
            print("Please try again or contact support.")

if __name__ == "__main__":
    recommender = TravelRecommender()
    recommender.run()