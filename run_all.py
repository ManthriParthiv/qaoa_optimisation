from preprocessing.prepare_data import create_portfolio_problem
from processing.qaoa_runner import run_qaoa
from postprocessing.analyze import display_results

if __name__ == "__main__":
    expected_returns = [0.1, 0.2, 0.15, 0.12]
    covariance_matrix = [
        [0.005, -0.010, 0.004, -0.002],
        [-0.010, 0.040, -0.002, 0.004],
        [0.004, -0.002, 0.023, 0.002],
        [-0.002, 0.004, 0.002, 0.018]
    ]
    budget = 2

    qubo = create_portfolio_problem(expected_returns, covariance_matrix, budget)
    result = run_qaoa(qubo)
    display_results(result)