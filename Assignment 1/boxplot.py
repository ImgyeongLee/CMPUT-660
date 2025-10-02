# I made it horizontally
# since the box plot has such a long tail
# and a lot of outliers.

import numpy as np
import matplotlib.pyplot as plt

filename = "filename.txt"
counts = []
with open(filename, "r", encoding="utf-8", errors="ignore") as f:
    for line in f:
        try:
            count = int(line.strip().split(";")[-1])
            counts.append(count)
        except ValueError:
            continue

commit_counts = np.array(counts, dtype=np.int64)

plt.figure(figsize=(12,6))
plt.boxplot(commit_counts, vert=False, patch_artist=True)
plt.xscale("log") # Since every single entity has a huge variance.
plt.xlabel("x label is here (log scale)")
plt.title("Nice title (full data)")
plt.tight_layout()
plt.savefig("filename.png", dpi=300) # for scp
plt.show()