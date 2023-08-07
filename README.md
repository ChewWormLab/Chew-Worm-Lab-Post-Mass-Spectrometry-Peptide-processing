# Peptide Sequence processing:
## Overview
This is the code used to analyze the unassigned peptide sequences, presented in Rahmani A. & Chew YL., "Article title" 
available at (link to article). 

The samples were processed via Liquid Chromatography with tandem mass spectrometry (LC-MS-MS). 
The sequences were generated using the Mascot Server via the Mascot Daemon application (Mascot Science: https://www.matrixscience.com/daemon.html)
The LC-MSMS and subsequent Mascot processing was conducted by Dr Anne Poljak (UNSW).

Due to a large number of non-confident hits per sample, this code was written to allow for the identification of their associated peptides using the NCBI reference proteins database (refseq_protein).

This code generates 2 lists of biotinylated and non-biotinylated peptide sequences and their associated proteins.

## Packages used for code processing:
This code was written for Windows OS and has only been used on these systems. This code was written in Python 3.9 and uses the following packages/libraries.
- Biopython 1.78
- Pandas    1.5.3
- Anaconda 2023.03
## Citations
