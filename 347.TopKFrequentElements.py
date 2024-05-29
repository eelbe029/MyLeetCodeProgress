def topKFrequent(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    liste = {}
    for el in nums:
        if el in liste:
            liste[el] += 1
        else:
            liste[el] = 1
    top_el = []
    print(liste) 
    for num,freq in liste.items():
        if len(top_el) < k:
            top_el.append(num)
        else:
            old = top_el.pop()
            if liste[old] < freq:
                top_el.append(num)
            else:
                top_el.append(old)
        top_el = sorted(top_el,reverse=True)
    return top_el[:k]
print(topKFrequent([6,0,1,4,9,7,-3,1,-4,-8,4,-7,-3,3,2,-3,9,5,-4,0],6))
