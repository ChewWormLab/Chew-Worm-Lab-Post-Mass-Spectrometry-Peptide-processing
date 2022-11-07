import csv ##import the csv libary - required to read the csv file
##creating a peptide "class" i.e. blueprint for an instance of each peptide
class Peptide:
    ##inside the class, will create methods or "functions"
    ##constructor method for the peptide class
    def __init__(self, query:int, observed:float, mr_Expt:float, mr_Calc:float, ppm:float, miss:int, score:int, expect:float, rank:int, peptide_String:str): ##these attributes have been taken from the Excel doc from AR; when an instantiation of the class is created with these parameters passed, it should assign these parameters accordingly
        ##need to ensure that a valid 
        assert query > 0, f"Query {query} is equal to, or less than zero, check that the values have been passed" ##query has to not be of the value 0; f" is a format string prompt for the error message
        ##assign the arguements to the attributes of the class
        self.__uniqueStatus ="unknown" ##will not be set at initalisation of object
        self.__biotinylated = False ##will not be set at initalisation of object
        self.__query = query
        self.__observed = observed
        self.__mr_Expt = mr_Expt
        self.__mr_Calc = mr_Calc
        self.__ppm = ppm
        self.__miss = miss
        self.__score = score
        self.__expect = expect
        self.__rank = rank
        self.__peptide_String = peptide_String ##these are instance attributes (not class attributes)
        ##note that float assigned variables can be passed integers
    
    ##getters for the peptide class - this is extra code written in case there needs to be ongoing modification
    @property
    def query(self):
        return self.__query
    @property
    def observed(self):
        return self.__observed
    @property
    def mrExpt(self):
        return self.__mr_Expt
    @property
    def mrCalc(self):
        return self.__mr_Calc
    @property
    def ppm(self):
        return self.__ppm
    @property
    def miss(self):
        return self.__miss
    @property
    def score(self):
        return self.__score
    @property
    def expect(self):
        return self.__expect
    @property
    def rank(self):
        return self.__rank
    @property
    def peptideString(self): ##the most important one - will be called in other methods
        return self.__peptide_String
    @property
    def biotin(self):
        return self.__biotinylated
    @property
    def uniqueStatus(self):
        return self.__uniqueStatus
    
    ##Mutators
    @query.setter
    def query(self, value): #needs to be passed an int value
        self.__query = value
    
    @observed.setter
    def observed(self, obsFloat):
        self.__observed = obsFloat
    
    @mrExpt.setter
    def mrExpt(self, mrExptFloat):
        self.__mr_Expt = mrExptFloat
    @mrCalc.setter
    def mrCalc(self, mrCalcFloat):
        self.__mr_Calc = mrCalcFloat
    @ppm.setter
    def ppm(self, ppmFloat):
        self.__ppm = ppmFloat      
    @miss.setter
    def miss(self, missInt):
        self.__miss = missInt
    @score.setter
    def score(self, scoreInt):
        self.__score = scoreInt
    @expect.setter
    def expect(self, expectFloat):
        self.__expect = expectFloat
    @rank.setter
    def rank(self, rankInt):
        self.__rank = rankInt
    @peptideString.setter
    def peptideString(self, pepString): ##the most important one - will be called in other methods
        self.__peptide_String = pepString
    @biotin.setter
    def biotin(self, biotinBool): #needs to be passed a boolean value
        self.biotinylated = biotinBool
    @uniqueStatus.setter
    def uniqueStatus(self, uniqueString):
        self.uniqueStatus = uniqueString
       
    ##note CSV values come up with double query symbol and triple quotation marks in excel document; EA's cheap fix is to open CSV file in vs code, use csv viewer and select all instances of query symbol and "" using ctrl+F2 and delete
    ##note csv file needs to have " " around string - select column and follow https://lenashore.com/2012/04/how-to-add-quotes-to-your-cells-in-excel-automatically/ instructions
    
    ##generate list of biotinylated peptide objects!
    @classmethod
    def BiotinListFromCSV(cls):
        with open('1_TID_C_NE_simplified.csv', 'r') as f: ##CHANGE NAME OF CSV FILE TO FILE TO BE READ
            reader = csv.DictReader(f)  ##reads f file as python dictionary; method from csv library, creates dictionary variable named "reader"
            peptideDict = list(reader) ##converts python dictionary into a list
            BiotinList = []
            Biotin = "Biotin"
        for peptide in peptideDict: ##for each index of the dictionary 
            if Biotin in peptide.get('Peptide'): #if the word "biotin" is in peptide string, create the object and append to the list
                BiotinList.append(Peptide( ##instantiating objects from csv using constructor; note appending each object to new list called entireList
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
        return BiotinList #return the list as a variable of all the biotinylated peptides in the csv document
    
    ##generate list of Non biotinylated peptide objects!
    @classmethod
    def noBiotinListFromCSV(cls):
        with open('1_TID_C_NE_simplified.csv', 'r') as f: ##open and read csv file, converts to f variable
            reader = csv.DictReader(f)  ##reads f file as python dictionary; method from csv library, creates dictionary variable named "reader"
            peptideDict = list(reader) ##converts python dictionary into a list
            noBiotinList = []
            Biotin = "Biotin"
        for peptide in peptideDict: 
            if Biotin in peptide.get('Peptide'): ##skip peptide if string contains biotin
                continue
            else:
                noBiotinList.append(Peptide( ##instantiating objects from csv using constructor; note appending each object to new list called entireList
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
        return noBiotinList #return the list as a variable of all the biotinylated peptides in the csv document
    
    ##Generate Peptide Amino Acid String (necessary for BLAST list generation)
    @staticmethod
    def aminoAcidList(peptideList):
        peptideStringList = [] #generating an empty list to hold the strings
        sequenceList =[] #should hold only the amino acid sequences
        i = 0
        j = 0
        while i < len(peptideList):
            tmpPep = peptideList[i]
            tmpString = tmpPep.peptideString
            peptideStringList.append(tmpString) #creating a list of just the sequences
            i +=1
        ##need to split the sequence strings at each point to only have the sequence, no commentary
        while j < len(peptideStringList):
            tmpStr = peptideStringList[j]
            splitString = tmpStr.split("+",1) #this should split at the + symbol, with a  maximum of 2 elements
            seqString = splitString[0] #this should return the string at index 0 AKA the sequence (hopefully!)
            sequenceList.append(seqString) #adds sequence to the new List 
            j += 1
        return sequenceList
    
    ##Generate Query List (necessary for BLAST list generation)
    @staticmethod
    def queryList(peptideList):
        queryList = []
        i = 0
        while i < len(peptideList):
            tmpPep = peptideList[i]
            tmpQuery = tmpPep.query
            queryList.append(tmpQuery)
            i += 1
        return queryList

    ###need to iterate through the biotin list, get JUST the sequences and export to a text file for Blast seq
    @staticmethod
    def blastList(queryList, aminoAcidList):
        blastFile = open("blastSeq.txt", "w")
        for i in range(len(aminoAcidList)):
            blastFile.write(">"+ str(queryList[i]) + "\n" + aminoAcidList[i] + "\n")
        blastFile.close