from sequences import Sequence
import matplotlib.pyplot as plt

class Series:
    def __init__(self, definition, start, end):
        self.definition = definition
        self.start = start
        self.end = end
    
    def generate_terms(self):
        sequence = Sequence(self.definition)
        return sequence.generate_terms(self.start, self.end)
    
    def generate_partial_sums(self):
        terms = self.generate_terms()
        partial_sums = [sum(terms[:i+1]) for i in range(len(terms))]
        return partial_sums
    
    def plot_partial_sums(self):
        partial_sums = self.generate_partial_sums()
        plt.scatter(range(self.start, self.end + 1), partial_sums, color='red', marker='o')

        plt.axhline(0, color='black', linewidth=1.5)
        plt.axvline(0, color='black', linewidth=1.5)

        plt.xlabel('Term')
        plt.ylabel('Partial Sum')
        plt.title('Partial Sums of the Series')
        plt.grid(True, which='both', linestyle='--', linewidth=0.5)
        plt.show()

series = Series(lambda n: 1 / (2**n), 1, 10)
series.plot_partial_sums()
