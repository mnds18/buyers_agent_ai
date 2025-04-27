# agents/verification_agents.py

def verify_output(output):
    if not output:
        raise ValueError("Verification Failed: Output is empty!")
    return True
