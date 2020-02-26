def compareTwoVersionStrings(version1, version2):
    """
        Compare two version strings 
    """
    v1 = version1.split(".") # split string version1 by "."
    v2 = version2.split(".") # split string version2 vy "."
    v1 = map(int, v1) # convert version1 string list to int
    v2 = map(int, v2) # convert version2 string list to int
    
    for i in range(len(v1)):
        if v1[i] > v2[i]:
            print("Version {} is greather than Version {}.".format(version1, version2))
        if v2[i] > v1[i]:
            print("Version {} is greather than Version {}.".format(version2, version1))
    if version1 == version2:
        print("Version {} is equal to Version {}.".format(version1, version2))

  
    
# Program that test the lib considering different strings of versions
compareTwoVersionStrings("1.0.7", "2.0.7")
compareTwoVersionStrings("1.0.1", "1.0.1")
compareTwoVersionStrings("1.1", "1.0")