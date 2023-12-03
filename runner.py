import os

testset = ["M667", "M1110", "M2534", "M3810", "M4170", "M6416", "M10243", "M510", "M2593", "M11595"]

for test in testset:
    print(test)
    os.system("python iqtree.py " + test)
    print("\n\n\n")