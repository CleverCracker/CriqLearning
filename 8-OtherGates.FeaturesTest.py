import cirq

circuit = cirq.Circuit()
print(cirq.unitary(cirq.S(cirq.LineQubit.range(1)[0])))
print(cirq.S(cirq.LineQubit.range(1)[0]))

print(cirq.unitary(cirq.X(cirq.LineQubit.range(1)[0])))
print(cirq.X(cirq.LineQubit.range(1)[0]))

# * Tells How Many Quibit Required
print(cirq.CCNOT.num_qubits())

# print(cirq.mixture(cirq.H(cirq.LineQubit.range(1)[0])))
q0, q1 = cirq.LineQubit.range(2)
circuit.append(cirq.X(q0).controlled_by(q1))
print(circuit)
