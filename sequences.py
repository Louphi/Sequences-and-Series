import math
import matplotlib.pyplot as plt

class Sequence:
    def __init__(self, definition, recursive=False, initial_terms=None):
        self.definition = definition
        self.recursive = recursive
        self.initial_terms = initial_terms if initial_terms else []
        self.sequence = []

    def generate_terms(self, start, end):
        n = end - start + 1
        if self.recursive:
            self.sequence = self.initial_terms[:]
            for i in range(len(self.initial_terms), n):
                self.sequence.append(self.definition(self.sequence, i))
        else:
            self.sequence = [self.definition(i) for i in range(start, end + 1)]
        return self.sequence

    def plot_terms(self, start, end):
        terms = self.generate_terms(start, end)
        plt.figure(figsize=(10, 6))
        plt.scatter(range(start, end + 1), terms, color='blue', marker='o')

        plt.axhline(0, color='black', linewidth=1.5)
        plt.axvline(0, color='black', linewidth=1.5)
        
        plt.title('Sequence Plot', fontsize=16)
        plt.xlabel('n', fontsize=14)
        plt.ylabel('a(n)', fontsize=14)
        plt.grid(True, which='both', linestyle='--', linewidth=0.5)
        plt.show()

# Example usage

# Alternating sequence
# alt_seq = Sequence(lambda n: (1/n))
# alt_seq.plot_terms(start=5, end=20)

# Lucas sequence
# lucas_seq = Sequence(lambda seq, n: seq[n-1] + seq[n-2], recursive=True, initial_terms=[2, 1])
# lucas_seq.plot_terms(20, start=5)

# Geometric sequence
# a = 10
# r = 100/98
# geo_seq = Sequence(lambda n: a*r**(n-1))
# geo_seq.plot_terms(20, start=5)

# Generalized Bertrand sequence
# bertrand_seq = Sequence(lambda n: 1/(n*math.log(n)*math.log(math.log(n))*math.log(math.log(math.log(n)))*math.log(math.log(math.log(math.log(n))))))
# bertrand_seq.plot_terms(100000, start=10000)