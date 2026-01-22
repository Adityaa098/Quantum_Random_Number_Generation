import pennylane as qml

# Define a quantum device with 1 qubit and 1000 shots (repetitions)
dev = qml.device("default.qubit", wires=1, shots=1000)

# Define a quantum node (circuit)
@qml.qnode(dev)
def quantum_random_circuit():
    qml.Hadamard(wires=0)   # Put the qubit into superposition
    return qml.sample(wires=0)  # Measure qubit 1000 times

# Generate random bits
random_bits = quantum_random_circuit()

print(random_bits)  # This is an array of 0s and 1s, your quantum random bits
