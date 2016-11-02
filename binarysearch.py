class BinarySearch(list):

  def __init__(self, a, b): #Creates list of length a with steps of b between elements
    self.a = a
    self.b = b
         
    for num in range(self.a):
      list.append(self, self.b)
      self.b +=b
      num +=1
  
    self.length = num

  def search(self,value):
    first = 0
    last = self.length-1
    found = False
    count = 0
    in_list = False
    try:
      index = self.index(value)
      in_list = True
    except ValueError:
      index = -1
      in_list = False

    while first<=last and not found and in_list and value != self[last]:
        midpoint = (first+last)//2
        mid_value = self[midpoint]
        if mid_value == value:
            found = True
            count +=1
            index = midpoint
        else:
            if value < mid_value:
                last = midpoint - 1
                count +=1
            else:
                first = midpoint + 1
                count +=1
    
    
    return {"count": count, "index": index}    