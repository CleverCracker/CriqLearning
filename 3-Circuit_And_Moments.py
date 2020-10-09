import cirq

circuit = cirq.Circuit()

# * Apending Circuits
circuit.append(cirq.H(q) for q in cirq.LineQubit.range(3))
print(circuit)

# * Circuit Directly as Well
print(cirq.Circuit(cirq.SWAP(q, q+1) for q in cirq.LineQubit.range(3)))
# * Create  each gate in a Separate Momnet
print(cirq.Circuit(cirq.Moment([cirq.H(q)]) for q in cirq.LineQubit.range(3)))

# * Circuit and Device
# * Example Using  Foxtail Device
q0 = cirq.GridQubit(0, 0)
q1 = cirq.GridQubit(0, 1)
q2 = cirq.GridQubit(0, 2)
adjecent_op = cirq.CZ(q0, q1)
nonadjacent_op = cirq.CZ(q0, q2)
# * Unconstraint Circuit with no Device

free_circuit = cirq.Circuit()
# Both Operation or Allowed
free_circuit.append(adjecent_op)
free_circuit.append(nonadjacent_op)
print('Unconstrained Device:')
print(free_circuit)

# * Circuit Using Foxtail Device
foxtail_circuit = cirq.Circuit(device=cirq.google.Foxtail)
print('Foxtail Device:')
foxtail_circuit.append(adjecent_op)
print(foxtail_circuit)
try:
    # Not allowed, will throw exception
    foxtail_circuit.append(nonadjacent_op)
except ValueError as e:
    print('Not allowed. %s' % e)
# *
# *
