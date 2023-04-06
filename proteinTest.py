from peptideClass import Peptide  ##this is required to import the class from the code file
from hitClass import Protein 

testXML = open("RKS984Z401N-Alignment.xml") #only has 20 peptides - is test
testProteinList = Protein.parseBlast(testXML)

print("Protein list has been generated!")
Protein.printProteins(testProteinList)

