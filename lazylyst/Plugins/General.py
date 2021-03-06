from __future__ import print_function
import os

import numpy as np
from obspy import UTCDateTime

# Function to change picking mode to the wanted mode...
# ... Return the original mode if the wanted mode is not defined  
def setPickMode(*args,**kwargs):
    availPickModes=sorted([str(key) for key in args[0].keys()])
    if kwargs['wantMode'] not in availPickModes:
        print('Update pickTypesMaxCountPerSta to be able to place '+str(kwargs['wantMode'])+' picks manually')
    return kwargs['wantMode']

# Swap between highlightint the vertical (P-picking mode) or horizontals (S-picking mode)
def setTracePenAssign(curMode,curAssign):
    # If highlight not defined, define it
    if 'highlight' not in curAssign.keys():
        curAssign={'highlight':['*Z'],'lowlight':['*1','*2','*E','*N']}
    # If pickMode is P, highlight vertical (also do this by default with no picking mode)
    if curMode in ['P','']:
        return {'highlight':['*Z'],'lowlight':['*1','*2','*E','*N']}
    # If pickMode is S, highlight the horizontal (toggle between horizontals if already highlighted)
    elif curMode=='S':
        if '*1' in curAssign['highlight']:
            return {'lowlight':['*1','*E','*Z'],'highlight':['*2','*N']}
        else:
            return {'lowlight':['*2','*N','*Z'],'highlight':['*1','*E']}
    # If not picking P or S, use default
    else:
        return {}
        
# Delete a given pick type, over a specific station (all stations if not specified)
def delPick(pickSet,pickMode,whichSta=None):
    if len(pickSet)==0:
        return '$pass'
    if whichSta is None:
        pickSet=pickSet[np.where((pickSet[:,1]!=pickMode))]
    else:
        pickSet=pickSet[np.where((pickSet[:,0]!=whichSta)|(pickSet[:,1]!=pickMode))]
    return pickSet
    
# Remove all picks from the current pick set
def delPickSet():
    return np.empty((0,3),dtype='a32')
        
# Set the current pick file
def setCurPickFile(curPickFile,pickFiles,nextFile=False,prevFile=False):
    maxFileIdx=len(pickFiles)-1
    prevPickFile=curPickFile
    # Return nothing if no pick files to choose from...
    # ...or if the current pick file is not set
    if maxFileIdx==-1 or curPickFile=='':
        return '$pass'
    curIdx=np.where(pickFiles==curPickFile)[0][0]
    # If the next or previous page, ensure still in bounds
    if nextFile and curIdx+1<=maxFileIdx:
        curPickFile=pickFiles[curIdx+1]
    elif prevFile and curIdx-1>=0:
        curPickFile=pickFiles[curIdx-1]
    # Do not update if nothing has changed
    if prevPickFile==curPickFile:
        return '$pass'
    return str(curPickFile)
    
# Remove the current pick file
def removeCurPickFile(curPickFile,pickFiles):
    if curPickFile in pickFiles:
        pickFiles=pickFiles[np.where(pickFiles!=curPickFile)]
    return pickFiles
    
# Go to the last double clicked station on the map 
def goToStaPage(curMapSta,staSort,staPerPage,curPage):
    if curMapSta is None:
        return '$pass'
    if curMapSta not in staSort:
        return '$pass'
    goToPage=np.where(staSort==curMapSta)[0][0]/staPerPage
    if goToPage==curPage:
        return '$pass'
    else:
        return int(goToPage)
        
# Pan between events
def goToNextPickFile(curPickFile,pickFiles):
    # If not pick files to go to, pass
    if len(pickFiles)==0:
        return '$pass'
    # If the current file isn't present, go to the first
    if curPickFile not in pickFiles:
        idx=0
    # Otherwise go to the next in the list
    else:
        idx=np.where((pickFiles==curPickFile))[0][0]+1
        if idx==len(pickFiles):
            idx=0
    return pickFiles[idx]
    
# Write out stream given current bounds as a MSEED file
# Gives name to file same as the pick file (different extension)
def writeMSEED(stream,timeRange,mainPath,curPickFile):
    outName=curPickFile.replace('.'+curPickFile.split('.')[-1],'.mseed')
    stream.trim(UTCDateTime(timeRange[0]),UTCDateTime(timeRange[1]))
    stream.write(mainPath+'/'+outName,format='MSEED')
    
# Add picks from nearby events with an alternate phase name (to color them differently)
def addNearbyPicks(pickDir,pickFiles,pickTimes,preTime,postTime
                   ,curPickFile,pickSet,givePickType='O'):
    # Get a list of all files whos data would overlap, given pre/post times
    curFileTime=pickTimes[list(pickFiles).index(curPickFile)]
    nearFiles=pickFiles[np.where((pickTimes+preTime<=curFileTime+postTime)&
                                 (pickTimes+postTime>=curFileTime+preTime))]
    # Add all of these files picks with type "givePickType"
    for aFile in nearFiles:
        path=pickDir+'/'+aFile
        # If the file is not empty and is not the current file
        if os.path.getsize(path)!=0 and aFile!=curPickFile:
            # Load the nearby picks
            addPicks=np.genfromtxt(path,delimiter=',',dtype='a32')
            if len(addPicks.shape)==1:
                addPicks=np.array([addPicks])
            # Swap the pick types and add to the current pick set
            addPicks[:,1]=givePickType
            pickSet=np.vstack((pickSet,addPicks))
    # If no picks present, nothing to change
    if 0 in pickSet.shape:
        return '$pass'
    # Remove any of the new picks which are outside the pre/post time
    if givePickType in pickSet[:,1]:
        pickSet=pickSet[np.where((pickSet[:,1]!=givePickType)|
                                 ((pickSet[:,2].astype(float)<=curFileTime+postTime)&
                                 (pickSet[:,2].astype(float)>=curFileTime+preTime)))]
        return pickSet
    # If no added picks, nothing to change
    else:
        return '$pass'
            
    
    
    
    
    
    
    