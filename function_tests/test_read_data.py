from mu2etools import read_data as rd 
    
def test_get_file_list(defname): 
    file_list = rd.get_file_list(defname) 
    print(file_list)
    return

file_list = test_get_file_list(defname='nts.mu2e.CeEndpointMix1BBSignal.Tutorial_2024_03.tka')

def test_read_file(filename):  
    file = rd.read_file(filename) 
    return 

test_read_file(file_list[0])