# Brute Force for Pigou Network

DEMAND = 1.0

def cost_path1(flow):
    return flow

def cost_path2(flow):
    return 1.0

def total_cost(flow_on_path1, demand=DEMAND):
    flow_on_path2 = demand - flow_on_path1
    return (
        flow_on_path1 * cost_path1(flow_on_path1)
        + flow_on_path2 * cost_path2(flow_on_path2)
    )

def brute_force_optimum(steps=10000, demand=DEMAND):
    best_flow = 0.0
    best_cost = float("inf")
    for i in range(steps + 1):
        flow_on_path1 = demand * i / steps
        cost = total_cost(flow_on_path1, demand)
        if cost < best_cost:
            best_cost = cost
            best_flow = flow_on_path1
    return best_flow, best_cost

if __name__ == "__main__":
    flow, cost = brute_force_optimum()
    share = flow / DEMAND if DEMAND else 0.0
    print(f"Brute-force optimum flow on path1: {share:.6f}")
    print(f"Total cost: {cost:.6f}")