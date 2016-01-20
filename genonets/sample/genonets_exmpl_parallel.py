#!/usr/bin/env python

"""
    genonets_exmpl_parallel
    ~~~~~~~~~~~~~~~~~~~~~~~

    Demonstrates the steps required to create genotype networks, perform analyses, 
    and write results to files using Genonets with multiprocessing enabled.

	Use the following command to run the script:
	'python genonets_exmpl_parallel.py DNA true data/genonets_sample_input.txt 0.35 results_parallel'

	Output files will be generated in 'results_parallel/'

    :author: Fahad Khalid
    :license: MIT, see LICENSE for more details.
"""

from genonets import cmdl_handler					# For parsing command line arguments
from genonets import genonets_interface as gn_if	# Interface to get the Genonets object

def process(args) :
	# Create the Genonets object. This will load the input file into
	# memory.
	gn = gn_if.Genonets(args)

	# Use 'gn' to create genotype networks for all genotype sets.
	gn.create(parallel=True)

	# Perform all available analyses on all genotype networks.
	gn.analyze(parallel=True)

	# Write all genotype networks to files in GML format. For a genotype network
	# with two or more components, two files are generated: One corresponds to the
	# entire network with all components, and the other corresponds to the dominant
	# component only.
	gn.save()

	# Save all genotype network level measures to 'Genotype_set_measures.txt'.
	gn.saveNetResults()

	# Save all genotype level measures to '<genotypeSetName>_genotype_measures.txt'
	# files.  One file per genotype set is generated.
	gn.saveGenotypeResults()


if __name__ == "__main__" :
	# Parse the command line arguments using the Genonets command line handler, and
	# pass the list of arguments to 'process()'.
	process(cmdl_handler.CmdParser().getArgs())

	# Print message to indicate processing is done.
	print("Done.\n")