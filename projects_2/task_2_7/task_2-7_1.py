files = ["seq1", "seq2", "seq3", "seq4"]
date = "02.02.2026"  # фиксированная дата взятия образца

for name in files:
    new_name = name + "_" + date + ".fasta"
    print(f"{new_name}")