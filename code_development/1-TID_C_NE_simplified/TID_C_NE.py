from peptideClass import Peptide  ##this is required to import the class from the code file

##main method
TID_BiotinList = Peptide.BiotinListFromCSV() ##need to pass the Peptide class as a parameter for the instantiate from CSV method
##tests of code
testPeptide = TID_BiotinList[1]
queryTest = testPeptide.query
print(queryTest)
print(type(TID_BiotinList[1])) ##should return peptide object = works
print(len(TID_BiotinList))

##Pre-Processing Step
TID_noBiotinList = Peptide.noBiotinListFromCSV()
print(len(TID_noBiotinList))

biotinList_SequenceOnly = Peptide.aminoAcidList(TID_BiotinList)
biotinList_QueryOnly = Peptide.queryList(TID_BiotinList)

nobiotinList_SequenceOnly = Peptide.aminoAcidList(TID_noBiotinList)
nobiotinList_QueryOnly = Peptide.queryList(TID_noBiotinList)

print(biotinList_QueryOnly)
Peptide.blastList(biotinList_QueryOnly,biotinList_SequenceOnly) 

##Post-Blast Processing