from Bio import SearchIO
from Bio.Seq import Seq
import csv
import os
import datetime

##this class will create an object for each result from the Blast Search's CSV file. This will be use to generate a final protein object

class HSP:
    ##constructor for protein) 
    def __init__(self, query:int, geneId:str, proteinDescript:str, hitSequence:str, eValue:float):
        self.__query = query #this is the query number that is used from the text document generated in peptide parsing.
        self.__description = proteinDescript ##name of protein hit is associated with
        self.__geneId = geneId
        self.__hitSequence = hitSequence ##sequence returned from search
        self.__eValue = eValue
        self.__count = 0
        self.__hitDict = [{hitSequence:eValue}] ##list of dictionary objects
    ##getters AKA accessors (return the variable)
    @property
    def query(self):
        return self.__query       
    @property
    def description(self):
        return self.__description     
    @property
    def hitSequence(self):
        return self.__hitSequence 
    @property
    def eValue(self):
        return self.__eValue 
    @property
    def hitDict(self):
        return self.__hitDict 
    @property
    def count(self): 
        return self.__count
    @property
    def geneId(self): 
        return self.__geneId
    
    ##setters AKA mutators
    @description.setter
    def description(self, descript):
        self.__description = descript
    
    @hitDict.setter
    def hitDict(self, dictionary):
        self.__hitDict = dictionary

    @count.setter
    def count(self, num):
        self.__count = num  
    
    
    ##protein method to count the number of peptides + assign new count to protein object
    def countPeptides(self):
        pepDict = self.__hitDict
        count = len(pepDict)
        self.count(count)
    
    ##test print method
    def printHit(self):
        print("Hit is " + self.__description  + " with an e Value of " + self.__eValue)
    
    ## Hits from CSV results of BlastSearch --> NOT RECOMMENDED
    ##will generate a list of Hit objects which will be used to generate a Protein List
    @classmethod
    def HSPListfromCSV(cls,FilePath):
        with open(FilePath, 'r') as f: ##CHANGE NAME OF CSV FILE TO FILE TO BE READ
            reader = csv.DictReader(f)  ##reads f file as python dictionary; method from csv library, creates dictionary variable named "reader"
            BlastSearch = list(reader) ##converts python dictionary into a list
            BlastSearchList = []
            eValueThreshold = 0.05
            identityPercent = 100.0
            i = 0
            for hit in BlastSearch: ##for each index of the dictionary 
                if float(hit.get('Hsp_evalue')) < eValueThreshold:
                    if (float(hit.get('Percent Identity')) == identityPercent) and (hit.get('Iteration_query-len') == hit.get('Hsp_positive')): #if percent identity = 100 AND if the query length == the number of positive residues in the same place as the original (double check with AR if this is ok)
                        BlastSearchList.append(HSP( ##instantiating objects from csv using constructor; note appending each object to new list called entireList
                            query = int(hit.get('Iteration_query-def')), ##note that 'title" needs to match column headers
                            proteinDescript = str(hit.get('Hit_def')),
                            hitSequence = str(hit.get('Hsp_hseq')),
                            eValue = float(hit.get('Hsp_evalue')),
                        ))
        f.close()
        Update_hpsObjects = BlastSearchList
        i = 0
        while i < len(Update_hpsObjects):
            tmpHSP = Update_hpsObjects[i] ##tmp variable to hold current hsp obj data 
            j = i+1
            while j <len(Update_hpsObjects):
                nextHSP = Update_hpsObjects[j]
                if nextHSP.description == tmpHSP.description: ##if 2 HSPs have the description
                    tmpDict = []
                    tmpDict = tmpHSP.hitDict
                    nextDict = nextHSP.hitDict
                    tmpDict.append(nextDict)
                    setattr(tmpHSP,'hitDict',tmpDict)
                    Update_hpsObjects [i] = tmpHSP
                    Update_hpsObjects.pop(j)##remove the repeat after it has been added to the original entry
                    ##unsure if need to update the index after removing an item, expecting it to remove the it
                else:
                    j+=1
            i+=1
        return Update_hpsObjects
      
    ##testing the parsing; http://biopython.org/DIST/docs/tutorial/Tutorial.
    ## %identity calculated using https://environmentalmicrobiome.biomedcentral.com/articles/10.1186/s40793-020-00361-y ;17-06-2023
    ## features from Biotin Record class determined via Biopython tutorial + Biopython Search IO output object XML https://biopython.org/docs/1.81/api/Bio.SearchIO.BlastIO.html 
    @classmethod
    def HSPListfromXML(cls,FilePath):
        with open(FilePath,'r') as f:
            hspObjects = []
            xmlResults = SearchIO.parse(f,"blast-xml") ##will iterate over the BLAST output file (this is XML formatted)
            metaList = []
            baseBLASTname = os.path.basename(FilePath)
            BLASTname = os.path.splitext(baseBLASTname)[0]
            filecreationTime = os.path.getctime(FilePath)   
            for query in xmlResults: ##XML results is a file containing all of the results for each query sequence as a SearchIO object
                BLASTdb = query.target
                BLASTprogram = query.program
                BLASTver = query.version
                BLASTref = query.reference ##extracting meta info and assigning it to list outside of iteration
                metaList.append(BLASTdb)
                metaList.append(BLASTprogram)
                metaList.append(BLASTver) 
                metaList.append(BLASTref)
                for hit in query: ## each hit is an identified protein that matches the query sequence        
                    for hsp in hit: ##each HSP is a sequence from the hit, that is highly matching with the query sequence
                        hspHitLen = len(hsp.hit) ##returns seqObject; 
                        hspQueryLen = len(hsp.query)
                        if ((hsp.ident_num/hsp.aln_span)*100) == 100 and hspHitLen == hspQueryLen and hsp.gap_num == 0 and hsp.evalue <0.05: ##100% identity + length of query seq is same as length of hit + no gap + eVALUE<0.05,ask AR about redundancy
                            hspObjects.append(HSP(
                                query = int(hsp.query_id),
                                geneId=(hsp.hit_id),
                                proteinDescript= (hsp.hit_description),
                                hitSequence = str((hsp.hit).seq),
                                eValue= float(hsp.evalue)
                            ))
                metaName = BLASTname + " meta.txt"
                with open(metaName,"w") as m:
                    m.write("BLAST program: "  + metaList[1] + "\n"
                        + "BLAST database: "+ metaList[0] + "\n"
                        + "BLAST version" + metaList[2] +"\n"
                        + "BLAST reference: " + metaList[3] +"\n"
                        +"Date of search: " + str(datetime.datetime.fromtimestamp(filecreationTime)) ##date of file creation
                    )
                m.close
            f.close()
        return hspObjects
    @classmethod
    def refinedList(cls,hspObjects):
        Update_hpsObjects = hspObjects
        i = 0
        while i < len(Update_hpsObjects):
            tmpHSP = Update_hpsObjects[i] ##tmp variable to hold current hsp obj data 
            j = i+1
            while j <len(Update_hpsObjects):
                nextHSP = Update_hpsObjects[j]
                if nextHSP.description == tmpHSP.description: ##if 2 HSPs have the description
                    tmpDict = []
                    tmpDict = tmpHSP.hitDict
                    nextDict = nextHSP.hitDict
                    tmpDict.append(nextDict)
                    setattr(tmpHSP,'hitDict',tmpDict)
                    Update_hpsObjects [i] = tmpHSP
                    Update_hpsObjects.pop(j)##remove the repeat after it has been added to the original entry
                    ##unsure if need to update the index after removing an item, expecting it to remove the it
                else:
                    j+=1
            i+=1
        return Update_hpsObjects
    
    @classmethod ##method in case individuals want to print out entire HSP list in terminal
    def printHSPList(cls,proteinList):
        i = 0
        while i < len(proteinList):
            tmpProtein = proteinList[i]
            proteinName = tmpProtein.description
            proteinDictionary = tmpProtein.hitDict
            print("Protein name: " + proteinName)
            print(proteinDictionary)
            if len(tmpProtein.hitDict) > 1:
                print (proteinName + " has " + str(len(tmpProtein.hitDict)) + " hits from the BLAST search")
            i += 1
    
    @classmethod ##method in case individuals want to print out a list of all the HSPs which have multiple appearances
    def printMultipleHits(cls,proteinList):
        i = 0
        j = 0
        while i < len(proteinList):
            tmpProtein = proteinList[i]
            proteinName = tmpProtein.description
            proteinDictionary = tmpProtein.hitDict
            if len(tmpProtein.hitDict) > 1:
                print (proteinName + " has " + str(len(tmpProtein.hitDict)) + " hits from the BLAST search")
                print(proteinDictionary)
                j +=1
            i +=1
        print(j)
    
    ## https://www.ncbi.nlm.nih.gov/sites/batchentrez => for bulk geneId search
    @classmethod
    def protein_HitCSV(cls,hspList, refinedHSPList, fileName, metaFile):
        file = fileName+"Protein-Hits"
        txtFile = fileName + "gene_Ids"
        with open(metaFile,'r') as m:
            metaInfo = m.read()
        with open(f"{file}.csv", "w", newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["BLAST search Information: ",metaInfo])
            writer.writerow([])
            writer.writerow(["genBank ID", "Protein Description","Number of Hits", "Hit Sequences with corresponding E values"])
            for HSP in refinedHSPList:
                writer.writerow([HSP.geneId,HSP.description,len(HSP.hitDict),HSP.hitDict])
        f.close
        m.close
        with open(f"{txtFile}.txt","w") as a:
            for HSP in hspList:
                geneId = HSP.geneId
                stringList= geneId.split("|")
                gene = stringList[1] ##should return the mid part of a string split at each | e.g. should hopefully return NP_001366805.1
                a.write( gene + "\n")
            a.close