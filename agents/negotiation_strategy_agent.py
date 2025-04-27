# agents/negotiation_strategy_agent.py

def create_negotiation_strategy(valuations):
    strategies = []
    for val in valuations:
        strategy = {
            "name": val["name"],
            "offer_price": val["estimated_value"] * 0.95  # Aim 5% discount
        }
        strategies.append(strategy)
    return strategies
