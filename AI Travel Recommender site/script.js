// Destination data - enhanced with AI personality matching
const destinations = [
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
        "ai_personality_match": ["creative", "spiritual", "adventurous"],
        "packing_suggestions": ["Light clothing", "Sunscreen", "Swimwear", "Modest clothing for temples"],
        "travel_tips": [
            "Respect local customs, especially when visiting temples",
            "Bargain at markets but do so politely",
            "Drink bottled water and be cautious with street food"
        ]
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
        "ai_personality_match": ["intellectual", "traditional", "thoughtful"],
        "packing_suggestions": ["Comfortable walking shoes", "Layered clothing", "Modest clothing"],
        "travel_tips": [
            "Learn basic Japanese phrases",
            "Remove shoes when entering homes/temples",
            "Visit temples early morning to avoid crowds"
        ]
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
        "ai_personality_match": ["romantic", "luxury", "photography"],
        "packing_suggestions": ["Light clothing", "Sunscreen", "Swimwear", "Comfortable shoes for cobblestones"],
        "travel_tips": [
            "Wear comfortable shoes for cobblestone streets",
            "Book popular restaurants in advance",
            "Stay hydrated in the summer heat"
        ]
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
        "ai_personality_match": ["outdoor", "active", "nature_lover"],
        "packing_suggestions": ["Layered clothing", "Hiking boots", "Waterproof jacket", "Bear spray"],
        "travel_tips": [
            "Carry bear spray when hiking",
            "Check weather conditions before outdoor activities",
            "Book accommodations well in advance, especially in summer"
        ]
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
        "ai_personality_match": ["cultural", "adventurous", "explorer"],
        "packing_suggestions": ["Light clothing", "Sunscreen", "Modest clothing for cultural sites", "Comfortable walking shoes"],
        "travel_tips": [
            "Dress modestly in the medina",
            "Bargain at souks but do so respectfully",
            "Try street food from reputable vendors"
        ]
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
        "ai_personality_match": ["thrill_seeker", "outdoor", "adventurous"],
        "packing_suggestions": ["Layered clothing", "Hiking boots", "Waterproof jacket", "Adventure gear"],
        "travel_tips": [
            "Book adventure activities in advance",
            "Check weather conditions for outdoor activities",
            "Respect local environment and wildlife"
        ]
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
        "ai_personality_match": ["urban", "artistic", "social"],
        "packing_suggestions": ["Light clothing", "Sunscreen", "Swimwear", "Comfortable walking shoes"],
        "travel_tips": [
            "Be aware of pickpockets in tourist areas",
            "Learn basic Spanish or Catalan phrases",
            "Take advantage of the siesta schedule"
        ]
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
        "ai_personality_match": ["remote", "wilderness", "challenge_seeker"],
        "packing_suggestions": ["Warm layered clothing", "Waterproof jacket", "Hiking boots", "Sun protection"],
        "travel_tips": [
            "Prepare for unpredictable weather",
            "Book accommodations well in advance",
            "Respect fragile ecosystems"
        ]
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
        "ai_personality_match": ["unique", "natural_wonder", "photography"],
        "packing_suggestions": ["Warm layered clothing", "Waterproof jacket", "Sturdy shoes", "Camera gear"],
        "travel_tips": [
            "Dress in layers for changing conditions",
            "Book the Blue Lagoon in advance",
            "Download offline maps for remote areas"
        ]
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
        "ai_personality_match": ["beach_lover", "budget", "party"],
        "packing_suggestions": ["Light clothing", "Sunscreen", "Swimwear", "Insect repellent"],
        "travel_tips": [
            "Negotiate taxi fares before getting in",
            "Carry a copy of your passport",
            "Dress modestly when visiting temples"
        ]
    }
];

