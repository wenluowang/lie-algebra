"""
Example 2: Root Systems and Cartan Matrices

This script demonstrates working with root systems in SageMath.
Run this script with: sage example_02_root_systems.py
"""

from sage.all import *

def main():
    print("=" * 60)
    print("Example 2: Root Systems and Cartan Matrices")
    print("=" * 60)
    
    # Create root systems for different types
    types = [['A', 2], ['B', 2], ['C', 2], ['D', 3]]
    
    for cartan_type in types:
        print(f"\n{'=' * 60}")
        print(f"Type {cartan_type[0]}{cartan_type[1]}:")
        print('=' * 60)
        
        R = RootSystem(cartan_type)
        print(f"Root system: {R}")
        
        # Cartan matrix
        print("\nCartan Matrix:")
        print(R.cartan_matrix())
        
        # Dynkin diagram
        print("\nDynkin Diagram:")
        print(R.dynkin_diagram())
        
        # Root lattice
        root_lattice = R.root_lattice()
        
        # Simple roots
        simple_roots = root_lattice.simple_roots()
        print(f"\nSimple roots: {simple_roots}")
        
        # Positive roots
        positive_roots = list(root_lattice.positive_roots())
        print(f"\nPositive roots ({len(positive_roots)} total):")
        for root in positive_roots:
            print(f"   {root}")
        
        # Dimension of corresponding Lie algebra
        # dim = number of positive roots * 2 + rank
        rank = R.cartan_type().rank()
        dim = len(positive_roots) * 2 + rank
        print(f"\nRank: {rank}")
        print(f"Dimension of Lie algebra: {dim}")
    
    print("\n" + "=" * 60)
    print("Root System Properties")
    print("=" * 60)
    
    # Detailed analysis of A2
    R = RootSystem(['A', 2])
    root_space = R.root_space()
    
    print("\nType A2 (sl(3)) detailed analysis:")
    print(f"Root space: {root_space}")
    
    # Get specific roots
    alpha1 = root_space.simple_root(1)
    alpha2 = root_space.simple_root(2)
    
    print(f"\nSimple root α1: {alpha1}")
    print(f"Simple root α2: {alpha2}")
    print(f"α1 + α2: {alpha1 + alpha2}")
    
    # Coroot
    alpha1_coroot = alpha1.associated_coroot()
    print(f"\nCoroot of α1: {alpha1_coroot}")
    
    print("\n" + "=" * 60)

if __name__ == "__main__":
    main()
