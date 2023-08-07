from Bio.Blast import NCBIXML ##this package is required to parse the XML file
import csv
class Hit(Peptide):
    ##constructor for protein) 
    def __init__(self, query:int, proteinDescript:str, hitSequence:str, eValue:float):
        self.__query = query #this is the query number that is used from the text document generated in peptide parsing.
        self.__description = proteinDescript ##name of protein hit is associated with
        self.__hitSequence = hitSequence ##sequence returned from search
        self.__eValue = eValue
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
            print(i)
            tmpProtein = proteinList[i]
            tmpDescript = tmpProtein.description
            protDescript[i] = tmpDescript
            i = i + 1
        return protDescript
        
    ## Protiens from CSV list
    def ProteinListFromCSV(cls, FilePath):
        with open(FilePath, 'r') as f: ##CHANGE NAME OF CSV FILE TO FILE TO BE READ
            reader = csv.DictReader(f)  ##reads f file as python dictionary; method from csv library, creates dictionary variable named "reader"
            HitDict = list(reader) ##converts python dictionary into a list
            HitList = []
            eValueThreshold = 0.05
            identityPercent = 100
        for hit in HitDict: ##for each index of the dictionary 
            if hit.get('Hsp_evalue') < eValueThreshold:
                if hit.get('Percent Identity') == identityPercent & hit.get('Iteration_query-len') == hit.get('Hsp_positive'): #if percent identity = 100 AND if the query length == the number of positive residues in the same place as the original (double check with AR if this is ok)
                    HitList.append(Hit( ##instantiating objects from csv using constructor; note appending each object to new list called entireList
                        query = int(peptide.get('Query')), ##note that 'title" needs to match column headers
                        observed = float(peptide.get('Observed')),
                        mr_Expt = float(peptide.get('Mr(expt)')),
                        mr_Calc = float(peptide.get('Mr(calc)')),
                        ppm = float(peptide.get('ppm')),
                        miss = int(peptide.get('Miss')),
                        score = int(peptide.get('Score')),
                        expect = float(peptide.get('Expect')),
                        rank = int(peptide.get('Rank')),
                        peptide_String = peptide.get('Peptide'),
                    ))
        return HitList #return the list as a variable of all the biotinylated peptides in the csv document