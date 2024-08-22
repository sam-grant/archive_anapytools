'''

Utilities for reading files from /pnfs on FNAL EAF. 
Samuel Grant 2024.

Methods from Yuri Oksuzian at https://github.com/oksuzian/mu2etools. 

'''

# External libraries 
import subprocess
import uproot 

# Read a single file
def read_file(filename, quiet=False): 
    if not quiet:
        print(f'---> Reading file:\n{filename}')
    try:
        # Setup commands
        commands = 'source /cvmfs/mu2e.opensciencegrid.org/setupmu2e-art.sh; muse setup ops;'
        commands += f'echo {filename} | mdh print-url -s root -'
        # Execute commands 
        filename = subprocess.check_output(commands, shell=True, universal_newlines=True)
        if not quiet:
            print(f'\n---> Created xroot url:\n{filename}')
            print('---> Opening file with uproot...') 
        # Open the file 
        with uproot.open(filename) as file:
            if not quiet: 
                print('Done!')
            return file 
    except OSError as e:
        # Setup alternative commands 
        print(f'\n----> Exception timeout while opening {filename}!\n{e}\n---> Retrying locally.')
        commands = 'source /cvmfs/mu2e.opensciencegrid.org/setupmu2e-art.sh; muse setup ops;'
        commands += f'echo {filename} | mdh copy-file -s tape -l local -'
        # Execute commands
        subprocess.check_output(commands, shell=True, universal_newlines=True)
        # Return the opened file inside a 'with' statement
        with uproot.open(filename) as file:
            return file

# Make a file list from a SAM definition 
def get_file_list(defname, quiet=False): 
    if not quiet:
        print(f'---> Getting file list for {defname}.') 
    try:
        # Setup commands
        commands = 'source /cvmfs/mu2e.opensciencegrid.org/setupmu2e-art.sh; muse setup ops;'
        commands += f"samweb list-files 'defname: {defname} with availability anylocation' | sort -V"
        # Execute commands 
        file_list = subprocess.check_output(commands, shell=True, universal_newlines=True)
        # Return the file list
        file_list = file_list.splitlines()
        if not quiet:
            print("Done!")
        return file_list
    except OSError as e:
        print(f'\n----> Exception timeout while getting file list for {defname}!\n{e}')
        return
        