import cirq

# * Named QUbit
q0 = cirq.NamedQubit('source')
q1 = cirq.NamedQubit('target')

# * line Qubits
q3 = cirq.LineQubit(3)

# * Line Qubit with Range
q0, q1, q2 = cirq.LineQubit.range(3)

# * Grid Quibits
q4_5 = cirq.GridQubit(4, 5)

# * Grid Quibits Square
qsq_4 = cirq.GridQubit.square(4)
