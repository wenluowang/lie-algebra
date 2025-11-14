"""
Example 3: Matrix Representations of Lie Algebras

This script demonstrates working with matrix representations.
Run this script with: sage example_03_matrix_representations.py
"""

from sage.all import *

def main():
    print("=" * 60)
    print("Example 3: Matrix Representations of Lie Algebras")
    print("=" * 60)
    
    print("\n1. sl(2) - Special Linear Lie Algebra")
    print("-" * 60)
    
    # Standard basis of sl(2): 2x2 traceless matrices
    E = matrix(QQ, [[0, 1], [0, 0]])  # Raising operator
    F = matrix(QQ, [[0, 0], [1, 0]])  # Lowering operator
    H = matrix(QQ, [[1, 0], [0, -1]]) # Cartan element
    
    print("\nBasis matrices:")
    print(f"\nE (raising operator):\n{E}")
    print(f"\nF (lowering operator):\n{F}")
    print(f"\nH (Cartan element):\n{H}")
    
    # Verify they are traceless
    print("\nTrace verification (should all be 0 for sl(n)):")
    print(f"   trace(E) = {E.trace()}")
    print(f"   trace(F) = {F.trace()}")
    print(f"   trace(H) = {H.trace()}")
    
    # Define Lie bracket
    def lie_bracket(X, Y):
        """Compute [X, Y] = XY - YX"""
        return X * Y - Y * X
    
    # Compute structure relations
    print("\nLie bracket computations:")
    bracket_EF = lie_bracket(E, F)
    bracket_HE = lie_bracket(H, E)
    bracket_HF = lie_bracket(H, F)
    
    print(f"\n[E, F] =\n{bracket_EF}")
    print(f"Expected: H = {H}")
    print(f"Match: {bracket_EF == H}")
    
    print(f"\n[H, E] =\n{bracket_HE}")
    print(f"Expected: 2E = {2*E}")
    print(f"Match: {bracket_HE == 2*E}")
    
    print(f"\n[H, F] =\n{bracket_HF}")
    print(f"Expected: -2F = {-2*F}")
    print(f"Match: {bracket_HF == -2*F}")
    
    print("\n" + "=" * 60)
    print("2. sl(3) - A basis of traceless 3x3 matrices")
    print("-" * 60)
    
    # Some basis elements of sl(3)
    E12 = matrix(QQ, [[0, 1, 0], [0, 0, 0], [0, 0, 0]])
    E23 = matrix(QQ, [[0, 0, 0], [0, 0, 1], [0, 0, 0]])
    E21 = matrix(QQ, [[0, 0, 0], [1, 0, 0], [0, 0, 0]])
    H1 = matrix(QQ, [[1, 0, 0], [0, -1, 0], [0, 0, 0]])
    
    print("\nSome basis elements of sl(3):")
    print(f"\nE_12:\n{E12}")
    print(f"\nE_23:\n{E23}")
    print(f"\nH_1:\n{H1}")
    
    # Compute a bracket
    print("\nExample bracket computation:")
    bracket = lie_bracket(E12, E23)
    print(f"[E_12, E_23] =\n{bracket}")
    
    # Verify trace
    print(f"\ntrace([E_12, E_23]) = {bracket.trace()}")
    
    print("\n" + "=" * 60)
    print("3. so(3) - Special Orthogonal Lie Algebra")
    print("-" * 60)
    
    # Standard basis of so(3): 3x3 antisymmetric matrices
    J1 = matrix(QQ, [[0, 0, 0], [0, 0, -1], [0, 1, 0]])
    J2 = matrix(QQ, [[0, 0, 1], [0, 0, 0], [-1, 0, 0]])
    J3 = matrix(QQ, [[0, -1, 0], [1, 0, 0], [0, 0, 0]])
    
    print("\nBasis of so(3) (antisymmetric matrices):")
    print(f"\nJ1:\n{J1}")
    print(f"\nJ2:\n{J2}")
    print(f"\nJ3:\n{J3}")
    
    # Verify antisymmetry
    print("\nAntisymmetry verification:")
    print(f"   J1 = -J1^T: {J1 == -J1.transpose()}")
    print(f"   J2 = -J2^T: {J2 == -J2.transpose()}")
    print(f"   J3 = -J3^T: {J3 == -J3.transpose()}")
    
    # Structure constants (angular momentum algebra)
    print("\nStructure relations (should satisfy [Ji, Jj] = εijk Jk):")
    print(f"[J1, J2] =\n{lie_bracket(J1, J2)}")
    print(f"Expected: J3 =\n{J3}")
    print(f"Match: {lie_bracket(J1, J2) == J3}")
    
    print(f"\n[J2, J3] =\n{lie_bracket(J2, J3)}")
    print(f"Expected: J1 =\n{J1}")
    print(f"Match: {lie_bracket(J2, J3) == J1}")
    
    print(f"\n[J3, J1] =\n{lie_bracket(J3, J1)}")
    print(f"Expected: J2 =\n{J2}")
    print(f"Match: {lie_bracket(J3, J1) == J2}")
    
    print("\n" + "=" * 60)

if __name__ == "__main__":
    main()
