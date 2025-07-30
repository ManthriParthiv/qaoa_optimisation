from qiskit.algorithms.minimum_eigensolvers import QAOA
from qiskit.primitives import Estimator
from qiskit_optimization.algorithms import MinimumEigenOptimizer
from qiskit.algorithms.optimizers import COBYLA
from qiskit.utils import algorithm_globals

def run_qaoa(qubo):
    """
    Runs the Quantum Approximate Optimization Algorithm (QAOA) on the given QUBO problem.
    """
    algorithm_globals.random_seed = 42
    
    # Use the Estimator primitive, as QuantumInstance is deprecated.
    estimator = Estimator()
    
    # Initialize QAOA with the estimator and optimizer.
    qaoa = QAOA(estimator=estimator, optimizer=COBYLA(), reps=1)
    
    # Use MinimumEigenOptimizer to solve the QUBO problem.
    optimizer = MinimumEigenOptimizer(qaoa)
    result = optimizer.solve(qubo)
    
    return result