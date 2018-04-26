import os
from itertools import groupby

whole_step_notes = ['A', 'C', 'D', 'F', 'G']
half_step_notes = ['B', 'E']

# 2 = whole step (W) | 1 = half step (H)
major = [2, 2, 1, 2, 2, 2, 1]
minor = [2, 1, 2, 2, 1, 2, 2]

notes = {'A': 0, 'A#': 1, 'B': 2, 'C': 3, 'C#': 4, 'D': 5, 'D#': 6, 'E': 7, 'F': 8, 'F#': 9, 'G': 10, 'G#': 11}


def flat_to_sharp(note):
    code = notes[note[0]] - 1
    return list(notes.keys())[list(notes.values()).index(code)]


def get_scale(key):
    scale = []
    variant = key[0]

    root = key[1:]
    if len(root) == 2 and root[1] == 'b':
        root = flat_to_sharp(root)

    scale.append(root)
    # print(scale)
    code = notes[root]
    if variant == 'M':
        for i, step in enumerate(major):
            # print(i, step)
            code += step
            if code > 11:
                code = code - 12
            scale.append((list(notes.keys())[list(notes.values()).index(code)]))
    else:
        for i, step in enumerate(minor):
            # print(i, step)
            code += step
            if code > 11:
                code = code - 12
            scale.append((list(notes.keys())[list(notes.values()).index(code)]))
    return scale


def generate_all_scales():
    all_scales = dict()
    for x in notes:
        all_scales['M' + x] = get_scale('M' + x)
        all_scales['m' + x] = get_scale('m' + x)
    return all_scales


all_scales = generate_all_scales()

# for element in all_scales:
#     print(element + ': ' + str(all_scales[element]))

in_file_path = os.path.join(os.path.dirname(__file__), "testInput")
out_file_path = os.path.join(os.path.dirname(__file__), "testOutput.txt")

with open(in_file_path, 'r') as infile:
    with open(out_file_path, 'w') as outfile:
        cases = int(infile.readline())
        for case in range(cases):
            notes = (infile.readline().rstrip())
            # print(notes)

            res = []

            if notes != '0':
                print('Calculating keys...')
                piece = (infile.readline().rstrip().split(' '))
                piece = [key for key, grp in groupby(piece)]
                print('PIECE:', piece)
            else:
                # Include all possible keys
                print('--- All possible keys ---')
                for element in all_scales:
                    res.append(element)
                    res.sort()
                res = ' '.join(res)
            # outfile.write("Case #" + str(case + 1) + ": " + str(res) + "\n")