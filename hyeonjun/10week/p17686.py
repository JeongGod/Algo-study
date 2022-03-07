def solution(files):
    divide_files = []

    for file in files:
        s_num, e_num = 0, len(file)
        for word_idx, word in enumerate(file):
            if word.isnumeric() and not s_num:
                s_num = word_idx
            elif s_num and not word.isnumeric():
                e_num = word_idx
                break

        divide_files.append([file[:s_num], file[s_num:e_num], file[e_num:]])

    divide_files = sorted(
        divide_files, key=lambda x: (x[0].upper(), int(x[1])))

    return list("".join(i) for i in divide_files)
