from kernel import ARIS_Kernel

def run_simulation():
    node = ARIS_Kernel(node_id="Alpha-01")
    
    print("--- SCENARIO: The 5 Million Wage Request ---")
    # A worker with a 500k standard (Social Std) requests 5M (Desired)
    greed_report = node.compute_greed(desired=5000000, social_std=500000, others_limit=500000)
    print(f"Result: {greed_report['status']} | Greed Index: {greed_report['index']}")
    
    print("\n--- SCENARIO: Integrity vs. Freedom ---")
    integrity = node.compute_integrity(current_action=100, anchor_point=50) # Self-monitoring failed
    freedom = node.compute_freedom() # Absolute Freedom is 100%
    
    if not integrity['active']:
        print("Reasoning: Freedom execution BLOCKED due to Integrity failure.")
    else:
        print("Reasoning: Freedom execution AUTHORIZED.")

    print("\n--- SCENARIO: Zero Flush (Hallucination Prevention) ---")
    uncertain_data = node.zero_flush(confidence_score=65) # Below 73% threshold
    print(f"Data Score: {uncertain_data['result']} | Reason: {uncertain_data['element']}")

if __name__ == "__main__":
    run_simulation()
