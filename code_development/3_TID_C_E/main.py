from peptideClass import Peptide  ##this is required to import the class from the code file
from pathlib import Path, PureWindowsPath

##this is the only part of the code that needs to be modified
##update address of the FOLDER - note, do not remove the r before the double quotation marks
workingFolder = PureWindowsPath(r"C:\Users\Ericka\Desktop\Peptide_MS\YLCAR_peptides\3_TID_C_E")  
csvFile = workingFolder / "3 TID_M_NE_simplified.csv"   ##update file name to match csv name - note that it needs to be surrounded by double quotation marks

##Method to generate the Biotinylated Peptide List
BiotinList = Peptide.BiotinListFromCSV(csvFile) ##need to pass the Peptide class as a parameter for the instantiate from CSV method
##tests of code
testPeptide = BiotinList[0]
queryTest = testPeptide.query
print(queryTest) ##should print the query number for the 1st peptide in the list
print(type(BiotinList[1])) ##should return peptide object = works
print(len(BiotinList)) ##prints the number of peptides in the Biotinylated list

biotinList_SequenceOnly = Peptide.aminoAcidList(BiotinList)
biotinList_QueryOnly = Peptide.queryList(BiotinList)

print(biotinList_QueryOnly)
Peptide.blastList(biotinList_QueryOnly,biotinList_SequenceOnly) 

##Non-biotinylated List
noBiotinList = Peptide.noBiotinListFromCSV(csvFile)
print(len(noBiotinList))

nobiotinList_SequenceOnly = Peptide.aminoAcidList(noBiotinList)
nobiotinList_QueryOnly = Peptide.queryList(noBiotinList)
Peptide.noBiotin_blastList(nobiotinList_QueryOnly, nobiotinList_SequenceOnly)