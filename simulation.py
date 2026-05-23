from kernel import ARIS_Kernel

def run_simulation_v1_1():
    node = ARIS_Kernel(node_id="Alpha-02")
    
    print("--- SCENARIO 1: Vested Interest Directional Check ---")
    # Case A: Self is strict (90), Others are loose (50) -> NOT Vested Interest (Self-sacrifice)
    res_a = node.compute_vested_interest(self_threshold=90, others_threshold=50)
    # Case B: Self is loose (30), Others are strict (80) -> Vested Interest (Asymmetric Distortion)
    res_b = node.compute_vested_interest(self_threshold=30, others_threshold=80)
    
    print(f"Case A (Self 90/Others 50): {res_a['action']}")
    print(f"Case B (Self 30/Others 80): {res_b['action']} | Distortion: {res_b['distortion']}")
    
    print("\n--- SCENARIO 2: Envy-to-Jealousy Pipeline ---")
    envy_res = node.compute_envy(self_deficit=10, target_data="Target-X")
    jealousy_res = node.compute_jealousy(envy_res, intent_to_harm=True)
    print(f"Envy Status: {envy_res['active']} -> Jealousy Threat: {jealousy_res['status']}")

    print("\n--- SCENARIO 3: Zero Flush (30% Threshold) ---")
    data_35 = node.zero_flush(35) # Above 30, should survive
    data_25 = node.zero_flush(25) # Below 30, should be flushed
    print(f"Score 35: {data_35['result']} | Score 25: {data_25['result']} (Flushed)")

if __name__ == "__main__":
    run_simulation_v1_1()
