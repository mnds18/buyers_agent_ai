# agents/deal_closure_agent.py

def finalize_deals(strategies):
    deals = []
    for strat in strategies:
        deals.append({
            "property": strat["name"],
            "offer": strat["offer_price"]
        })
    return deals
