# Lie Algebra Examples with SageMath

This directory contains example scripts demonstrating various concepts in Lie algebra theory using SageMath.

## Prerequisites

Make sure you have SageMath installed and the conda environment activated:

```bash
conda activate lie-algebra-sage
```

## Running the Examples

All examples can be run using the `sage` command:

```bash
sage example_01_basics.py
sage example_02_root_systems.py
sage example_03_matrix_representations.py
sage example_04_classical_algebras.py
```

## Example Descriptions

### Example 1: Basic Lie Algebra Operations (`example_01_basics.py`)

This example covers:
- Creating simple Lie algebras (sl(2))
- Working with generators (e, f, h)
- Computing Lie brackets
- Verifying the Jacobi identity
- Exploring basis elements

**Key concepts**: Lie bracket, generators, Jacobi identity

### Example 2: Root Systems (`example_02_root_systems.py`)

This example explores:
- Root systems for types A, B, C, D
- Cartan matrices
- Dynkin diagrams
- Simple and positive roots
- Computing Lie algebra dimensions from root systems

**Key concepts**: Root systems, Cartan matrix, Dynkin diagram, simple roots

### Example 3: Matrix Representations (`example_03_matrix_representations.py`)

This example demonstrates:
- Matrix representation of sl(2)
- Basis of sl(3) using matrices
- so(3) as antisymmetric 3×3 matrices
- Verifying structure relations
- Computing Lie brackets for matrices

**Key concepts**: Matrix Lie algebras, structure constants, antisymmetric matrices

### Example 4: Classical Lie Algebras (`example_04_classical_algebras.py`)

This example surveys:
- The four classical series: A_n, B_n, C_n, D_n
- Dimension formulas for each type
- Detailed analysis of A2 (sl(3))
- Comparison table of classical algebras

**Key concepts**: Classical Lie algebras, dimension formulas, Cartan classification

## Learning Path

We recommend going through the examples in order:

1. Start with `example_01_basics.py` to understand fundamental operations
2. Move to `example_02_root_systems.py` to learn about the structure theory
3. Explore `example_03_matrix_representations.py` for concrete realizations
4. Finally, review `example_04_classical_algebras.py` for the big picture

## Additional Resources

- Main repository [README.md](../README.md)
- Interactive [Jupyter notebook tutorial](../lie_algebra_tutorial.ipynb)
- [SageMath Documentation](https://doc.sagemath.org/)

## Exercises

Try modifying these examples to:

1. Compute Lie brackets for larger algebras (e.g., sl(4), so(7))
2. Verify the Jacobi identity for different triples of elements
3. Construct matrix representations for other Lie algebras
4. Explore exceptional Lie algebras (E6, E7, E8, F4, G2)
5. Compute the Killing form for various Lie algebras

## Tips

- Use `sage -ipython` for an interactive IPython session with SageMath
- Use `sage -notebook` to work with Jupyter notebooks
- Refer to SageMath documentation with `?` (e.g., `LieAlgebra?`)
- Use tab completion to explore available methods
