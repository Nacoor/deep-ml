import numpy as np

def compute_chain_rule_gradient(functions: list[str], x: float) -> float:
	"""
	Compute derivative of composite functions using chain rule.
	
	Args:
		functions: List of function names (applied right to left)
		          Available: 'square', 'sin', 'exp', 'log'
		x: Point at which to evaluate derivative
	
	Returns:
		Derivative value at x
	
	Example:
		['sin', 'square'] represents sin(x²)
		['exp', 'sin', 'square'] represents exp(sin(x²))
	"""
	# Your code here
	func = {
		'square': lambda y: y ** 2,
		'sin': lambda y: np.sin(y),
		'exp': lambda y: np.exp(y),
		'log': lambda y: np.log(y)
	}

	deriv = {
		'square': lambda y: 2 * y,
		'sin': lambda y: np.cos(y),
		'exp': lambda y: np.exp(y),
		'log': lambda y: 1/y
	}

	result = 1

	for f in reversed(functions):
		result = result * deriv[f](x)
		x = func[f](x)
	
	return result