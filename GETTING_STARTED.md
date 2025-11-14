# Getting Started with Lie Algebras and SageMath

This guide will help you get started with learning Lie algebras using SageMath.

## What You'll Learn

By following this guide, you will:
1. Set up a SageMath environment using conda
2. Understand basic Lie algebra concepts
3. Use SageMath to explore Lie algebra structures
4. Work through practical examples

## Step 1: Installation

### Install Conda

If you don't have conda installed, download and install [Miniconda](https://docs.conda.io/en/latest/miniconda.html) or [Anaconda](https://www.anaconda.com/products/distribution).

### Create the SageMath Environment

```bash
# Clone the repository
git clone https://github.com/wenluowang/lie-algebra.git
cd lie-algebra

# Create the conda environment
conda env create -f environment.yml

# Activate the environment
conda activate lie-algebra-sage

# Verify installation
sage --version
```

If the environment creation fails, try manual installation:

```bash
conda create -n lie-algebra-sage python=3.11
conda activate lie-algebra-sage
conda install -c conda-forge sage
conda install -c conda-forge jupyter notebook
```

## Step 2: Choose Your Learning Path

### Option A: Interactive Notebook (Recommended for Beginners)

Start Jupyter notebook:
```bash
jupyter notebook
```

Open `lie_algebra_tutorial.ipynb` and work through the cells interactively.

### Option B: Python Scripts

Run the example scripts in order:
```bash
cd examples
sage example_01_basics.py
sage example_02_root_systems.py
sage example_03_matrix_representations.py
sage example_04_classical_algebras.py
```

### Option C: SageMath REPL

Start the SageMath command-line interface:
```bash
sage
```

Then type commands interactively. For example:
```python
sage: L = LieAlgebra(QQ, cartan_type=['A', 1])
sage: L
Lie algebra of ['A', 1] in the Chevalley basis
sage: e1 = L.e(1)
sage: f1 = L.f(1)
sage: e1.bracket(f1)
h1
```

## Step 3: Basic Concepts

### What is a Lie Algebra?

A **Lie algebra** is a vector space **g** with a binary operation `[·,·]` (called the Lie bracket) satisfying:

1. **Bilinearity**: The bracket is linear in both arguments
2. **Alternativity**: `[x, x] = 0` for all x
3. **Jacobi identity**: `[x, [y, z]] + [y, [z, x]] + [z, [x, y]] = 0`

### Simple Example: sl(2)

The simplest nontrivial Lie algebra is **sl(2)**, the Lie algebra of 2×2 traceless matrices.

```python
from sage.all import *

# Create sl(2)
L = LieAlgebra(QQ, cartan_type=['A', 1])

# Get the standard generators
e = L.e(1)  # raising operator
f = L.f(1)  # lowering operator
h = L.h(1)  # Cartan element

# Compute brackets
print(f"[e, f] = {e.bracket(f)}")  # equals h
print(f"[h, e] = {h.bracket(e)}")  # equals 2e
print(f"[h, f] = {h.bracket(f)}")  # equals -2f
```

### Matrix Representation

You can also work with explicit matrices:

```python
from sage.all import *

E = matrix(QQ, [[0, 1], [0, 0]])
F = matrix(QQ, [[0, 0], [1, 0]])
H = matrix(QQ, [[1, 0], [0, -1]])

# Lie bracket [X, Y] = XY - YX
def bracket(X, Y):
    return X*Y - Y*X

print(bracket(E, F))  # equals H
```

## Step 4: Explore More

### Classical Lie Algebras

SageMath supports all classical Lie algebras:

- **A_n** (type A): sl(n+1) - special linear
- **B_n** (type B): so(2n+1) - odd orthogonal
- **C_n** (type C): sp(2n) - symplectic
- **D_n** (type D): so(2n) - even orthogonal

```python
# Create different types
A3 = LieAlgebra(QQ, cartan_type=['A', 3])  # sl(4)
B2 = LieAlgebra(QQ, cartan_type=['B', 2])  # so(5)
C2 = LieAlgebra(QQ, cartan_type=['C', 2])  # sp(4)
D3 = LieAlgebra(QQ, cartan_type=['D', 3])  # so(6)
```

### Root Systems

Root systems are fundamental to understanding Lie algebras:

```python
# Create a root system
R = RootSystem(['A', 2])

# Cartan matrix
print(R.cartan_matrix())

# Positive roots
roots = R.root_lattice().positive_roots()
print(list(roots))
```

### Exceptional Lie Algebras

SageMath also supports exceptional Lie algebras:

```python
E6 = LieAlgebra(QQ, cartan_type=['E', 6])
E7 = LieAlgebra(QQ, cartan_type=['E', 7])
E8 = LieAlgebra(QQ, cartan_type=['E', 8])
F4 = LieAlgebra(QQ, cartan_type=['F', 4])
G2 = LieAlgebra(QQ, cartan_type=['G', 2])
```

## Step 5: Practice Exercises

### Exercise 1: Verify the Jacobi Identity

Pick any Lie algebra and three elements, then verify the Jacobi identity holds.

```python
L = LieAlgebra(QQ, cartan_type=['A', 2])
x, y, z = L.e(1), L.e(2), L.f(1)

jacobi = x.bracket(y.bracket(z)) + y.bracket(z.bracket(x)) + z.bracket(x.bracket(y))
print(f"Jacobi identity satisfied? {jacobi == 0}")
```

### Exercise 2: Explore Dimensions

Verify the dimension formula for sl(n): dim(sl(n)) = n² - 1

```python
for n in range(2, 7):
    L = LieAlgebra(QQ, cartan_type=['A', n-1])
    expected = n**2 - 1
    actual = L.dimension()
    print(f"sl({n}): expected {expected}, got {actual}, match: {expected == actual}")
```

### Exercise 3: Matrix Lie Algebras

Create your own matrix Lie algebra and verify it's closed under the Lie bracket.

### Exercise 4: Root System Analysis

Pick a root system and:
- Count the positive roots
- Compute the Cartan matrix
- Draw the Dynkin diagram (on paper or describe it)

## Common Issues and Solutions

### Issue: "sage: command not found"

Make sure the conda environment is activated:
```bash
conda activate lie-algebra-sage
```

### Issue: Import errors

If you're using a Python script, make sure to import from sage:
```python
from sage.all import *
```

### Issue: Conda environment creation fails

Try manual installation:
```bash
conda create -n lie-algebra-sage python=3.11
conda activate lie-algebra-sage
conda install -c conda-forge sage
```

## Next Steps

1. Work through all examples in the `examples/` directory
2. Complete the Jupyter notebook tutorial
3. Read the main [README.md](README.md) for more resources
4. Explore the [SageMath documentation](https://doc.sagemath.org/)
5. Try implementing your own Lie algebra computations

## Additional Resources

- [SageMath Tutorial](https://doc.sagemath.org/html/en/tutorial/)
- [Lie Algebras in SageMath](https://doc.sagemath.org/html/en/reference/algebras/lie_algebras.html)
- [Root Systems Documentation](https://doc.sagemath.org/html/en/reference/combinat/sage/combinat/root_system/root_system.html)
- James Humphreys, "Introduction to Lie Algebras and Representation Theory"

## Getting Help

- SageMath documentation: `https://doc.sagemath.org/`
- SageMath ask forum: `https://ask.sagemath.org/`
- Use `?` in sage for help: `LieAlgebra?`
- Use tab completion to explore: `L.<tab>`

Happy learning!
