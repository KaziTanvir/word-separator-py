with open("Proverbs.txt", mode="r") as s_file:
    words_all = []

    for line in s_file.readlines():
        words = line.strip().split(" ")
        words_all += words

    unique = set(words_all)

    with open("Unique.txt", mode='w') as write_file:
        for item in sorted(unique):
            write_file.write(item)
            write_file.write("\n")

    print("done")