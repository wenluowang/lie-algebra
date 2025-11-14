"""
Example 1: Basic Lie Algebra Operations with SageMath

This script demonstrates fundamental operations with Lie algebras using SageMath.
Run this script with: sage example_01_basics.py
"""

from sage.all import *

def main():
    print("=" * 60)
    print("Example 1: Basic Lie Algebra Operations")
    print("=" * 60)
    
    # Create sl(2) - the special linear Lie algebra
    print("\n1. Creating sl(2):")
    L = LieAlgebra(QQ, cartan_type=['A', 1])
    print(f"   Lie algebra: {L}")
    print(f"   Cartan type: {L.cartan_type()}")
    print(f"   Base ring: {L.base_ring()}")
    print(f"   Dimension: {L.dimension()}")
    
    # Get the generators
    print("\n2. Generators of sl(2):")
    e1 = L.e(1)
    f1 = L.f(1)
    h1 = L.h(1)
    print(f"   e1 (raising): {e1}")
    print(f"   f1 (lowering): {f1}")
    print(f"   h1 (Cartan): {h1}")
    
    # Compute Lie brackets
    print("\n3. Lie brackets:")
    print(f"   [e1, f1] = {e1.bracket(f1)}")
    print(f"   [h1, e1] = {h1.bracket(e1)}")
    print(f"   [h1, f1] = {h1.bracket(f1)}")
    
    # Verify Jacobi identity
    print("\n4. Verifying Jacobi identity:")
    x, y, z = e1, f1, h1
    jacobi = x.bracket(y.bracket(z)) + y.bracket(z.bracket(x)) + z.bracket(x.bracket(y))
    print(f"   [x,[y,z]] + [y,[z,x]] + [z,[x,y]] = {jacobi}")
    print(f"   Is zero? {jacobi == 0}")
    
    # Get all basis elements
    print("\n5. Full basis:")
    basis = L.basis()
    print(f"   Basis elements: {basis}")
    print(f"   Number of basis elements: {len(basis.list())}")
    
    print("\n" + "=" * 60)

if __name__ == "__main__":
    main()
