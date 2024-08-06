'''

Utilities for parallelising analysis jobs on FNAL EAF. 
Samuel Grant 2024.

Methods from Yuri Oksuzian at https://github.com/oksuzian/mu2etools. 

'''

from concurrent.futures import ThreadPoolExecutor, as_completed

# Execute a given function on a list of files in parallel.
def Multithread(fileList, processFunction):
    with ThreadPoolExecutor() as executor:
        # Submit tasks to the executor
        futures = {executor.submit(processFunction, fileName): fileName for fileName in filelist}
        # Process results as they complete
        for future in as_completed(futures):
            filename = futures[future]
            try:
                future.result()  # Retrieve the result or raise an exception if occurred
                print(f'---> {fileName} processed successfully!')
            except Exception as exc:
                print(f'---> {fileName} generated an exception!\n{exc}')

