from qiskit import QuantumCircuit, Aer, execute

# Create 1-qubit, 1-classical-bit circuit
qc = QuantumCircuit(1, 1)
qc.h(0)          # Apply Hadamard gate
qc.measure(0, 0) # Measure qubit 0 into classical bit 0

# Use Aer simulator
simulator = Aer.get_backend('aer_simulator')

# Run the circuit
job = execute(qc, simulator)
result = job.result()

# Get counts (measurement results)
counts = result.get_counts()
print(counts)

