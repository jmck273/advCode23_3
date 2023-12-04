import re
def getContent(fileURL):
    '''
    Getting the content of the URL. To not overwhelm the Advent of code server, I have saved
    the file locally as a text file. There shouldn't be the need for these exceptions as I have included the
    text file in the repo, but it is meant to be good coding practices
    '''
    try:
        with open(fileURL, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"File '{fileUrl}' not found")
        return None
    except Exception as e:
        print(f"Error Occurred: {e}")
        return None
    
def checkVal(val):
    return (not val.isnumeric() and val != ".")

def findPartNumber(textIn):
    symbolList = ["!","@","#","$","%","^","&","*","(",")","_","-","+","=","/","?"]
    pattern = re.compile(r'(\d+)')
    lineLen = len(textIn[0])
    textLen = len(textIn)
    totSum = 0
    for j in range(len(textIn)):
        for matches in pattern.finditer(textIn[j]):
            #print(match)
            foundVal = False
            lowIndex, highIndex = matches.span()
            highIndex -= 1
            match = matches.group()
            #Left Side Boundary
            if lowIndex > 0:
                if checkVal(textIn[j][lowIndex-1]) and not foundVal:
                    totSum += int(match)
                    foundVal = True
            #Right Side Boundary
            if highIndex < lineLen-1:
                if checkVal(textIn[j][highIndex + 1]) and not foundVal:
                    totSum += int(match)
                    foundVal = True
            #Upper Line Boundary
            if j == 0:
                for i in range(lowIndex,highIndex+1):
                    if checkVal(textIn[j+1][i]) and not foundVal:
                        totSum += int(match)
                        foundVal = True
                        break
                #Corners
                if lowIndex > 0:
                   if checkVal(textIn[j+1][lowIndex-1]) and not foundVal:
                        totSum += int(match)
                        foundVal = True 
                if highIndex < lineLen-1:
                    if checkVal(textIn[j+1][highIndex + 1]) and not foundVal:
                        totSum += int(match)
                        foundVal = True
            elif j == (textLen - 1):
                for i in range(lowIndex,highIndex+1):
                    if checkVal(textIn[j-1][i]) and not foundVal:
                        totSum += int(match)
                        foundVal = True
                        break
                #Corners
                if lowIndex > 0:
                   if checkVal(textIn[j-1][lowIndex-1]) and not foundVal:
                        totSum += int(match)
                        foundVal = True 
                if highIndex < lineLen-1:
                    if checkVal(textIn[j-1][highIndex + 1]) in symbolList and not foundVal:
                        totSum += int(match)
                        foundVal = True
            else:
                for i in range(lowIndex,highIndex+1):
                    if (checkVal(textIn[j-1][i]) or checkVal(textIn[j+1][i])) and not foundVal:
                        totSum += int(match)
                        foundVal = True 
                #Corners
                if lowIndex > 0:
                   if (checkVal(textIn[j+1][lowIndex-1]) or checkVal(textIn[j-1][lowIndex-1])) and not foundVal:
                        totSum += int(match)
                        foundVal = True 
                if highIndex < lineLen-1:
                    if (checkVal(textIn[j+1][highIndex + 1]) or checkVal(textIn[j-1][highIndex + 1])) and not foundVal:
                        totSum += int(match)
                        foundVal = True
    
    return totSum

def findGears(textIn):
    retSum = 0
    lineLen = len(textIn[0])
    textLen = len(textIn)
    pattern = re.compile(r'(\d+)')
    symbolList = ["*"]
    matchArr = []
    matchSet = set()
    for j in range(len(textIn)):
        for matches in pattern.finditer(textIn[j]):
            foundVal = False
            lowIndex, highIndex = matches.span()
            highIndex -= 1
            match = matches.group()
            #Left Side Boundary
            if lowIndex > 0:
                if checkVal(textIn[j][lowIndex-1]) and not foundVal:
                    matchArr.append((int(match),(j,lowIndex-1)))
                    foundVal = True
            #Right Side Boundary
            if highIndex < lineLen-1:
                if checkVal(textIn[j][highIndex + 1]) and not foundVal:
                    matchArr.append((int(match),(j,highIndex + 1)))
                    foundVal = True
            #Upper Line Boundary
            if j == 0:
                for i in range(lowIndex,highIndex+1):
                    if checkVal(textIn[j+1][i]) and not foundVal:
                        matchArr.append((int(match),(j+1,i)))
                        foundVal = True
                        break
                #Corners
                if lowIndex > 0:
                   if checkVal(textIn[j+1][lowIndex-1]) and not foundVal:
                        matchArr.append((int(match),(j+1,lowIndex-1)))
                        foundVal = True 
                if highIndex < lineLen-1:
                    if checkVal(textIn[j+1][highIndex + 1]) and not foundVal:
                        matchArr.append((int(match),(j+1,highIndex + 1)))
                        foundVal = True
            elif j == (textLen - 1):
                for i in range(lowIndex,highIndex+1):
                    if checkVal(textIn[j-1][i]) and not foundVal:
                        matchArr.append((int(match),(j-1,i)))
                        foundVal = True
                        break
                #Corners
                if lowIndex > 0:
                   if checkVal(textIn[j-1][lowIndex-1]) and not foundVal:
                        matchArr.append((int(match),(j-1,lowIndex-1)))
                        foundVal = True 
                if highIndex < lineLen-1:
                    if checkVal(textIn[j-1][highIndex + 1]) in symbolList and not foundVal:
                        matchArr.append((int(match),(j-1,highIndex + 1)))
                        foundVal = True
            else:
                for i in range(lowIndex,highIndex+1):
                    if (checkVal(textIn[j-1][i]) or checkVal(textIn[j+1][i])) and not foundVal:
                        if checkVal(textIn[j-1][i]):
                            matchArr.append((int(match),(j-1,i)))
                        if checkVal(textIn[j+1][i]):
                            matchArr.append((int(match),(j+1,i)))
                        foundVal = True 
                #Corners
                if lowIndex > 0:
                   if (checkVal(textIn[j+1][lowIndex-1]) or checkVal(textIn[j-1][lowIndex-1])) and not foundVal:
                        if checkVal(textIn[j-1][lowIndex-1]):
                            matchArr.append((int(match),(j-1,lowIndex-1)))
                        if checkVal(textIn[j+1][lowIndex-1]):
                            matchArr.append((int(match),(j+1,lowIndex-1)))
                        foundVal = True 
                if highIndex < lineLen-1:
                    if (checkVal(textIn[j+1][highIndex + 1]) or checkVal(textIn[j-1][highIndex + 1])) and not foundVal:
                        if checkVal(textIn[j-1][highIndex + 1]):
                            matchArr.append((int(match),(j-1,highIndex + 1)))
                        if checkVal(textIn[j+1][highIndex + 1]):
                            matchArr.append((int(match),(j+1,highIndex + 1)))
                        foundVal = True
    for i in range(len(matchArr)-1):
        indexList = []
        if matchArr[i][1] in matchSet: continue
        for j in range(i+1,len(matchArr)):
            if matchArr[i][1] == matchArr[j][1]:
                indexList.append(j)
        matchSet.add(matchArr[i][1])
        if len(indexList) == 1:
            retSum += matchArr[i][0] * matchArr[indexList[0]][0]

    return retSum

if __name__ == "__main__":
    textStr = getContent("input.txt")
    textSplit = textStr.splitlines()
    print(findGears(textSplit))
    