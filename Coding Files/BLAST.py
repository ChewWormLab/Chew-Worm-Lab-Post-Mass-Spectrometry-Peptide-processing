from Bio.Blast import NCBIWWW
from Bio import SeqIO
import os

class BLASTmethods:
    ##using Biopyton to do a remote search
    @classmethod
    def remoteBiotinBLAST(cls, FASTAfile):
        FASTA_string = open(FASTAfile).read()
        ## --------------------------------- BLAST SEARCH _-----------------------------------##
        print("Performing remote blast of Biotinylated sequences, please wait")
        BLASTresults = NCBIWWW.qblast(
            "blastp", ##uses blastp function - protein-proteinmatching
            "refseq_protein", ##uses the refseq_protein database
            FASTA_string,
            expect = 0.05, 
            format_type = "XML",
            entrez_query='txid6239[Organism]' ##specifies c elegans taxid
            )
        print("remote BLAST of biotinylated peptides is complete")
        ## ------------------------------SAVING BLAST RESULTS---------------------------------##
        save_file = open("Biotin BLAST.xml","w") ##creates a new xml file for the biotin list query (as per stack exchange) 
        save_file.write(BLASTresults.read()) ##writes the previous save result into save XML file
        save_file.close()
        BLASTresults.close()       
        return os.path.abspath("Biotin BLAST.xml")
        
    @classmethod
    def remote_noBiotinBLAST(cls, FASTAfile):
        FASTA_string = open(FASTAfile).read()
        ## --------------------------------- BLAST SEARCH _-----------------------------------##
        print("Performing remote blast  of non-biotinylated sequences, please wait")
        BLASTresults = NCBIWWW.qblast(
            "blastp", ##uses blastp function - protein-proteinmatching
            "refseq_protein", ##uses the refseq_protein database
            FASTA_string,
            expect = 0.05, 
            format_type = "XML",
            entrez_query='txid6239[Organism]' ##specifies c elegans taxid
            )
        print("remote BLAST of Non-biotinylated peptides is complete")
        ## ------------------------------SAVING BLAST RESULTS---------------------------------##
        save_file = open("no_Biotin BLAST.xml","w") ##creates a new xml file for the biotin list query (as per stack exchange) 
        save_file.write(BLASTresults.read()) ##writes the previous save result into save XML file
        save_file.close()
        BLASTresults.close()
        return os.path.abspath("no_Biotin BLAST.xml")