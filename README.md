# Peptide Sequence processing
This is some rough code that has been broken up into separate components for C.elegans peptide processing.
Due to a large number of unassigned peptides/proteins from C elegans mass spec, the following pipeline was designed.

This is a private repo.

# Project is done in 3 parts:
> Iterating through a csv file to generate a reference list of biotinylated peptides as well as non-biotinylated peptides from Mass Spec samples
> Running generated lists through Blastp Suite (this may require the use of services such as google cloud)
> Sorting through generated proteins and assigning a "protein score"

