# agents/risk_due_diligence_agent.py

def assess_risks(properties):
    risks = []
    for prop in properties:
        risks.append({
            "name": prop["name"],
            "risk_level": "Low"  # Pretend all are low risk for now
        })
    return risks
