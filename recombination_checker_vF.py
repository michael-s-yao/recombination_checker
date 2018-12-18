#!/usr/bin/env python

'''
Copyright 2018 Michael Yao
Caltech, Pasadena, CA 91125
This Recombination Checker software determines if there are any potential sites
of recombination within a plasmid sequence.

The plasmid DNA sequence must be entered in the format 
/Users/johnsmith/Documents/Folder/test_file.txt
when prompted.
'''

from datetime import datetime

__author__ = "Michael Yao"
__copyright__ = "Copyright 2018"
__version__ = "1.0.2"
__maintainer__ = "Michael Yao"
__email__ = "myao@caltech.edu"
__status__ = "Development"

def generate_substr_p(string, start, length):
    '''
    The generate_substr_p function takes a string and generates a substring of 
    a specified length using a starting character position in the string.
    Use this function to generate a substring of a plasmid.
    ARGUMENTS:
    string - template string that we want to take the substring of
    start - the starting position of the substring within the string
    length - the length of our desired substring
    RETURN:
    The function returns the list 'desired_substr_list' which is our desired
    substring in the form of a list.
    '''
    assert length <= len(string), 'Desired substring length longer than length of the string'
    assert start <= len(string), 'Start position not specified in the string'
    str_list = []
    desired_substr_list = []
    for char in string: str_list.append(char.lower())
    for char in string: str_list.append(char.lower())
    for i in range(start, (start + length)):
        desired_substr_list.append(str_list[i])
    return desired_substr_list

def check_recomb(string, homology_len, match_percent):
    '''
    The check_recomb function takes a DNA string as an input and determines if 
    there are any potential areas for recombination.
    ARGUMENTS:
    string - DNA string input
    homology_len - number of base pairs to analyze for homology
    match_percent - percent of base pairs of homology_len that have to be the
        same to return a potential recombination site
    RETURN:
    The function returns a list of the potential 
    '''
    dic_substr = {}
    list_recomb_raw = []
    list_recomb_final = []
    list_recomb_unique = []
    for i in range(0, len(string)):
        dic_substr[i] = generate_substr_p(string, i, homology_len)
    for i in range(0, len(string)):
        for j in range((i + homology_len), len(string)):
            counter = 0
            for k in range(0, homology_len):
                if dic_substr[i][k] == dic_substr[j][k]: counter += 1
            if counter >= (homology_len * match_percent):
                list_recomb_raw.append((i, j))
    return list_recomb_raw

if __name__ == '__main__':
    start = datetime.now()
    print("This program will help determine if there are any potential sites of"
          " recombination in your plasmid.")
    dna_seq_file = input("Enter valid DNA sequence .txt file here: ")
    homology_len = int(input("Enter minimum DNA homology length for "
                             "recombination: "))
    match_percent = float(input("Enter minimum percentage (0-1) of homology "
                                "length necessary for recombination: "))
    dna_seq_file_open = open(dna_seq_file, 'r')
    dna_seq = dna_seq_file_open.readline()
    potential_sites = check_recomb(dna_seq, homology_len, match_percent)
    print("Potential recombation sites: {}".format(potential_sites))
    print("Program run time: {}".format(datetime.now() - start))
    print_seq = input("Output site sequences? [y/n] ")
    if print_seq == 'y' or print_seq == 'Y':
        for site in potential_sites:
            output1 = generate_substr_p(dna_seq, site[0], homology_len)
            output2 = generate_substr_p(dna_seq, site[1], homology_len)
            output1_str = ''.join(output1)
            output2_str = ''.join(output2)
            print('{} and {} share potential homology.'.format(output1_str, \
                                                               output1_str))           