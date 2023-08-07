from peptideClass import Peptide  ##this is required to import the class from the code file

##main method
FileName = 'Peptide_Practice.csv' ##Change name to file name
EntireList = Peptide.BiotinListFromCSV(FileName) ##need to pass the Peptide class as a parameter for the instantiate from CSV method
##tests of code
testPeptide = EntireList[1]
queryTest = testPeptide.query
print(queryTest)
print(type(EntireList[1])) ##should return peptide object = works
print(len(EntireList))
##testing the biotin sorting method from the list

BiotinList = Peptide.BiotinList(EntireList) 
print(len(BiotinList)) ##returns count of biotinylated peptides

SequenceOnly = Peptide.aminoAcidList(BiotinList)
QueryOnly = Peptide.queryList(BiotinList)
##print(QueryOnly) - prints list of 
Peptide.blastList(QueryOnly,SequenceOnly)



