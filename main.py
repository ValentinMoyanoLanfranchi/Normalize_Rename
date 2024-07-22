import os
import unicodedata

rootDir = '' # Insert the directory that you want to normalize

def StripAccents(s):
   return ''.join(c for c in unicodedata.normalize('NFD', s)
                  if unicodedata.category(c) != 'Mn')

def ReplaceInvalidCharacter(path):
    for Directory_Name, subdirList, fileList in os.walk(path, topdown=True):
        for File_Name in fileList:
            New_File_Name = File_Name.replace("´", " ")
            os.rename(Directory_Name+"/"+File_Name,Directory_Name+"/"+New_File_Name)
            
def Normalize(path):
    for Directory_Name, subdirList, fileList in os.walk(path, topdown=True):
        normalized_folder = StripAccents(Directory_Name)
        os.rename(Directory_Name,normalized_folder)
        
        for File_Name in fileList:
            normalized_file = StripAccents(File_Name)
            os.rename(Directory_Name+"/"+File_Name,Directory_Name+"/"+normalized_file)
        
def FindExtension(file_name):
    extension = ""
    extension_founded = False
    for character in file_name:
        if character == "." or extension_founded:
            if extension_founded:
                extension += character
            extension_founded = True
    return extension

ReplaceInvalidCharacter(rootDir)
Normalize(rootDir)
    