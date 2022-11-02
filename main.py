from peptideClass import Peptide  ##this is required to import the class from the code file

##main method
test_EntireList = Peptide.instantiateFromCSV() ##need to pass the Peptide class as a parameter for the instantiate from CSV method
##tests of code
testPeptide = test_EntireList[1]
queryTest = testPeptide.query
print(queryTest)
print(type(test_EntireList[1])) ##should return peptide object = works
testString = test_EntireList[1]
print(testString)
print(len(test_EntireList))
##testing the biotin sorting method from the list
print("test!")
test_BiotinList = Peptide.BiotinList(test_EntireList) #issue with this line - not creating list;maybe issue with code or with how method is passed
print(len(test_BiotinList))

