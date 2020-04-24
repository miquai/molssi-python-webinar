# Import libraries

import os
import argparse
import glob

# No functions

# Main code


if __name__ == "__main__":

    # Use argparse to get file names
    
    parser = argparse.ArgumentParser("This script parses amber mdout files to extract the total energy.")
    
    parser.add_argument("filepath", help="The file path for the mdout file to be analyzed.")
    
    args = parser.parse_args()
    
    # Tell the computer where the file is
    
    # Want to analyze multiple files like so: python analyze_mdout.py 'data/*.mdout'
    
    filenames = glob.glob(args.filepath)
    
    #filename = args.filepath
    
    for filename in filenames:
        
        # Open the file for reading

        f = open(filename, 'r')
        fname = os.path.basename(filename).split('.')[0] # Get the file name witout the .stuff

        # Read the data

        data = f.readlines() # Reads file and makes a list composed of lines of the file

        # Close the file

        f.close()

        # Open a file for writing

        f_write = open(F'{fname}_Etot_new.txt', 'w+')

        # Loop through lines in the file

        values = []

        for line in data:

            # Get information from the lines

            split_line = line.split() # Splits line based on white space
            #print(split_line)

        # Get information from the lines & write that info to the new file

            if 'Etot' in line:
                #print(split_line[2])

                #f_write.write(f'{split_line[2]}\n')

                values.append(split_line[2])

        values = values[:-2] # Cut off the last two values

        for value in values:
            f_write.write(F'{value}\n')

        f_write.close()