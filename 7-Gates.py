import cirq
import matplotlib.pyplot as plt

# Simple Circuit Found on Every Book

circuit = cirq.Circuit()
q0, q1, q2 = cirq.LineQubit.range(3)

circuit.append(cirq.H(q1))
circuit.append(cirq.CNOT(q1, q2))
circuit.append(cirq.CNOT(q0, q1))
circuit.append(cirq.H(q0))
circuit.append(cirq.measure(q0, q1, q2, key='result'))
simulateCircuit(circuit)
print(circuit)


def simulateCircuit(circuit):
    """
    Simulation of Circuit by Clever Cracker
    """
    s = cirq.Simulator()
    simulate = s.run(circuit, repetitions=1000)
    print(simulate.histogram(key='result'))
