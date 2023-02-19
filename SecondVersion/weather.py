'''Calling the functions for Weather solution.'''
import calculator

c = calculator.Calculator('weather.dat', "Dy", "MxT", "MnT")
print("Day number of smallest temperature spread: ", c.ans)
