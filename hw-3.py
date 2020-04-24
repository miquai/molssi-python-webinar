# start with imports

import os
import argparse



# define functions
        
    #none
    
    
    
    
    
# main part of code

if __name__ == "__main__":
    
    # next: use argparse

    parser = argparse.ArgumentParser(description='This script parses amber mdout files to extract the total energy.') # this tells argparse you're going to use it

    parser.add_argument('file_path', help="The file path for the mdout file to be analyzed.")
    # this is an argument we want the code to accept

    args = parser.parse_args()
    # collect all the arguments from argparse
    
    
    
    # finally: the code
    
    file_path = args.file_path
    
    f = open(file_path, 'r')

    # Read the data

    data = f.readlines() # Reads file and makes a list composed of lines of the file

    # Close the file

    f.close()

    # Open a file for writing

    f_write = open('Etot_hw3.txt', 'w+')

    # Loop through lines in the file

    for line in data:

        # Get information from the lines

        split_line = line.split() # Splits line based on white space
        #print(split_line)

    # Get information from the lines & write that info to the new file

        if 'Etot' in line:
            #print(split_line[2])
            f_write.write(f'{split_line[2]}\n')

    f_write.close()