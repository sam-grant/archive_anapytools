from Mu2eEAF import ReadData as rd 
from Mu2eEAF import Parallelise as pa
    
def TestParallelise(): 
    fileList = rd.GetFileList("nts.sgrant.CosmicCRYExtractedCatTriggered.MDC2020ae_best_v1_3.001205_00000231.root")

    def Process(fileName):
        file = rd.ReadFile(fileName)
        with file["TrkAnaExt/trkana]" as tree:
            print(f"---> File {fileName} keys: {tree.keys}") 
        return 

    pd.Parallelise(fileList, processFunction)
        
    return

TestParallelise()