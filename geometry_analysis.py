"""
This module has functions associated with analyzing the geometry of a molecule.

It can be run as a script with an xyz file.
"""

# COLLECT ALL CODE IN ONE BOX



# start with imports

import numpy
import os
import argparse


# next: functions

def open_xyz(file_path):
    
    """
    This function opens an xyz file, separates the coordinates and the symbols and recasts the coordinates as floats
    Input: a file_path
    Returns 2 things: symbols, coordinates
    """
    
    xyz_file = numpy.genfromtxt(fname=file_path, skip_header=2, dtype='unicode')
    
    symbols = xyz_file[:,0]
    
    coordinates = xyz_file[:,1:]
    
    coordinates = coordinates.astype(numpy.float)
    
    return symbols, coordinates

def calculate_distance(atom1_coord, atom2_coord): # inputs are 2 coordinates
    
    x_distance = atom1_coord[0] - atom2_coord[0]
    y_distance = atom1_coord[1] - atom2_coord[1]
    #y_distance = atom1_coord[0] - atom2_coord[1] # wrong on purpose, to demonstrate test might still pass!
    z_distance = atom1_coord[2] - atom2_coord[2]
    
    atom_distance = numpy.sqrt(x_distance**2 + y_distance**2 + z_distance**2)
    
    return atom_distance

def bond_check(distance, minimum_length=0, maximum_length=1.5): # These equal signs point to the default values!
    if distance > minimum_length and distance <= maximum_length:
        return True # "True" turned green becasue it's a Boolean operator
    else:
        return False


    
# tell python this is the main part of the code!    

if __name__ == "__main__":
    
    
    # next: use argparse

    parser = argparse.ArgumentParser(description='The script analyzes a user-given xyz file and outputs the length of the bonds.') # this tells argparse you're going to use it

    parser.add_argument('xyz_file', help="The file path for the xyz file to analyze.")
    # this is an argument we want the code to accept

    args = parser.parse_args()
    # collect all the arguments from argparse




    # finally: geometry analysis code

    # Replace this with args stuff
    #file_location = os.path.join('data','water.xyz')
    xyzfilename = args.xyz_file

    #symbols, coordinates = open_xyz(file_location) # HERE'S OUR "open_xyz" FUNCTION!
    symbols, coordinates = open_xyz(xyzfilename)


    num_atoms = len(symbols)

    for num1 in range(0,num_atoms):

        for num2 in range(0,num_atoms):

            if num1<num2:

                atom_distance = calculate_distance(coordinates[num1], coordinates[num2]) # HERE'S OUR "atom_distance" FUNCTION!

                if bond_check(atom_distance) is True: # HERE'S OUR "bond_check" FUNCTION!

                    print(F'{symbols[num1]} to {symbols[num2]}: {atom_distance:.3f}') # .3f means print just 3 decimal places


              