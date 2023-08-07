#https://stackoverflow.com/questions/56135329/how-do-i-iterate-through-all-files-inside-a-given-directory-and-create-folders-a
#note this will create a python folder for the python code file bulk files

##MOVE THIS CODE FILE INTO THE DIRECTORY OF INTEREST -> every HTML file inside the folder will be moved to a new
##created file that will have the same name as a file


import os, shutil

##insert address of folder containing all html files here
parent_folder = 'E:\Exp 4 - transfer_3012295_files_2de11099\AP060323_QE CElegans\HTML files (CAN BE OPENED IF NEEDED)\\'#make sure to add the double back slash at the end of the code folder; 

##insert address of folder continaing all the coding files here
code_folder = 'E:\Exp 4 - transfer_3012295_files_2de11099\Coding Files\\' #make sure to add the double back slash at the end of the code folder; 
files = [name for name in os.listdir(parent_folder) if os.path.isfile(os.path.join(parent_folder, name))]

for f_name in files:
    file = os.path.join(parent_folder, f_name)  # full path

    folder_name = f_name.split('.')[0]  # removes file extension
    
    ##will only create new files for html files
    if file.endswith(".htm"):
        
        ##creates a full path for a new folder
        Samplefolder = os.path.join(parent_folder, folder_name)  

        if not os.path.exists(Samplefolder):  # checks folder has not existed before
            os.mkdir(Samplefolder)
        shutil.move(file, os.path.join(Samplefolder, f_name))  # move files into new folder. 
        
        ##copying python code files into the new folders
        for codefile_name in os.listdir(code_folder):
            sourceCodeFile = os.path.join(code_folder, codefile_name) ##gets the full path of the code files
            destCodefILE = os.path.join(Samplefolder,codefile_name) ##creates a full path of a file in the created sample folder. Destination code file
            shutil.copy(sourceCodeFile,destCodefILE)