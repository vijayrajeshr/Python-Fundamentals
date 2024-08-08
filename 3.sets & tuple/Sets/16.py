# SET Operators
DCA1={"C","C++","HTML","Windows","MSOffice","Internet"}
DCA2={"Windows","MSOffice","TallyErp9","Internet","Access"}
DCP={"C","C++"}
ADJP={"C","C++","HTML","Java","RMI","Servlets","JavaScript","Internet"}
DMO={"Windows","MSOffice","Internet","Demo"}

DCA1.difference_update(DCA2)
ADJP.intersection_update(DCP)
DCA2.symmetric_difference_update(DMO)

print("DCA1 with DCA2 difference_update:",DCA1)
print("ADJP with DCP intersection_update:",ADJP)
print("DCA2 with DMO symmetric_difference_update:",DCA2)

print("Check DCP is Subset of ADJP :",DCP.issubset(ADJP))
print("Check ADJP is Superset of DCP :",ADJP.issuperset(DCP))
