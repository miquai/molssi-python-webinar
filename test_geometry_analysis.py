"""
Tests for geometry analysis functions.
"""



import geometry_analysis as ga # Import our old code, geometry_analysis.py, which contains functions



def test_calculate_distance(): # Write a test for the calculate_distance function in geometry_analysis.py
    
    coord1 = [0, 0, 0] # Make some face coordinates
    coord2 = [1, 0, 0]
    
    expected = 1.0 # Define expected result
    
    observed = ga.calculate_distance(coord1, coord2) # Ask the function to calculate the distance
    
    assert observed == expected # "assert" statement: if this is true, our test will pass. This is the critical line for a test!
    


def test_bond_check(): # Write a test for the bond_check function in geometry_analysis.py
    
    bond_distance = 1.0 # Make a fake distance
    
    expected = True # Define expected result
    
    observed = ga.bond_check(bond_distance) # Ask the function to determine if bond is True or False
    
    assert observed == expected # "assert" statement

    
### NOTE! Just becuase the above test passed doesn't mean bond_check is working perfectly. We need to design a fuller test!

    
def test_bond_check_0(): # Write a test for the bond_check function in geometry_analysis.py
    
    bond_distance = 0 # Make a fake distance
    
    expected = False # Define expected result
    
    observed = ga.bond_check(bond_distance) # Ask the function to determine if bond is True or False
    
    assert observed == expected # "assert" statement
    
    
def test_bond_check_1p6(): # Write a test for the bond_check function in geometry_analysis.py
    
    bond_distance = 1.6 # Make a fake distance
    
    expected = False # Define expected result
    
    observed = ga.bond_check(bond_distance) # Ask the function to determine if bond is True or False
    
    assert observed == expected # "assert" statement
    