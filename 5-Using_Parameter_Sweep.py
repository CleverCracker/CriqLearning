import cirq
import matplotlib.pyplot as plt
import sympy

# * Perform an X Gate with variable exponent
q = cirq.GridQubit(1, 1)
circuit = cirq.Circuit(cirq.X(q) ** sympy.Symbol('t'),
                       cirq.measure(q, key='m'))

# * Sweep exponent from zero (off) to one (on) and back to two (off)
param_sweeep = cirq.Linspace('t', start=0, stop=2, length=200)

# * Simpulator the Sweep
s = cirq.Simulator()
trials = s.run_sweep(circuit, param_sweeep, repetitions=1000)

# * Plot All the Result
x_data = [trail.params['t'] for trail in trials]
y_data = [trial.histogram(key='m')[1] for trial in trials]
plt.scatter('t', 'p', data={'t': x_data, 'p': y_data})
# *
