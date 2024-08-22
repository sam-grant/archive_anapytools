from mu2etools import read_data as rd 
from mu2etools import parallelise as pa
    
def test_parallelise(defname): 
    file_list = rd.get_file_list(defname)
    def process_function(filename):
        file = rd.read_file(filename, quiet=True)
        print() 
        return 
    try:
        pa.multithread(file_list, process_function) 
    except Exception as exc:
        print(f'---> mulithread() generated an exception!{exc}')
    return

test_parallelise(defname='nts.sgrant.CosmicCRYExtractedCatTriggered.MDC2020ae_best_v1_3.root')