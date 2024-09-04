import matplotlib.pyplot as plt

class Sequence:
    def __init__(self, definition, recursive=False, initial_terms=None):
        self.definition = definition
        self.recursive = recursive
        self.initial_terms = initial_terms if initial_terms else []
        self.sequence = []

    def generate_terms(self, n):
        if self.recursive:
            self.sequence = self.initial_terms[:]
            for i in range(len(self.initial_terms), n):
                self.sequence.append(self.definition(self.sequence, i))
        else:
            self.sequence = [self.definition(i) for i in range(1, n + 1)]
        return self.sequence

    def plot(self, n):
        terms = self.generate_terms(n)
        plt.figure(figsize=(10, 6))
        plt.scatter(range(1, n + 1), terms, color='blue', marker='o')
        
        for i, term in enumerate(terms, start=1):
            plt.annotate(f'{term:.2f}', (i, term), textcoords="offset points", xytext=(0,10), ha='center')
        
        plt.axhline(0, color='black', linewidth=1.5)
        plt.axvline(0, color='black', linewidth=1.5)
        
        plt.title('Sequence Plot', fontsize=16)
        plt.xlabel('n', fontsize=14)
        plt.ylabel('a(n)', fontsize=14)
        plt.grid(True, which='both', linestyle='--', linewidth=0.5)
        plt.show()

# Example usage

# Alternating sequence
# alt_seq = Sequence(lambda n: (1/n)*(-1)**n)
# alt_seq.plot(20)

# Lucas sequence
# lucas_seq = Sequence(lambda seq, n: seq[n-1] + seq[n-2], recursive=True, initial_terms=[2, 1])
# lucas_seq.plot(20)

# Geometric sequence
a = 10
r = 100/98
geo_seq = Sequence(lambda n: a*r**(n-1))
geo_seq.plot(20)