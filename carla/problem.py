# class for problem
class Problem():
    # initializing variables for each problem object
    def __init__(self, problemID, size):
        self.problemID = problemID
        self.encodedBin = "####"
        self.finished = False
        self.bin = {}
        self.lastAddedBin = 0
        self.totalLen = 0
        self.totalSize = 0
        self.size = size
    
    # ending problem
    def endProblem(self):
        self.finished = True
    
    # create a new bin for the problem object
    def createNewBin(self, newItem):
        newItem = int(newItem)
        
        self.bin[len(self.bin) + 1] = [newItem]
        self.lastAddedBin = len(self.bin)
    
    # place the new item in the correct bin
    def binPacking(self, newItem):
        newItem = int(newItem)
        
        if len(self.bin) == 0:
            self.createNewBin(newItem)
        else:
            bestBin = None
            for binNum in range(1, len(self.bin)+1):
                if sum(self.bin[binNum]) + newItem <= self.size:
                    if bestBin == None or sum(self.bin[binNum]) > sum(self.bin[bestBin]):
                        bestBin = binNum
            if bestBin == None:
                self.createNewBin(newItem)
            else:
                self.bin[bestBin].append(newItem)
                self.lastAddedBin = bestBin
            
            
                
        self.totalLen += 1
        self.totalSize += newItem
        
        self.encodeBin()

    # encode the bins to a string format
    def encodeBin(self):
        binVal = list(self.bin.values())
        listAllEncodedBins = ["#", "#"]
        
        for i in range(len(binVal)):
            encodeCurrBin = "!".join(str(val) for val in binVal[i])
            listAllEncodedBins.insert(-1, encodeCurrBin)
        
        self.encodedBin = "#".join(str(encodedCurrBin) for encodedCurrBin in listAllEncodedBins)
