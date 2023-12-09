import os

testset = ["M2593", "M3810", "M4318", "M5379", "M6416", "M4170", "M7929", "M7964", "M14582", "M667"]

for test in testset:
    print(test)
    os.system("python iqtree.py " + test)
    print("\n\n\n")