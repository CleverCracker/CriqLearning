import cirq

# * Create a Circuit to Generate Bell State:
# * sqrt(2) *(|00> + |11> )
bell_circuit = cirq.Circuit()
q0, q1 = cirq.LineQubit.range(2)
bell_circuit.append(cirq.H(q0))
bell_circuit.append(cirq.CNOT(q0, q1))

# * Initializer Simulator
s = cirq.Simulator()

print('Simulator the Circuit')
result = s.simulate(bell_circuit)
print(result)
print()

# * For Simpling we need to add a measurement at end

bell_circuit.append(cirq.measure(q0, q1, key='result'))

print('Sample the Circuit:')
samples = s.run(bell_circuit, repetitions=1000)
# * Printing Histogram Result
print(samples.histogram(key='result'))
