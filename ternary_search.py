def ternary_search(input_list, target):
    """The function performs a ternary search on the given array.
    It divides the array into three parts and recursively searches for the target item,
    returning the index of the target if found, otherwise None.
    
    @params input_list: an array with the list of elements to search
    @params target: an integer referring to the element to search for
    
    @return: an integer referring to the index of the target item if found, otherwise None
    """
    
    def _ternary_search_helper(left, right):
        """Recursive helper function for ternary search.
        
        @params left: an integer referring to the left index of the array
        @params right: an integer referring to the right index of the array
        
        @return: an integer referring to the index of the target item if found, otherwise None
        """
        if right >= left:
            mid1 = left + (right - left) // 3
            mid2 = right - (right - left) // 3
            
            if input_list[mid1] == target:
                return mid1
            if input_list[mid2] == target:
                return mid2
            
            if target < input_list[mid1]:
                return _ternary_search_helper(left, mid1 - 1)
            elif target > input_list[mid2]:
                return _ternary_search_helper(mid2 + 1, right)
            else:
                return _ternary_search_helper(mid1 + 1, mid2 - 1)
        
        return None
    
    # Initialize the search with the full array
    return _ternary_search_helper(0, len(input_list) - 1)
