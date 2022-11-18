from Bio.Blast import NCBIXML
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
        proteinList = [] 
        e_value_threshold = 0.05
        blast_records = NCBIXML.parse(blast_XML_File) #this should return a file 
        i = 0
        for blast_record in blast_records: ##https://lists.open-bio.org/pipermail/biopython/2012-February/013895.html
            for alignment in blast_record.alignments:
                print("if here, is iterating over alignment in blast_record")
                for hsp in alignment.hsps:
                    print("if here, is iterating over hsp elements for each alignment")
                    i = i + 1
                    print(i) ##for some reason not iterating as a list?
                    print(type(hsp.expect))    
                    if hsp.expect < e_value_threshold:
                        # query = blast_record.header.query #wtf
                        # proteinList.append(Protein(alignment.title,query,hsp.expect))
                        i = i + 1
                        print("if here, is iterating over hsp elements < 0.05")
                        print(i)
                
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
        
        


