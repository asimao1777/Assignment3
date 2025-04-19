def ternary_search(input_list, left, right, target):

  """The function performs a ternary search on the given array.
  It divides the array into three parts and recursively searches for the target item,
  returning the index of the target if found, otherwise None.
 
  @params arr: an array with the list of elements to search
  @params left: an integer referring to the left index of the array
  @params right: an integer referring to the right index of the array
  @params target: an integer referring to the element to search for

  @return: an integer referring to the index of the target item if found, otherwise None"""
  
  # Checks if the array is not empty (base case)
  if right >= left:
      mid1 = left + (right - left) // 3
      mid2 = right - (right - left) // 3

# Checks if the target is present at mid1 or mid2
      if input_list[mid1] == target:
          return mid1
      if input_list[mid2] == target:
          return mid2

# Checks if the target is present in the first, second or third part of the array (recursive invariant)
      if target < input_list[mid1]:
          return ternary_search(input_list, left, mid1 - 1, target)
      elif target > input_list[mid2]:
          return ternary_search(input_list, mid2 + 1, right, target)
      else:
          return ternary_search(input_list, mid1 + 1, mid2 - 1, target)
      
# Returns None if the target is not found 
  return None

