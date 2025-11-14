"""
Example 4: Classical Lie Algebras

This script explores the classical Lie algebra series A, B, C, D.
Run this script with: sage example_04_classical_algebras.py
"""

from sage.all import *

def main():
    print("=" * 60)
    print("Example 4: Classical Lie Algebras")
    print("=" * 60)
    
    print("\nThe classical Lie algebras are:")
    print("   A_n: sl(n+1) - special linear")
    print("   B_n: so(2n+1) - special orthogonal (odd)")
    print("   C_n: sp(2n) - symplectic")
    print("   D_n: so(2n) - special orthogonal (even)")
    
    print("\n" + "=" * 60)
    print("Type A_n: sl(n+1)")
    print("=" * 60)
    
    for n in [1, 2, 3, 4]:
        L = LieAlgebra(QQ, cartan_type=['A', n])
        dim = L.dimension()
        expected_dim = (n + 1)**2 - 1
        print(f"\nA{n} = sl({n+1}):")
        print(f"   Dimension: {dim} (expected: (n+1)² - 1 = {expected_dim})")
        print(f"   Rank: {L.cartan_type().rank()}")
    
    print("\n" + "=" * 60)
    print("Type B_n: so(2n+1)")
    print("=" * 60)
    
    for n in [2, 3, 4]:
        L = LieAlgebra(QQ, cartan_type=['B', n])
        dim = L.dimension()
        m = 2*n + 1
        expected_dim = m * (m - 1) // 2
        print(f"\nB{n} = so({m}):")
        print(f"   Dimension: {dim} (expected: m(m-1)/2 = {expected_dim})")
        print(f"   Rank: {L.cartan_type().rank()}")
    
    print("\n" + "=" * 60)
    print("Type C_n: sp(2n)")
    print("=" * 60)
    
    for n in [2, 3, 4]:
        L = LieAlgebra(QQ, cartan_type=['C', n])
        dim = L.dimension()
        m = 2*n
        expected_dim = m * (m + 1) // 2
        print(f"\nC{n} = sp({m}):")
        print(f"   Dimension: {dim} (expected: m(m+1)/2 = {expected_dim})")
        print(f"   Rank: {L.cartan_type().rank()}")
    
    print("\n" + "=" * 60)
    print("Type D_n: so(2n)")
    print("=" * 60)
    
    for n in [3, 4, 5]:
        L = LieAlgebra(QQ, cartan_type=['D', n])
        dim = L.dimension()
        m = 2*n
        expected_dim = m * (m - 1) // 2
        print(f"\nD{n} = so({m}):")
        print(f"   Dimension: {dim} (expected: m(m-1)/2 = {expected_dim})")
        print(f"   Rank: {L.cartan_type().rank()}")
    
    print("\n" + "=" * 60)
    print("Detailed Analysis: A2 (sl(3))")
    print("=" * 60)
    
    L = LieAlgebra(QQ, cartan_type=['A', 2])
    
    print(f"\nLie algebra: {L}")
    print(f"Dimension: {L.dimension()}")
    print(f"Rank: {L.cartan_type().rank()}")
    
    # Get all generators
    print("\nGenerators:")
    e1, e2 = L.e(1), L.e(2)
    f1, f2 = L.f(1), L.f(2)
    h1, h2 = L.h(1), L.h(2)
    
    print(f"   Raising operators: e1 = {e1}, e2 = {e2}")
    print(f"   Lowering operators: f1 = {f1}, f2 = {f2}")
    print(f"   Cartan generators: h1 = {h1}, h2 = {h2}")
    
    # Some brackets
    print("\nSome Lie brackets:")
    print(f"   [e1, f1] = {e1.bracket(f1)}")
    print(f"   [e2, f2] = {e2.bracket(f2)}")
    print(f"   [e1, e2] = {e1.bracket(e2)}")
    print(f"   [h1, e1] = {h1.bracket(e1)}")
    print(f"   [h1, e2] = {h1.bracket(e2)}")
    
    # Basis
    print("\nFull basis:")
    basis = L.basis()
    for i, b in enumerate(basis.list()):
        print(f"   b{i}: {b}")
    
    print("\n" + "=" * 60)
    print("Comparison Table")
    print("=" * 60)
    
    print("\n{:8s} {:15s} {:10s} {:6s}".format("Type", "Name", "Dimension", "Rank"))
    print("-" * 50)
    
    examples = [
        (['A', 2], 'sl(3)'),
        (['A', 3], 'sl(4)'),
        (['B', 2], 'so(5)'),
        (['B', 3], 'so(7)'),
        (['C', 2], 'sp(4)'),
        (['C', 3], 'sp(6)'),
        (['D', 3], 'so(6)'),
        (['D', 4], 'so(8)'),
    ]
    
    for cartan_type, name in examples:
        L = LieAlgebra(QQ, cartan_type=cartan_type)
        type_str = f"{cartan_type[0]}{cartan_type[1]}"
        print("{:8s} {:15s} {:10d} {:6d}".format(
            type_str, name, L.dimension(), L.cartan_type().rank()
        ))
    
    print("\n" + "=" * 60)

if __name__ == "__main__":
    main()
