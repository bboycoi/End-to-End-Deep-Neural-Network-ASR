import os
 

    
'''
	generate text file to data/train
'''
def getListOfFiles(dirName):
    # create a list of file and sub directories 
    # names in the given directory 
    listOfFile = os.listdir(dirName)
    allFiles = list()
    baseDir = os.path.basename(dirName)
    transName = dirName.replace('/','-')+".trans.txt"
    print(transName)
    f = open(transName,"w+")
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory 
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        elif entry[-4:] == '.wav' :
                f.write(entry[:-4]+" "+baseDir[2:]+"\n")
                allFiles.append(entry[:-4]+" "+baseDir[2:])
            
#           allFiles.append(fullPath[57:-4].replace('/','-').replace('_','-')+" "+baseDir[2:])  

    return allFiles        
 
 
def main():
    
    dirName = 'google_home/';
    
    # Get the list of all files in directory tree at given path
    listOfFiles = getListOfFiles(dirName)
        
if __name__ == '__main__':
    main()
