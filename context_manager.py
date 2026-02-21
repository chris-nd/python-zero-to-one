with open(
    r"/Users/Chris/Software Development/TrainingPython/Basics/my_file.txt",
    "r",
    encoding="utf-8",
) as my_file:
    for line in my_file:
        print(line)

with open(
    r"/Users/Chris/Software Development/TrainingPython/Basics/bin_file.bin",
    "bw",
) as bin_file:
    for i in range(100):
        bin_file.write(b"\x3d")