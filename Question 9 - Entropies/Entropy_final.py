from math import log2

#This function calculates the Joint Chance for our array.
#It is used by the "entropy" function
def joint_chance(array):
    #We generate the length of our tables
    px = [0] * len(array)
    py = [0] * len(array)
    
    for i in range(0, len(array)):
        for j in range(0, len(array[i])):
            px[j] += array[i][j]
            py[i] += array[i][j]
    return px, py

#This function calculates the entropy of X and Y - H(X) and H(Y)
def entropy(array):
    px, py = joint_chance(array)
    hx, hy = 0, 0
    
    for i in range(0, len(px)):
        hx += (-px[i]) * log2(px[i])
        hy += (-py[i]) * log2(py[i])
    return [hx, hy]

#This function calculates the joint entropy of X and Y - H(X,Y)
def joint_entropy(array):
    hxy = 0
    
    for i in range(0, len(array)):
        for j in range(0, len(array[i])):
            if array[i][j] != 0: hxy += (-array[i][j]) * log2(array[i][j])
    return hxy

#This function calculates the donditional entropy of X and Y - H(X|Y),H(Y|X)
#It uses both of the above functions
def conditional_entropy(entropy_xy, joint_entropy):
    return [joint_entropy - entropy_xy[1], joint_entropy - entropy_xy[0]]

#This function calculates the mutual information of X and Y - I(X,Y)
def mutual_info(entropy_xy, commited):    
    return (entropy_xy - commited)

array = [[1/7, 1/7, 1/7], [0, 1/7, 1/7], [2/7, 0, 0]]

entropy_xy = entropy(array)
joint = joint_entropy(array)
conditional = conditional_entropy(entropy_xy, joint)
mutual = mutual_info(entropy_xy[0], conditional[0])
print("The entropy of X and Y is: ", entropy_xy)
print("The joint entropy of X and Y is: ", joint)
print("The conditional entropy of X and Y is: ", conditional)
print("The mutual entropy of X and Y is: ",mutual)