# Shell commands

### Note

Almost of the commands are made by Imgyeong Lee (me), but I asked ChatGPT to figure out how to run the tasks in parallel. Therefore, the commands might have some modifications from ChatGPT.

All shell commands for this assignment look pretty similar because they are mainly in charge of parsing a specific field of data or eliminating duplicate data.

### Parsing and counting the data from files in /da5_data/basemaps/gz

```shell
for n in {0..N}; do (zcat /da5_data/basemaps/gz/filenameFullU${n}.s 2>> /da5_data/play/yourusername/error.log | awk -F';' '{count[$2]++} END{for(p in count) print count[p] ";" p}' > /da5_data/play/yourusername/yourfilename${n}.txt) || echo "Error at n=$n" >> /da5_data/play/yourusername/error.log & (( $(jobs -r | wc -l) % 5 == 0 )) && wait; done; wait
```

Where N is the last number of the filename. (either 31 or 127)

### Parsing the data and transferring it to datetime

```shell
for n in {0..N}; do (zcat /da5_data/basemaps/gz/filenameFullU${n}.s | awk -F';' '{y=strftime("%Y",$2);m=strftime("%m",$2);d=strftime("%d",$2); print $1 ";" y ";" m ";" d}' > /da5_data/play/yourusername/filename${n}.txt) || echo "Job $n failed with exit code $? at $(date)" >> /da5_data/play/yourusername/errors.log & if (( $(jobs -r | wc -l) >= 5 )); then wait -n; fi; done; wait; echo "All <task name> processing finished!"
```

### Stochastic sampling

```shell
for i in {0..N}; do (echo "Starting file $i..." >&2; zcat /da5_data/basemaps/gz/filenameFullU${i}.s 2>/dev/null | awk -F';' 'BEGIN{srand()} {if(rand()<0.001) print $1}' > /da5_data/play/yourusername/sample${i}.txt; echo "Finished file $i." >&2) & while (( $(jobs -r | wc -l) >= 5 )); do wait -n; done; done; wait; cat /da5_data/play/yourusername/sample*.txt > /da5_data/play/yourusername/sampled_data.txt; rm /da5_data/play/yourusername/sample*.txt
```

`rand()<0.001` part can be changed upon your desired sample size

### How I used `~/lookup` functions for WoC

When I need to grab a certain data which does not have any direct mapping with the other entity, I grab my desired data from the files under `/da5_data/basemaps/gz/` directory, and pass that to `~/lookup` functions. I mainly used `getValues` and `showCnt`, especially for the blobs.

The following command is one of the examples:

```shell
for n in {0..127}; do zcat /da5_data/basemaps/gz/b2fFullU${n}.s | awk -F';' '{print $1}' | while read sha; do echo "$sha" | ~/lookup/showCnt blob >/dev/null 2>&1 && echo "$sha" | ~/lookup/showCnt blob | head -c 4096 | file - | grep -iq text && echo "$sha" | tee -a /da5_data/play/nora/Blob/result.txt; done & (( $(jobs -r | wc -l) % 5 == 0 )) && wait; done; wait; echo "All done!"
```

### Counting the number of lines of the file

This is pretty simple.
`wc -l {filename}`
