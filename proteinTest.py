from peptideClass import Peptide  ##this is required to import the class from the code file
from proteinClass import Protein 

testXML = open("PK89BYGF013-Alignment.xml")
testProteinList = Protein.parseBlast(testXML)
