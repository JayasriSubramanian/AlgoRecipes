def get_number_of_islands(binaryMatrix):
  islandCount = 0
  for ri, row in enumerate(binaryMatrix):
    for cj, cell in enumerate(row):
      islandStack = []
      
      print(ri, cj)
      if binaryMatrix[ri][cj] == 1:
        islandStack.append(ri)
        islandStack.append(cj)

        while islandStack != []:
          print(islandStack)
          cjs = islandStack.pop()
          ris = islandStack.pop()
          if binaryMatrix[ris][cjs] == 1:
            binaryMatrix[ris][cjs] = -1
            if ris != 0:
              islandStack.append(ris-1) 
              islandStack.append(cjs)
            if ris != len(binaryMatrix)-1:
              islandStack.append(ris+1) 
              islandStack.append(cjs)
            if cjs != 0:
              islandStack.append(ris) 
              islandStack.append(cjs-1)
            if cjs != len(binaryMatrix[0]) - 1:
              islandStack.append(ris) 
              islandStack.append(cjs+1)
              
        islandCount +=1
        
  return islandCount  