// AI personality traits mapping
const personalityTraits = {
    "adventurous": ["adventure", "outdoor", "thrill_seeker", "challenge_seeker"],
    "cultural": ["culture", "traditional", "intellectual", "artistic"],
    "relaxed": ["relaxation", "beach_lover", "luxury", "romantic"],
    "nature_lover": ["nature", "wilderness", "natural_wonder", "outdoor"],
    "social": ["nightlife", "urban", "party", "social"],
    "budget_conscious": ["budget", "backpacker", "affordable", "value"]
};

// DOM elements
const travelForm = document.getElementById('travelForm');
const recommendationsSection = document.getElementById('recommendations');
const recommendationsContainer = document.getElementById('recommendationsContainer');
const packingSuggestions = document.getElementById('packingSuggestions');
const travelTips = document.getElementById('travelTips');

// Calculate match score with AI enhancements
function calculateMatchScore(destination, preferences) {
    let score = 0;
    
    // Budget matching (weighted)
    const budgetMap = {
        "1": ["$500-$1500", "$800-$1500", "$1000-$2000"],
        "2": ["$1500-$2500", "$1500-$3000", "$2000-$3500"],
        "3": ["$2500-$4000", "$2000-$4000", "$3000+"]
    };
    
    const userBudget = preferences.budget;
    if (userBudget && budgetMap[userBudget].includes(destination.cost_range)) {
        score += 3;  // Higher weight for budget match
    }
    
    // Weather matching
    const userWeather = preferences.weather;
    if (userWeather !== "any" && destination.weather.includes(userWeather)) {
        score += 2;
    }
    
    // Activity matching (higher weight)
    const userActivities = preferences.activities || [];
    const activityMatches = userActivities.filter(activity => destination.activities.includes(activity)).length;
    score += activityMatches * 2;  // Double weight for activity matches
    
    // Season matching
    const userSeason = preferences.season;
    if (userSeason !== "any" && destination.season.includes(userSeason)) {
        score += 2;
    }
    
    // AI Personality matching
    const userTraits = preferences.personality_traits || [];
    let aiMatches = 0;
    for (const trait of userTraits) {
        // Check if this trait maps to any of the destination's personality matches
        if (personalityTraits[trait]) {
            for (const destTrait of (destination.ai_personality_match || [])) {
                if (personalityTraits[trait].includes(destTrait)) {
                    aiMatches += 1;
                }
            }
        }
    }
    score += aiMatches * 1.5;  // Weight for personality matching
    
    // Duration weighting (longer trips can accommodate more activities)
    const duration = preferences.duration || '0';
    if (['3', '4'].includes(duration) && destination.activities.length >= 4) {
        score += 1;  // Bonus for destinations with many activities for longer trips
    }
    
    return score;
}

// Generate AI-powered insights
function getAIInsights(destination, preferences) {
    const insights = [];
    
    // Budget insight
    const userBudget = preferences.budget;
    const budgetLabels = {"1": "budget-conscious", "2": "mid-range", "3": "luxury"};
    if (userBudget) {
        insights.push(`This destination fits your ${budgetLabels[userBudget] || 'preferred'} travel style.`);
    }
    
    // Activity insight
    const userActivities = preferences.activities || [];
    const matchedActivities = userActivities.filter(act => destination.activities.includes(act));
    if (matchedActivities.length > 0) {
        const activityStr = matchedActivities.join(", ");
        insights.push(`You'll find plenty of ${activityStr} opportunities here.`);
    }
    
    // Personality insight
    const userTraits = preferences.personality_traits || [];
    if (userTraits.length > 0) {
        const traitStr = userTraits.join(", ");
        insights.push(`This destination appeals to ${traitStr} travelers like you.`);
    }
    
    // Seasonal insight
    const userSeason = preferences.season;
    if (userSeason && destination.season.includes(userSeason)) {
        insights.push(`The timing is perfect for visiting during ${userSeason}.`);
    }
    
    return insights.join(" ");
}

