import cirq


def main():
    """
    Main Function For Hello World
    === EXAMPLE OUTPUT ===
    Circuit:
    (0, 0): ───X^0.5───M('m')───
    Results:
    m=11000111111011001000
    """
    # * Pick a Qubit
    qubit = cirq.GridQubit(0, 0)

    # * Create a Circuit
    circuit = cirq.Circuit(
        cirq.X(qubit)**0.5,
        cirq.measure(qubit, key='m')
    )

    print('Circuit:')
    print(circuit)

    # * Simulate the Circuit Servel Time
    simulate = cirq.Simulator()
    result = simulate.run(circuit, repetitions=20)
    print('Result:')
    print(result)

# * Main Fucntin Run


if __name__ == "__main__":
    main()
