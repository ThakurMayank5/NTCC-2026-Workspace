# Optimal Equilibrium for Pigou Network
# Socially Optimal Routing

DEMAND = 1.0

def cost_path1(flow):
	return flow

def cost_path2(flow):
	return 1.0

def cost_path1_derivative(flow):
	return 1.0

def cost_path2_derivative(flow):
	return 0.0

def marginal_cost_path1(flow):
	return cost_path1(flow) + flow * cost_path1_derivative(flow)

def marginal_cost_path2(flow):
	return cost_path2(flow) + flow * cost_path2_derivative(flow)

def total_cost(flow_on_path1, demand=DEMAND):
	flow_on_path2 = demand - flow_on_path1
	return (
		flow_on_path1 * cost_path1(flow_on_path1)
		+ flow_on_path2 * cost_path2(flow_on_path2)
	)

def social_optimum(demand=DEMAND, tol=1e-9, max_iter=100):
	def marginal_gap(flow_on_path1):
		return marginal_cost_path1(flow_on_path1) - marginal_cost_path2(demand - flow_on_path1)

	if marginal_gap(demand) <= 0:
		return demand
	if marginal_gap(0.0) >= 0:
		return 0.0

	lo, hi = 0.0, demand
	for _ in range(max_iter):
		mid = (lo + hi) / 2.0
		gap = marginal_gap(mid)
		if abs(gap) <= tol:
			return mid
		if gap > 0:
			hi = mid
		else:
			lo = mid
	return (lo + hi) / 2.0

if __name__ == "__main__":
	flow = social_optimum()
	share = flow / DEMAND if DEMAND else 0.0
	cost = total_cost(flow)
	print(f"Socially optimal flow on path1: {share:.6f}")
	print(f"Total cost: {cost:.6f}")