// Get recommendations based on preferences with AI enhancements
function getRecommendations(preferences) {
    // Calculate scores for all destinations
    const scoredDestinations = destinations.map(destination => ({
        destination,
        score: calculateMatchScore(destination, preferences)
    }));
    
    // Sort by score (descending)
    scoredDestinations.sort((a, b) => b.score - a.score);
    
    // Return top 3 recommendations with score > 0, including AI insights
    return scoredDestinations
        .filter(item => item.score > 0)
        .slice(0, 3)
        .map(item => {
            const recommendation = {...item.destination};
            recommendation.match_score = item.score;
            recommendation.ai_insights = getAIInsights(recommendation, preferences);
            return recommendation;
        });
}

// Display recommendations with AI features
function displayRecommendations(recommendations) {
    if (recommendations.length === 0) {
        recommendationsContainer.innerHTML = `
            <div class="no-results">
                <h3>Sorry, we couldn't find any destinations matching your preferences.</h3>
                <p>Try adjusting your criteria for better results.</p>
            </div>
        `;
        return;
    }
    
    let recommendationsHTML = '';
    
    recommendations.forEach((dest, index) => {
        recommendationsHTML += `
            <div class="destination-card">
                <h3>${dest.name}</h3>
                <p>${dest.description}</p>
                
                <div class="match-info">
                    <p><strong>AI Insights:</strong> ${dest.ai_insights}</p>
                </div>
                
                <p class="cost-range"><strong>Estimated Cost Range:</strong> ${dest.cost_range}</p>
                <p class="best-time"><strong>Best Time to Visit:</strong> ${dest.best_time}</p>
                
                <div class="attractions-list">
                    <h4>Top 3 Activities or Attractions:</h4>
                    <ul>
                        ${dest.attractions.map(attraction => `<li>${attraction}</li>`).join('')}
                    </ul>
                </div>
            </div>
        `;
    });
    
    recommendationsContainer.innerHTML = recommendationsHTML;
    
    // Display AI features for the top recommendation
    if (recommendations.length > 0) {
        const topDestination = recommendations[0];
        
        // Display packing suggestions
        if (topDestination.packing_suggestions) {
            packingSuggestions.innerHTML = `
                <ul>
                    ${topDestination.packing_suggestions.map(item => `<li>${item}</li>`).join('')}
                </ul>
            `;
        }
        
        // Display travel tips
        if (topDestination.travel_tips) {
            travelTips.innerHTML = `
                <ul>
                    ${topDestination.travel_tips.map(item => `<li>${item}</li>`).join('')}
                </ul>
            `;
        }
    }
}

// Handle form submission
travelForm.addEventListener('submit', function(e) {
    e.preventDefault();
    
    // Get form values
    const formData = new FormData(travelForm);
    
    // Get selected activities
    const activities = [];
    travelForm.querySelectorAll('input[name="activities"]:checked').forEach(checkbox => {
        activities.push(checkbox.value);
    });
    
    // Get personality traits from radio buttons
    const personalityTraits = [];
    for (let i = 1; i <= 3; i++) {
        const selected = travelForm.querySelector(`input[name="personality${i}"]:checked`);
        if (selected) {
            personalityTraits.push(selected.value);
        }
    }
    
    // Create preferences object
    const preferences = {
        budget: formData.get('budget'),
        weather: formData.get('weather'),
        activities: activities,
        duration: formData.get('duration'),
        season: formData.get('season'),
        personality_traits: personalityTraits
    };
    
    // Validate that at least some preferences are selected
    if (!preferences.budget || !preferences.weather || !preferences.season) {
        alert('Please fill in all required fields.');
        return;
    }
    
    // Get recommendations
    const recommendations = getRecommendations(preferences);
    
    // Display recommendations
    displayRecommendations(recommendations);
    
    // Show recommendations section
    recommendationsSection.style.display = 'block';
    
    // Scroll to recommendations
    recommendationsSection.scrollIntoView({ behavior: 'smooth' });
});

// Initialize the page
document.addEventListener('DOMContentLoaded', function() {
    console.log('AI-Powered Travel Recommender System Loaded');
});