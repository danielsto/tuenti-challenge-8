import os


def get_basic_value(comb):
    base = len(comb)
    res = 0
    for i, num in enumerate(reversed(comb)):
        res += num * pow(base, i)
    return res


def get_base(line):
    line = line[0:len(line) - 1]
    res = range(len(line))
    return res


def get_minimum(base):
    minimum = [1, 0]
    for num in base[2:len(base)]:
        minimum.append(num)
    return minimum


def get_maximum(base):
    maximum = []
    # get_maximum()
    for num in reversed(base):
        maximum.append(num)
    return maximum


in_file_path = os.path.join(os.path.dirname(__file__), "submitInput")
out_file_path = os.path.join(os.path.dirname(__file__), "submitOutput.txt")

with open(in_file_path, 'r') as infile:
    with open(out_file_path, 'w') as outfile:
        cases = int(infile.readline())

        for case in range(cases):
            encryption = list(infile.readline())
            base = list(get_base(encryption))

            minimum = get_minimum(base)
            maximum = get_maximum(base)

            res = get_basic_value(maximum) - get_basic_value(minimum)

            outfile.write("Case #" + str(case + 1) + ": " + str(res) + "\n")
