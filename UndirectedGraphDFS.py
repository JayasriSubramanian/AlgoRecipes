def get_number_of_islands(binaryMatrix):
  #pass # your code goes here
  def check_element(rowi, colj):
    if binaryMatrix[rowi][colj] == 1:
      print("L8row" + str(rowi) + "col" + str(colj))
      binaryMatrix[rowi][colj] = 'V'
      if rowi > 0:
        check_element(rowi-1, colj)
      
      if colj < len(binaryMatrix[rowi])-1:
        check_element(rowi, colj+1)
      
      if rowi < len(binaryMatrix) - 1:
        check_element(rowi+1, colj)
      
      if colj > 0:
        check_element(rowi, colj-1)
      
    return True
  islandCount = 0  
  for rowi, row in enumerate(binaryMatrix):

    for colj, element in enumerate(row):
      
      if element == 1:
        check_element(rowi, colj)
        islandCount += 1
        print("L31row" + str(rowi) + "col" + str(colj) + "islandCount" + str(islandCount))

  return islandCount 
  
