#!/usr/bin/env python
import argparse
import sys
from sarscov2summary import summary


def main():
	arguments = argparse.ArgumentParser(description='Summarize selection analysis results.')

	arguments.add_argument('-o', '--output', help = 'Write results here', type = argparse.FileType('w'), default = sys.stdout)
	arguments.add_argument('-s', '--slac',   help = 'SLAC results file', required = True, type = argparse.FileType('r'))
	arguments.add_argument('-f', '--fel',   help = 'FEL results file', required = True, type = argparse.FileType('r'))
	arguments.add_argument('-m', '--meme',   help = 'MEME results file', required = True, type = argparse.FileType('r'))
	arguments.add_argument('-p', '--prime',  help = 'PRIME results file', required = False, type = argparse.FileType('r'))
	arguments.add_argument('-P', '--pvalue',  help = 'p-value', required = False, type = float, default = 0.1)
	arguments.add_argument('-c', '--coordinates',  help = 'An alignment with reference sequence (assumed to start with NC)', required = True, type = argparse.FileType('r'))

	arguments.add_argument('-D', '--database', help ='Primary database record to extract sequence information from', required = True, type = argparse.FileType('r'))
	arguments.add_argument('-d', '--duplicates', help ='The JSON file recording compressed sequence duplicates', required = True, type = argparse.FileType('r'))
	arguments.add_argument('-M', '--MAF', help ='Also include sites with hapoltype MAF >= this frequency', required = False, type = float, default = 0.2)
	arguments.add_argument('-E', '--evolutionary_annotation', help ='If provided use evolutionary likelihood annotation', required = False, type = argparse.FileType('r'))
	arguments.add_argument('-F', '--evolutionary_fragment', help ='Used in conjunction with evolutionary annotation to designate the fragment to look up', required = False, type = str)
	arguments.add_argument('-A', '--mafs', help ='If provided, write a CSV file with MAF/p-value tables', required = False, type = str)
	arguments.add_argument('-V', '--evolutionary_csv', help ='If provided, write a CSV file with observed/predicted frequncies', required = False, type = str)

	import_settings = arguments.parse_args()
	summary(import_settings)

if __name__ == '__main__':
    exit(main())