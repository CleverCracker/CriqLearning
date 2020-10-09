import cirq

# * Example Gates
notGate = cirq.CNOT
pauliZ = cirq.Z

# * Using  Exponentiation to get square root gates
sqrtXGates = cirq.X**0.5
sqrtIswap = cirq.ISWAP**0.5

# * Some Gates That takes Parameters
sqrt_sqrt_y = cirq.YPowGate(exponent=0.25)

# * Example Opration
q0, q1 = cirq.LineQubit.range(2)
z_op = cirq.Z(q0)
not_op = cirq.CNOT(q0, q1)
sqrt_iswap_op = sqrtIswap(q0, q1)
print(sqrt_iswap_op)
# *
