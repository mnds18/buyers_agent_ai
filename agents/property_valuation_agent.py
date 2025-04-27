# agents/property_valuation_agent.py

def valuate_properties(properties):
    valuations = []
    for prop in properties:
        valuation = {
            "name": prop["name"],
            "estimated_value": prop["price"] * 1.05  # 5% above listing price
        }
        valuations.append(valuation)
    return valuations
