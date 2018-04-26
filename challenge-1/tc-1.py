import os

in_file_path = os.path.join(os.path.dirname(__file__), "submitInput")
out_file_path = os.path.join(os.path.dirname(__file__), "submitOutput.txt")

with open(in_file_path, 'r') as infile:
    with open(out_file_path, 'w') as outfile:
        cases = int(infile.readline())

        for case in range(cases):
            lines = list(map(int, (infile.readline().split())))
            holes = (lines[0]-1) * (lines[1]-1)

            print(holes)
            outfile.write("Case #" + str(case + 1) + ": " + str(holes) + "\n")