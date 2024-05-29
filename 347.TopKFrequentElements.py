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
            top_el.append([num,freq])
        else:
            old = top_el.pop()
            if old[1] < freq:
                top_el.append([num,freq])
            else:
                top_el.append(old)
        top_el.sort(key=lambda x: x[1], reverse=True)
    return [top_el[i][0] for i in range(k)]

print(topKFrequent([6,0,1,4,9,7,-3,1,-4,-8,4,-7,-3,3,2,-3,9,5,-4,0],6))
