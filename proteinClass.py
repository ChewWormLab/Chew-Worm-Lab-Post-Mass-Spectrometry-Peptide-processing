from Bio.Blast import NCBIXML
from Bio.Blast import Record
##this script will parse the XML file
class Protein:
    ##constructor for protein) 
    def __init__(self, protein_descript:str, peptideQuery:str, eValue:float):
        self.__description = protein_descript
        self.__peptideDict = {peptideQuery:eValue} #initialising dictionary to hold the values
        self.__count = 0
    ##getters AKA accessors (return the variable)
    @property
    def description(self):
        return self.__description        
    @property
    def peptideDict(self):
        return self.__peptideDict 
    @property
    def count(self): 
        return self.__count
    
    ##setters AKA mutators
    @description.setter
    def description(self, descript):
        self.__description = descript
    
    @peptideDict.setter
    def peptideDict(self, dictionary):
        self.__peptideDict = dictionary

    @count.setter
    def count(self, num):
        self.__count = num  
    
    
    ##note, using BioPython package installed via Conda
    ##static method to create a list object filled with protein objects
    @staticmethod
    def parseBlast(blast_XML_File): #pass the XML file as a parameter
        blast_File = open(blast_XML_File) #create a handle for the open XML file
        blast_records = NCBIXML.parse(blast_File) #this should return a file 
        proteinList = [] 
        for alignment in blast_records.alignment: ##https://lists.open-bio.org/pipermail/biopython/2012-February/013895.html
            for hsp in alignment.hsps:
                if hsp.expect < 0.05 and hsp.identities == 100:
                    query = blast_records.header.query #wtf
                    proteinList.append(Protein(alignment.title,query,hsp.expect))
        return proteinList
    
    ##protein method to count the number of peptides + assign new count to protein object
    def countPeptides(self):
        pepDict = self.__peptideDict
        count = len(pepDict)
        self.count(count)
    
    ##method to print specific protein's details
    def printProtein(self):
        protName = self.__description
        pepCount = self.__count
        pepDict = self.__peptideDict
        print("The protein " + protName + " has " + pepCount + " peptides. Peptides and e-values are as follows " + pepDict)
        
    ##method to print all of the proteins found in the sample
    @staticmethod
    def printProteins(proteinList):
        i = 0
        protDescript = []
        while i < len(proteinList):
            tmpProtein = proteinList[i]
            tmpDescript = tmpProtein.description
            protDescript[i] = tmpDescript
            i = i + 1
        return protDescript
    
            
        
        

