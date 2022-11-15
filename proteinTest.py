from peptideClass import Peptide  ##this is required to import the class from the code file
from proteinClass import Protein
from Bio.Blast import NCBIXML
from Bio.Blast import Record

testXML = open("PK89BYGF013-Alignment.xml")
testProteinList = Protein.parseBlast(testXML)