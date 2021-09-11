# import PythonPractice.packageconcept.Coverters

# or

from PythonPractice.packageconcept.coverters import lb_to_kg,kg_to_lbs

# or

from PythonPractice.packageconcept import coverters

# while importing
# from abc.cde import efg
# means abc is package --> cde is module --> efg is function


# from abc.cde import Efg
# means abc is package --> cde is module --> Efg is class


ll = coverters.kg_to_lbs(522)
print(ll)

kg = lb_to_kg(20)
print(kg)