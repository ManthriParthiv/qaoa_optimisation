from qiskit_optimization.applications import PortfolioOptimization
from qiskit_optimization.converters import QuadraticProgramToQubo

def create_portfolio_problem(expected_returns, covariance_matrix, budget):
    portfolio = PortfolioOptimization(expected_returns, covariance_matrix, budget)
    qp = portfolio.to_quadratic_program()
    qp2qubo = QuadraticProgramToQubo()
    qubo = qp2qubo.convert(qp)
    return qubo