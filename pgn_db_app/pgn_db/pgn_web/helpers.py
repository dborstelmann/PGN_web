def findUndergradData(array, val):
     for el in array:
             if el["schoolName"] == "Washington University in St. Louis":
                     return el[val]
