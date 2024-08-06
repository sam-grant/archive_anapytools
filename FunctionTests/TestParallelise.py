from Mu2eEAF import ReadData as rd 
from Mu2eEAF import Parallelise as pa
    
def TestParallelise(): 
    fileList = rd.GetFileList("nts.sgrant.CosmicCRYExtractedCatTriggered.MDC2020ae_best_v1_3.root")

    def processFunction(fileName):
        file = rd.ReadFile(fileName, quiet=True)
        print() 
        return 

    pa.Multithread(fileList, processFunction)
        
    return

TestParallelise()