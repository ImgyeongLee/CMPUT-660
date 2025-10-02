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

counts = np.array(counts, dtype=np.int64)
counts.sort()

# line 17 has ChatGPT's modification
cdf = np.arange(1, len(counts)+1) / len(counts)

plt.figure(figsize=(10,6))
plt.plot(counts, cdf, linewidth=1)
plt.xscale('log')
plt.xlabel("x lable (log scale)")
plt.ylabel("y lable")
plt.title("Nice title")
plt.grid(True, which="both", linestyle="--", linewidth=0.5)
plt.tight_layout()
plt.savefig("filename.png", dpi=300)
plt.show()