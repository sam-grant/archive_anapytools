from Mu2eEAF import ReadData as rd 
    
def TestReadFile(): 
    fileName="nts.sgrant.CosmicCRYExtractedCatTriggered.MDC2020ae_best_v1_3.001205_00000231.root" 
    file = rd.ReadFile(fileName) 
    print(file.keys)
    return 

def TestGetFileList(): 
    fileList = rd.ReadData("nts.sgrant.CosmicCRYExtractedCatTriggered.MDC2020ae_best_v1_3.root")
    print(fileList)
    return

TestReadFile()
# TestGetFileList()