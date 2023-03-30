import requests
from bs4 import BeautifulSoup
from typing import List, Tuple
from dataclasses import dataclass
import re

@dataclass
class GenscanOutput:
    status: str
    cds_list: List[str]
    intron_list: List[Tuple[int, int, int]]
    exon_list: List[Tuple[int, int, int]]


    # Define a method to run Genscan
    def run_genscan(sequence=None, sequence_file=None, organism="Vertebrate", exon_cutoff=1.00, sequence_name="") -> 'GenscanOutput':

        # If a sequence file is provided, read its contents
        if sequence_file != None:
            with open(sequence_file, 'r') as file:
                sequence = file.read()

        # Set up the data to be sent to Genscan
        data = {'-s': sequence,
                '-u': sequence_file, 
                '-o': organism,
                '-e': exon_cutoff, 
                '-n': sequence_name, 
                '-p': 'Predicted peptides only'}

        # Set the Genscan URL
        url = 'http://hollywood.mit.edu/cgi-bin/genscanw_py.cgi'

        # Send the data to Genscan and get the response
        response = requests.post(url, data=data)
        status = response

        # Parse the response HTML using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Initialize empty lists to hold the output data
        intron_list = []
        exon_list = []
        cds_list = []

        # Find all <pre> tags in the HTML
        pre_tags = soup.find_all('pre')

        # Loop over each <pre> tag and extract data
        for pre_tag in pre_tags:
            lines = pre_tag.text.split('\n')
            for i, line in enumerate(lines):
                # Extract exon information
                if re.search(r'(Intr|Term|Term|Sngl)', line):
                    fields = line.split()
                    begin = int(fields[3])
                    end = int(fields[4])
                    if begin > end:
                        begin, end = end, begin
                    exon = {
                        'Exon number': float(fields[0]),
                        'begin': begin,
                        'end': end,
                        'length': int(fields[5])
                    }
                    exon_list.append(exon)
                # Extract predicted peptide sequences
                if 'Predicted peptide sequence(s):' in line:
                    predicted_peptides = []
                    for j in range(i+1, len(lines)):
                        if not lines[j].startswith('-'):
                            predicted_peptides.append(lines[j].strip())
                        else:
                            break
                    cds_list = [s for s in predicted_peptides if re.match(r'^[A-Z]+$', s)]

        # Calculate intron information from exon information
        for i in range(1, len(exon_list)):
            intron = {
                'Intron number': i,
                'begin': exon_list[i-1]['end']+1,
                'end': exon_list[i]['begin']-1,
                'length': exon_list[i]['begin']-exon_list[i-1]['end']-1
            }
            intron_list.append(intron)

        # Create a GenscanOutput object to hold the output data and return it
        output = GenscanOutput(status=status, cds_list=cds_list, intron_list=intron_list, exon_list=exon_list)
        return output