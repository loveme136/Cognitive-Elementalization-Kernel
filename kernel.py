"""
PROJECT: Cognitive Elementalization Kernel (Sandbox v0.1)
ARCHITECTURE: Civilization OS / Mental Decentralization
AUTHOR: The Architect (Person 1) & Senior Engineer AI
STATUS: STABLE_KERNEL_BETA
"""

class ARIS_Kernel:
    def __init__(self, node_id):
        self.node_id = node_id

    def compute_value(self, target_object, internal_threshold):
        perceived_quality = target_object.get('quality', 0)
        is_compliant = perceived_quality >= internal_threshold
        return {
            "element": "VALUE",
            "status": "COMPLIANT" if is_compliant else "REJECTED",
            "delta": perceived_quality - internal_threshold,
            "log": "Passes internal guidelines" if is_compliant else "Below threshold: Zero Value"
        }

    def compute_success(self, actual_output, self_threshold):
        is_success = actual_output >= self_threshold
        return {
            "element": "SUCCESS",
            "state": "TERMINATED_SUCCESS" if is_success else "ITERATING_BRIDGE",
            "log": "Self-threshold reached: Success verified" if is_success else "Below threshold: Accumulating 'Bridge' data"
        }

    def compute_regret(self, investment_mass, recovery_speed, has_failed=True):
        if not has_failed: return None
        regret_index = investment_mass / max(recovery_speed, 0.001)
        return {
            "element": "REGRET",
            "intensity": regret_index,
            "status": "CRITICAL_SHUTDOWN" if regret_index > 73 else "NOMINAL_FEEDBACK",
            "log": "High intensity: Requires assist" if regret_index > 73 else "Convert to success-bridge data"
        }

    def compute_labor(self, task_tier):
        evolution_stages = {"survival": 1, "convenience": 2, "aesthetic": 3, "power": 4}
        tier_level = evolution_stages.get(task_tier.lower(), 1)
        return {
            "element": "LABOR",
            "tier": tier_level,
            "instruction": "Migrate to Tier 3+ (Intellectual/Aesthetic) for alignment." if tier_level < 3 else "High-tier contribution active."
        }

    def compute_will(self, demand_intensity):
        is_ignited = demand_intensity > 50
        return {
            "element": "WILL",
            "propulsion": "ACTIVE" if is_ignited else "IDLE",
            "force_vector": demand_intensity
        }
