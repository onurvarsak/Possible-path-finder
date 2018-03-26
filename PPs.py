# -*- coding: utf-8 -*-

######################################################## FILE OPENING #####################################################
import inspect;
import os;
commandsP2 = open(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))+"\\"+ "commandsP2.txt", "r") 
paths = open(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))+"\\"+ "paths.txt", "r") 

######################################################## CHANGEABLES ######################################################
FileInput = []
FilePaths = []
Input = []
Paths = []
outList = []

######################################################## FILE READING #####################################################
FileInput = commandsP2.readlines()
FilePaths = paths.readlines()
######################################################## FILE CLOSEING ####################################################
commandsP2.close()
paths.close()

#-------------------------------------------------------
for i in range(len(FileInput[0])): 
    x=str(FileInput[0][i]).replace(',','')
    if x != '':
        Input.append(x)
        
#-------------------------------------------------------
for i in FilePaths:
    Paths.append(i.split("\n"))
FilePaths = []
#-------------------------------------------------------
for i in range(len(Paths)):
    for j in range(len(Paths[i])):
        if Paths[i][j] != '':
            FilePaths.append(Paths[i][j])
Paths = []
#-------------------------------------------------------
for i in FilePaths:
    Paths.append(i.split(":"))
FilePaths = [[]]
#-------------------------------------------------------
for i in range (len(Paths)):
    FilePaths.append([])
    FilePaths[0].append(Paths[i][0])
    FilePaths[FilePaths[0].index(Paths[i][0])+1].append(Paths[i][1])
Paths =[]
Paths.append(FilePaths[0])
#-------------------------------------------------------
for i in range(1,len(FilePaths)):
    for j in range(len(FilePaths[i])):
        Paths.append(FilePaths[i][j].split(" "))
#-------------------------------------------------------      
        

########################################################
########################################################
##################  MAIN PROGRAM #######################
########################################################
########################################################
x = 0
for i in Input:
    for j in Paths[0]:
        if i == j:
            ################# 1. GO TO CITIES ######################
            ########################################################
            for k in Paths[Paths[0].index(j)+1]:
                outList.append(k)
            
            ################# 2. GO TO  CITIES #####################
            ########################################################                
            for k in outList:
                for l in Paths[0]:
                    if k == l:
                        for m in Paths[Paths[0].index(l)+1]:
                            for n in outList:
                                if m != n:
                                    x += 1
                                    if x == len(outList):
                                        outList.append(m)
                                        x=0
                                        break
                                else:
                                    x = 0
                                    break
                                    
            ################# 3. GO TO CITIES  #####################
            ########################################################
            for k in outList:
                for l in Paths[0]:
                    if k == l:
                        for m in Paths[Paths[0].index(l)+1]:
                            for n in outList:
                                if m != n:
                                    x += 1
                                    if x == len(outList):
                                        outList.append(m)
                                        x=0
                                        break
                                else:
                                    x = 0
                                    break
        
    else:
        if outList == []:
            print "City \'"+i+"\' has no reachable neighbour"
        else:
            print "\'"+i+"\':",outList
    outList=[]





