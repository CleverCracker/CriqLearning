"""Demonstrates Deutsch's algorithm.
   Deutsch's algorithm is one of the simplest demonstrations of quantum parallelism
   and interference. It takes a black-box oracle implementing a Boolean function
   f(x), and determines whether f(0) and f(1) have the same parity using just one
   query.  This version of Deutsch's algorithm is a simplified and improved version
   from Nielsen and Chuang's textbook.
   === REFERENCE ===
   https://en.wikipedia.org/wiki/Deutsch–Jozsa_algorithm
   Deutsch, David. "Quantum theory, the Church-Turing Principle and the universal
   quantum computer." Proc. R. Soc. Lond. A, 400:97, 1985.
   === EXAMPLE OUTPUT ===
   Secret function:
   f(x) = <0, 1>
   Circuit:
   0: ───────H───@───H───M('result')───
                 │
   1: ───X───H───X─────────────────────
   Result f(0)⊕f(1):
   result=1
   """

import random
import cirq
from cirq import H, X, CNOT, measure


def main():
    """
    Deursh David Problem Algo using  Quantum Computing
    """
    # Chose Qubit to use
    q0, q1 = cirq.LineQubit.range(2)

    # Pick a secret 2 bit funtion and Create a circuit to query the orecle
    secret_funtion = [random.randint(0, 1) for _ in range(2)]
    # print(secret_funtion)
    print()
    oracle = make_oracle(q0, q1, secret_funtion)
    print('Secret Fucntion:\nf(x) = <{}>'.format(
        ', '.join(str(e) for e in secret_funtion)))

    circuit = make_deutsch_circuit(q0, q1, oracle)

    print('Circuit:')
    print(circuit)

    # Simulation the Circuit
    simulator = cirq.Simulator()
    result = simulator.run(circuit)
    print('Result of f(0)⊕f(1):')
    print(result)


def make_oracle(q0, q1, secret_funtion):
    """
    Gate Implementaion for Secret Function f(x).
    """
    if secret_funtion[0]:
        yield [CNOT(q0, q1, X(q1))]
    if secret_funtion[1]:
        yield [CNOT(q0, q1)]


def make_deutsch_circuit(q0, q1, oracle):
    """
    Deutsch Circuit
    """

    c = cirq.Circuit()

    # Initialization of Qubit
    c.append([X(q1), H(q1), H(q0)])
    print(oracle)
    c.append(oracle)

    # Measure the X Basic
    c.append([H(q0), measure(q0, key='result')])
    return c


if __name__ == "__main__":
    main()
