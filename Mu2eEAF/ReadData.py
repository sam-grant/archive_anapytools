'''

Utilities for reading files from /pnfs on FNAL EAF. 
Samuel Grant 2024.

Methods from Yuri Oksuzian at https://github.com/oksuzian/mu2etools. 

'''

# External libraries 
import subprocess
import uproot 

# Read a single file
def ReadFile(fileName): 
    try:
        # Setup commands
        commands = "source /cvmfs/mu2e.opensciencegrid.org/setupmu2e-art.sh; muse setup ops;"
        commands += "echo %s | mdh print-url -s root -" % fileName
        print("---> Reading file:\n\n", fileName)
        # Execute commands 
        fileName = subprocess.check_output(commands, shell=True, universal_newlines=True)
        print("\n---> Created xroot url:\n\n", fileName)
        print("\n---> Opening file with uproot...") 
        # Return the opened file 
        return uproot.open("%s" % fileName)
    except OSError as e:
        # Setup alternative commands 
        print("\n----> Exception timeout while opening file with xroot, retrying locally: %s" % fileName)                    
        commands = "source /cvmfs/mu2e.opensciencegrid.org/setupmu2e-art.sh; muse setup ops;"
        commands += "echo %s | mdh copy-file -s tape -l local -" % fileName
        # Execute commands
        subprocess.check_output(commands, shell=True, universal_newlines=True)
        # Return the opened file 
        return uproot.open("%s" % filename)

# Make a file list from a SAM dataset 
def GetFileList(defname):
        # Setup commands
        commands = "source /cvmfs/mu2e.opensciencegrid.org/setupmu2e-art.sh; muse setup ops;"
        commands += "samweb list-files 'defname: %s with availability anylocation' | sort -V " % defname
        # Execute commands 
        fileList = subprocess.check_output(commands, shell=True, universal_newlines=True)
        # Return the file list
        return fileList.splitlines()