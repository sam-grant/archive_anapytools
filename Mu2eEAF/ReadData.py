'''

Utilities for reading files from /pnfs on FNAL EAF. 
Samuel Grant 2024.

Methods from Yuri Oksuzian at https://github.com/oksuzian/mu2etools. 

'''

# External libraries 
import subprocess
import uproot 

# Read a single file
def ReadFile(fileName, quiet=False): 
    try:
        # Setup commands
        commands = "source /cvmfs/mu2e.opensciencegrid.org/setupmu2e-art.sh; muse setup ops;"
        commands += f"echo {fileName} | mdh print-url -s root -"
        if not quiet:
            print(f"---> Reading file:\n{fileName}")
        # Execute commands 
        fileName = subprocess.check_output(commands, shell=True, universal_newlines=True)
        if not quiet:
            print(f"\n---> Created xroot url:\n{fileName}")
            print("---> Opening file with uproot...") 
        # Open the file 
        file = uproot.open(fileName)
        if not quiet: 
            print("Done!")
        return file 
    except OSError as e:
        # Setup alternative commands 
        print(f"\n----> Exception timeout while opening file with xroot, retrying locally: {fileName}")                    
        commands = "source /cvmfs/mu2e.opensciencegrid.org/setupmu2e-art.sh; muse setup ops;"
        commands += f"echo {fileName} | mdh copy-file -s tape -l local -" 
        # Execute commands
        subprocess.check_output(commands, shell=True, universal_newlines=True)
        # Return the opened file 
        return uproot.open(filename)

# Make a file list from a SAM dataset 
def GetFileList(defname):
        print(f"---> Getting file list for {defname}.") 
        # Setup commands
        commands = "source /cvmfs/mu2e.opensciencegrid.org/setupmu2e-art.sh; muse setup ops;"
        commands += f"samweb list-files 'defname: {defname} with availability anylocation' | sort -V "
        # Execute commands 
        fileList = subprocess.check_output(commands, shell=True, universal_newlines=True)
        # Return the file list
        fileList = fileList.splitlines()
        print("Done!")
        return fileList