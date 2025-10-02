import matplotlib.pyplot as plt

years = []
counts = []
with open("number-of-{entity}-per-year.txt") as f:
    for line in f:
        year, count = line.strip().split(";")
        years.append(int(year))
        counts.append(int(count))

plt.figure(figsize=(12,6))
plt.plot(years, counts, marker='o', linestyle='-', color='{color}')
plt.title("Number of {entity} per Year")
plt.xlabel("Year")
plt.ylabel("Number of {entity}")
plt.xticks(years, rotation=45)
plt.grid(True)
plt.tight_layout()
plt.savefig("number-of-{entity}-per-year.png", dpi=300)
plt.show()