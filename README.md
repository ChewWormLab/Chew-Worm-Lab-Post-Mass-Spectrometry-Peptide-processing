# Peptide Sequence processing:
## Overview
This is the code used to analyze the unassigned peptide sequences, presented in Rahmani A. & Chew YL., "Article title" 
available at (link to article). 

The samples were processed via Liquid Chromatography with tandem mass spectrometry (LC-MS-MS). 
The sequences were generated using the Mascot Server via the Mascot Daemon application (Mascot Science: https://www.matrixscience.com/daemon.html)
The LC-MSMS and subsequent Mascot processing was conducted by Dr Anne Poljak (UNSW).

Due to a large number of non-confident hits per sample, this code was written to allow for the identification of their associated peptides using the NCBI reference proteins database (refseq_protein).

This code generates 2 lists of biotinylated and non-biotinylated peptide sequences and their associated proteins in a CSV format.

This program is released under the Creativer Commons Attribution Noncommercial Licence 4.0 Deed (CC BY-NC).  Please see [LICENSE-CC-BY-NC](https://github.com/Ericka-A/Chew-Worm-Lab-Post-Mass-Spectrometry-Peptide-processing/blob/main/LICENSE-CC-BY-NC-4.0.md). More information can be found at the [Creative commons website](https://creativecommons.org/licenses/by-nc/4.0/)

## Packages used for code processing:
This code was written for Windows OS and has only been used on these systems. This code was written in Python 3.9 and uses the following packages/libraries.
- Biopython 1.78
- Pandas    1.5.3
- Anaconda 2023.03
## Citations

Cock, P.J.A. et al. Biopython: freely available Python tools for computational molecular biology and bioinformatics. Bioinformatics 2009 Jun 1; 25(11) 1422-3 https://doi.org/10.1093/bioinformatics/btp163 pmid:19304878

ANACONDA SOFTWARE DISTRIBUTION. November, 2016. Anaconda: Computer software [Online]. Vers. 2-2.4.0. Available: https://anaconda.com [Accessed 2023].THE PANDAS DEVELOPMENT TEAM. February, 2020. 

pandas-dev/pandas: Pandas [Online]. Latest ver.: Zenodo. Available: https://doi.org/10.5281/zenodo.3509134 [Accessed 2023].

pBLAST [Internet]. Bethesda (MD): National Library of Medicine (US), National Center for Biotechnology Information; 2004 – [ 2023]. Available from: https://blast.ncbi.nlm.nih.gov/Blast.cgi?PROGRAM=blastp&PAGE_TYPE=BlastSearch&LINK_LOC=blasthome 
