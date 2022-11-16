from peptideClass import Peptide  ##this is required to import the class from the code file

##main method
FileNameTest = 'Peptide_Practice.csv'
test_EntireList = Peptide.BiotinListFromCSV(FileNameTest) ##need to pass the Peptide class as a parameter for the instantiate from CSV method
##tests of code
testPeptide = test_EntireList[1]
queryTest = testPeptide.query
print(queryTest)
print(type(test_EntireList[1])) ##should return peptide object = works
print(len(test_EntireList))
##testing the biotin sorting method from the list

test_BiotinList = Peptide.BiotinList(test_EntireList) #issue with this line - not creating list;maybe issue with code or with how method is passed
print(len(test_BiotinList))

testSequenceOnly = Peptide.aminoAcidList(test_BiotinList)
testQueryOnly = Peptide.queryList(test_BiotinList)
print(testQueryOnly)
Peptide.blastList(testQueryOnly,testSequenceOnly) ##Actually works!!!!!!!!!!!!!!!



