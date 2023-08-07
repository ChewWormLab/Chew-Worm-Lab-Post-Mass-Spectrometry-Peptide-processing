from peptideClass import Peptide  ##this is required to import the class from the code file
import pathlib
from BLAST import BLASTmethods
from HSPClass import HSP


##-------------------this is the only part of the code that needs to be modified-------------------------------##

peptideFile = pathlib.PureWindowsPath(r"E:\Python Programming\07-08-2023 Int error and html table not found fix\HTML tables not found\Coding Files\AR_sample_13 not assigned peptides.html")   ##update file name to match the html or csv name - note that it needs to be surrounded by double quotation marks

##----------------------------------------Start of analysis----------------------------------------------------##

##Ascertain whether csv file or html file handed:
peptideFile_extension = pathlib.Path(peptideFile).suffix

print('\033[1m' + "Analysis Start" + '\033[0m')
print("--------------You have entered a " + peptideFile_extension + " type file for this analysis--------------")

if peptideFile_extension == ".csv":
##------------------------------ Using CSV to generate FASTA File ---------------------------------------------##
    ##---------   Biotinylated List   ---------- ##
    BiotinList = Peptide.BiotinListFromCSV(peptideFile) ##need to pass the Peptide class as a parameter for the instantiate from CSV method
    
    biotinList_SequenceOnly = Peptide.aminoAcidList(BiotinList)
    biotinList_QueryOnly = Peptide.queryList(BiotinList)
    
    biotinFASTA = Peptide.blastList(biotinList_QueryOnly,biotinList_SequenceOnly) 
    ##--------- Non-biotinylated List ---------- ##
    noBiotinList = Peptide.noBiotinListFromCSV(peptideFile)
    nobiotinList_SequenceOnly = Peptide.aminoAcidList(noBiotinList)
    nobiotinList_QueryOnly = Peptide.queryList(noBiotinList)
    noBiotinFASTA = Peptide.noBiotin_blastList(nobiotinList_QueryOnly, nobiotinList_SequenceOnly)
    ##--------- Summary (sanity checks) ---------- ##
    Peptide.preprocessingOverview(BiotinList,noBiotinList)
    Peptide.endPreprocessingMethod()
##----------------------------------------- Remote BLAST Search ------------------------------------------------##
    biotinBLASTxml = BLASTmethods.remoteBiotinBLAST("Biotin_blastSeq.txt") 
    nobiotinBLASTxml = BLASTmethods.remote_noBiotinBLAST("noBiotin_blastSeq.txt")
##-----------------------------------------  BLAST XML processing-----------------------------------------------##
    biotinHSPList = HSP.HSPListfromXML(biotinBLASTxml) ##using generated XML files from BLAST search to return a list object (already processed so that HSPs of same description are combined)
    noBiotin_HSP = HSP.HSPListfromXML(nobiotinBLASTxml,"no_Biotin")
    HSP.protein_HitCSV(biotinHSPList,"Biotin")
    print("The final list of biotinylated assigned peptides are:" + "\n")
    HSP.printHSPList(biotinHSPList)
    
elif peptideFile_extension == ".htm" or peptideFile_extension == ".html":
##------------------------------ Using HTML to generate FASTA File ---------------------------------------------##
    ##---------   Biotinylated List   ---------- ##
    print("Parsing HTML now for biotinylated peptides, this will take a bit of time")
    BiotinList = Peptide.BiotinListFromHTML(peptideFile)
    print("HTML parsing completed")
    ##Biotinylated peptide generation 
    biotinList_SequenceOnly = Peptide.aminoAcidList(BiotinList)
    biotinList_QueryOnly = Peptide.queryList(BiotinList)
    
    biotinFASTA = Peptide.blastList(biotinList_QueryOnly,biotinList_SequenceOnly) 
    
    ##--------- Non-biotinylated List ---------- ##
    print("Parsing HTML now for non-biotinylated peptides, this will take a bit of time")
    noBiotinList = Peptide.noBiotinListFromHTML(peptideFile)
    print("HTML parsing completed")
    nobiotinList_SequenceOnly = Peptide.aminoAcidList(noBiotinList)
    nobiotinList_QueryOnly = Peptide.queryList(noBiotinList)
    noBiotinFASTA = Peptide.noBiotin_blastList(nobiotinList_QueryOnly, nobiotinList_SequenceOnly)
    
    # ##--------- Summary (sanity checks) ---------- ##
    Peptide.preprocessingOverview(BiotinList,noBiotinList)
    Peptide.endPreprocessingMethod()
    
##----------------------------------------- Remote BLAST Search ------------------------------------------------##
    biotinBLASTxml = BLASTmethods.remoteBiotinBLAST("Biotin_blastSeq.txt") 
    nobiotinBLASTxml = BLASTmethods.remote_noBiotinBLAST("noBiotin_blastSeq.txt")
##-----------------------------------------  BLAST XML processing-----------------------------------------------##
    biotinHSPList = HSP.HSPListfromXML("Biotin BLAST.xml") ##using generated XML files from BLAST search to return a list object (already processed so that HSPs of same description are combined)
    biotinRefined = HSP.refinedList(biotinHSPList)
    noBiotin_HSP = HSP.HSPListfromXML("no_Biotin BLAST.xml")
    noBiotin_Refined = HSP.refinedList(noBiotin_HSP)
    HSP.protein_HitCSV(biotinHSPList,biotinRefined," Biotin ", "Biotin BLAST meta.txt")
    print("The final list of biotinylated assigned peptides are:" + "\n")
    HSP.printHSPList(biotinHSPList)
    HSP.protein_HitCSV(noBiotin_HSP,noBiotin_Refined,"no_Biotin ","no_Biotin BLAST meta.txt")
    print("The final list of biotinylated assigned peptides are:" + "\n")
    HSP.printHSPList(noBiotin_HSP)
    print('\033[1m' + "The processing of your peptides samples is done! " + '\033[0m' 
          + "Please check that you have generated the following files: " + "\n" 
          +"   >> Biotin BLAST.xml;"  + "\n"
          +"   >> no_Biotin BLAST.xml;" + "\n"
          +"   >> Biotin BLAST meta.txt " + "\n"
          +"   >> no_Biotin BLAST meta.txt " + "\n"
          +"   >> Biotin Protein-Hits.csv; " + "\n"
          +"   >> no_Biotin Protein-Hits.csv; " + "\n"
          +"   >> Biotin gene_Ids.txt " + "\n"
          +"   >> no_Biotin gene_Ids.txt " + "\n"
          + "\n"'\033[1m' + "~ ~ Best of luck with the worms! ~ ~" + '\033[0m' + "\n")
else:
    print("Please ensure that the file type is '.csv' or .htm'")
    print("If you are having issues, check the paths, or make sure that the code files you have altered are inside the folder of interest")