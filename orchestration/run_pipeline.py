# orchestration/run_pipeline.py

from agents.client_profile_agent import collect_client_profile
from agents.market_data_agent import fetch_market_data
from agents.property_sourcing_agent import source_properties
from agents.property_valuation_agent import valuate_properties
from agents.risk_due_diligence_agent import assess_risks
from agents.negotiation_strategy_agent import create_negotiation_strategy
from agents.legal_compliance_agent import check_legal_compliance
from agents.deal_closure_agent import finalize_deals
from agents.feedback_agent import collect_feedback
from agents.verification_agents import verify_output
from agents.llm_summary_agent import summarize_properties
from agents.suburb_ranking_agent import recommend_suburbs

def run_buyers_agent_pipeline(budget=None, location=None, investment_goal=None):
    from agents.client_profile_agent import collect_client_profile
    from agents.market_data_agent import fetch_market_data
    from agents.property_sourcing_agent import source_properties
    from agents.property_valuation_agent import valuate_properties
    from agents.risk_due_diligence_agent import assess_risks
    from agents.negotiation_strategy_agent import create_negotiation_strategy
    from agents.legal_compliance_agent import check_legal_compliance
    from agents.deal_closure_agent import finalize_deals
    from agents.feedback_agent import collect_feedback
    from agents.llm_summary_agent import summarize_properties
    from agents.verification_agents import verify_output

    # Step 0: Recommend Suburbs First
    recommended_suburbs = recommend_suburbs(goal=investment_goal, top_n=5)
    print("🔎 Recommended Suburbs Based on Your Goal:", recommended_suburbs)

    # Assume user selects first suburb
    selected_suburb = recommended_suburbs[0]["Suburb"]
    print(f"📍 Selected suburb to search properties in: {selected_suburb}")

    # Step 1: Get Client Profile
    client_profile = collect_client_profile()
    
    # Override defaults if user provided filters
    if budget:
        client_profile["budget"] = budget
    if location:
        client_profile["location"] = location
    if investment_goal:
        client_profile["investment_goal"] = investment_goal

    verify_output(client_profile)

    # Step 2: Get Market Data
    market_data = fetch_market_data(client_profile["location"])
    verify_output(market_data)

    # Step 3: Source Properties
    properties = source_properties(client_profile["location"], client_profile["budget"])
    verify_output(properties)

    # Step 4: Valuate Properties
    valuations = valuate_properties(properties)
    verify_output(valuations)

    # Step 5: Risk Due Diligence
    risks = assess_risks(properties)
    verify_output(risks)

    # Step 6: Negotiation Strategies
    strategies = create_negotiation_strategy(valuations)
    verify_output(strategies)

    # Step 7: Legal Compliance
    compliance = check_legal_compliance(properties)
    verify_output(compliance)

    # Step 8: Finalize Deals
    deals = finalize_deals(strategies)
    verify_output(deals)

    # Step 9: Collect Feedback
    feedback = collect_feedback(deals)
    verify_output(feedback)

    # Step 10: LLM Summary
    summary = summarize_properties(properties)

    return {
        "Profile": client_profile,
        "MarketData": market_data,
        "Properties": properties,
        "Valuations": valuations,
        "Risks": risks,
        "Strategies": strategies,
        "Compliance": compliance,
        "Deals": deals,
        "Feedback": feedback,
        "LLM_Summary": summary,
    }


if __name__ == "__main__":
    results = run_buyers_agent_pipeline()
    for key, value in results.items():
        print(f"\n{key}: {value}")
