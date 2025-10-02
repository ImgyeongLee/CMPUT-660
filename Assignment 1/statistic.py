import numpy as np

filename = "filename.txt"
counts = []

with open(filename, "r", encoding="utf-8", errors="ignore") as f:
    for line in f:
        try:
            count = int(line.strip().split(";")[-1])
            counts.append(count)
        except ValueError:
            continue

commit_counts = np.array(counts, dtype=np.int32)

mean = np.mean(commit_counts)
variance = np.var(commit_counts)
std_dev = np.std(commit_counts)

print("Mean:", mean)
print("Variance:", variance)
print("Standard Deviation:", std_dev)