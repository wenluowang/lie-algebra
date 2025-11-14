# Lie Algebra with SageMath

A comprehensive guide to learning Lie algebra using SageMath, a powerful open-source mathematics software system.

## Table of Contents
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Lie Algebra Basics](#lie-algebra-basics)
- [Examples](#examples)
- [Resources](#resources)

## Installation

### Prerequisites
- [Conda](https://docs.conda.io/en/latest/miniconda.html) or [Anaconda](https://www.anaconda.com/products/distribution) installed on your system

### Installing SageMath with Conda

1. **Clone this repository:**
   ```bash
   git clone https://github.com/wenluowang/lie-algebra.git
   cd lie-algebra
   ```

2. **Create the conda environment:**
   ```bash
   conda env create -f environment.yml
   ```

3. **Activate the environment:**
   ```bash
   conda activate lie-algebra-sage
   ```

4. **Verify the installation:**
   ```bash
   sage --version
   ```

### Alternative Installation Methods

If you encounter issues with the environment file, you can install SageMath manually:

```bash
# Create a new environment
conda create -n lie-algebra-sage python=3.11

# Activate the environment
conda activate lie-algebra-sage

# Install SageMath from conda-forge
conda install -c conda-forge sage

# Install Jupyter for interactive notebooks
conda install -c conda-forge jupyter notebook
```

## Getting Started

### Starting SageMath

After activating the conda environment, you can start SageMath in several ways:

1. **Command-line interface:**
   ```bash
   sage
   ```

2. **Jupyter Notebook:**
   ```bash
   jupyter notebook
   ```

3. **Python with SageMath:**
   ```python
   from sage.all import *
   ```

## Lie Algebra Basics

### What is a Lie Algebra?

A Lie algebra is a vector space **g** over a field **F** equipped with a binary operation called the Lie bracket `[·,·]: g × g → g` that satisfies:

1. **Bilinearity**: `[ax + by, z] = a[x,z] + b[y,z]` and `[z, ax + by] = a[z,x] + b[z,y]`
2. **Alternativity**: `[x, x] = 0` for all x ∈ g
3. **Jacobi identity**: `[x, [y, z]] + [y, [z, x]] + [z, [x, y]] = 0`

### Common Lie Algebras in SageMath

SageMath has built-in support for many classical Lie algebras:

- **sl(n)**: Special linear Lie algebra
- **so(n)**: Special orthogonal Lie algebra  
- **sp(2n)**: Symplectic Lie algebra
- **gl(n)**: General linear Lie algebra

## Examples

### Example 1: Creating a Simple Lie Algebra

```python
# Start SageMath or run in Jupyter with SageMath kernel
from sage.all import *

# Create sl(2) - the special linear Lie algebra of 2x2 matrices
L = LieAlgebra(QQ, cartan_type=['A', 1])
print(f"Lie algebra: {L}")

# Get the basis elements
basis = L.basis()
print(f"Basis elements: {basis}")
```

### Example 2: Computing Lie Brackets

```python
from sage.all import *

# Create the Lie algebra sl(3)
L = LieAlgebra(QQ, cartan_type=['A', 2])

# Get generators
e1, e2 = L.e(1), L.e(2)
f1, f2 = L.f(1), L.f(2)
h1, h2 = L.h(1), L.h(2)

# Compute Lie bracket [e1, f1]
bracket = e1.bracket(f1)
print(f"[e1, f1] = {bracket}")

# Verify Jacobi identity
x, y, z = e1, e2, f1
jacobi = x.bracket(y.bracket(z)) + y.bracket(z.bracket(x)) + z.bracket(x.bracket(y))
print(f"Jacobi identity check (should be 0): {jacobi}")
```

### Example 3: Root Systems

```python
from sage.all import *

# Create the root system for type A2 (sl(3))
R = RootSystem(['A', 2])
print(f"Root system: {R}")

# Get the root space
root_space = R.root_space()
print(f"Root space: {root_space}")

# Get positive roots
positive_roots = R.root_lattice().positive_roots()
print(f"Positive roots: {list(positive_roots)}")

# Get the Cartan matrix
cartan_matrix = R.cartan_matrix()
print(f"Cartan matrix:\n{cartan_matrix}")
```

### Example 4: Representations

```python
from sage.all import *

# Create sl(2)
L = LieAlgebra(QQ, cartan_type=['A', 1])

# Work with weight spaces
P = L.cartan_type().root_system().weight_lattice()
print(f"Weight lattice: {P}")

# Fundamental weights
fundamental_weights = P.fundamental_weights()
print(f"Fundamental weights: {fundamental_weights}")
```

### Example 5: Matrix Lie Algebras

```python
from sage.all import *

# Define sl(2) using matrices
def sl2_bracket(X, Y):
    """Compute the Lie bracket [X,Y] = XY - YX"""
    return X*Y - Y*X

# Define basis elements of sl(2)
E = matrix(QQ, [[0, 1], [0, 0]])  # Raising operator
F = matrix(QQ, [[0, 0], [1, 0]])  # Lowering operator
H = matrix(QQ, [[1, 0], [0, -1]]) # Cartan element

print("Basis of sl(2):")
print(f"E = \n{E}\n")
print(f"F = \n{F}\n")
print(f"H = \n{H}\n")

# Compute brackets
print("Lie brackets:")
print(f"[E, F] = \n{sl2_bracket(E, F)}\n")
print(f"[H, E] = \n{sl2_bracket(H, E)}\n")
print(f"[H, F] = \n{sl2_bracket(H, F)}\n")
```

## Learning Path

### Beginner Level
1. Understand basic linear algebra concepts (vector spaces, matrices)
2. Learn about the Lie bracket operation
3. Study simple examples like sl(2)
4. Explore root systems for classical Lie algebras

### Intermediate Level
1. Study classification of simple Lie algebras
2. Learn about Cartan subalgebras and root decomposition
3. Explore representations and weight spaces
4. Understand Dynkin diagrams

### Advanced Level
1. Study universal enveloping algebras
2. Learn about quantum groups
3. Explore applications in physics (gauge theory, particle physics)
4. Study infinite-dimensional Lie algebras

## Resources

### Documentation
- [SageMath Official Documentation](https://doc.sagemath.org/)
- [SageMath Lie Algebras Reference](https://doc.sagemath.org/html/en/reference/algebras/lie_algebras.html)
- [SageMath Root Systems](https://doc.sagemath.org/html/en/reference/combinat/sage/combinat/root_system/root_system.html)

### Books
- "Introduction to Lie Algebras and Representation Theory" by James Humphreys
- "Lie Algebras" by Nathan Jacobson
- "Representation Theory: A First Course" by William Fulton and Joe Harris

### Online Resources
- [SageMath Tutorials](https://doc.sagemath.org/html/en/tutorial/)
- [Lie Theory Tutorial](https://doc.sagemath.org/html/en/thematic_tutorials/lie.html)

## Contributing

Feel free to contribute examples, tutorials, or improvements to this repository!

## License

This project is open source and available for educational purposes.