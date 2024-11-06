from services.feeds import fetch_feeds
from services.openai_service import generate_ai_response

# Define a registry of services with their triggers
SERVICE_REGISTRY = {
    "news": fetch_feeds,
    # Add more services here
}

def get_relevant_services(user_message):
    # Use OpenAI to determine relevant services
    prompt = (
        "Based on the following message, determine which services are relevant. "
        "Available services are: news. "
        "Message: " + user_message
    )
    
    # Generate a response from OpenAI
    analysis_response = generate_ai_response(prompt)
    
    # Parse the response to determine relevant services
    relevant_services = []
    for trigger, service in SERVICE_REGISTRY.items():
        if trigger in analysis_response.lower():
            relevant_services.append(service)
    
    return relevant_services