def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    cross = {}
    
    for singles in arrays:
        for value in singles:
            if value not in cross:
                cross[value] = 1
            else:
                cross[value] += 1
                
    reverse = {}
                
    for key, value in cross.items():
        if value not in reverse:
            reverse[value] = [key]
        else:
            reverse[value].append(key)
            
    result = reverse[len(arrays)]
                
    

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
