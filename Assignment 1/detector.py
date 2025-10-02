import sys
import subprocess
import re

# Note: These language patterns are not really accurate.
# I used Google Gemini to create the regular expressions for those programming languages.
# As I mentioned in the PDF file, this script was only meant for an initial filtering step,
# and I manually checked whether multiple programming languages were actually present.
# The final output has been stored in CSV file.

LANG_PATTERNS = [
    # Java
    (re.compile(r'^\s*package\s+'), 'Java'),
    (re.compile(r'import\s+java'), 'Java'),
    (re.compile(r'^\s*public\s+class'), 'Java'),
    
    # Python
    (re.compile(r'^\s*def\s+'), 'Python'),
    (re.compile(r'^\s*import\s+'), 'Python'),
    
    # JavaScript & TypeScript
    (re.compile(r'function\s*\('), 'JavaScript'),
    (re.compile(r'^\s*const\s+\w+\s*='), 'JavaScript'),
    (re.compile(r'^\s*let\s+\w+\s*='), 'JavaScript'),
    (re.compile(r'^\s*var\s+\w+\s*='), 'JavaScript'),
    (re.compile(r'^\s*interface\s+\w+\s*'), 'TypeScript'),
    (re.compile(r'^\s*type\s+\w+\s*='), 'TypeScript'),
    
    # C / C++
    (re.compile(r'#include\s*<'), 'C/C++'),
    (re.compile(r'int\s+main\s*\('), 'C/C++'),
    
    # C#
    (re.compile(r'using\s+System;'), 'C#'),
    
    # PHP
    (re.compile(r'<\?php'), 'PHP'),
    
    # HTML
    (re.compile(r'<html>|<body>|<div>|<span>'), 'HTML'),
    
    # XML
    (re.compile(r'^\s*<\?xml'), 'XML'),
    
    # CSS
    (re.compile(r'^\s*[.#]?\w+\s*{'), 'CSS'),
    (re.compile(r'^\s*@import\s+'), 'CSS'),
    
    # Ruby (Not super accruate)
    (re.compile(r'^\s*class\s+\w+'), 'Ruby'),
    (re.compile(r'^\s*def\s+\w+'), 'Ruby'),
    
    # Swift
    (re.compile(r'^\s*import\s+UIKit'), 'Swift'),
    (re.compile(r'^\s*class\s+\w+\s*:'), 'Swift'),

    # SQL
    (re.compile(r'^\s*SELECT\s+', re.IGNORECASE), 'SQL'),
    (re.compile(r'^\s*INSERT\s+', re.IGNORECASE), 'SQL'),
    (re.compile(r'^\s*UPDATE\s+', re.IGNORECASE), 'SQL'),
    (re.compile(r'^\s*DELETE\s+', re.IGNORECASE), 'SQL'),

    # Shell (Not super accurate)
    (re.compile(r'^#!.*\b(sh|bash)\b'), 'Shell'),
    (re.compile(r'^\s*(echo|cd|ls|mkdir|rm)\s'), 'Shell'),

    # Markdown (Bad)
    (re.compile(r'^# '), 'Markdown'),
    (re.compile(r'^## '), 'Markdown'),
    (re.compile(r'^\*{1,3}'), 'Markdown'),
]

def detect_languages(blob_sha1):
    detected = set()
    try:
        result = subprocess.run(
            f"echo {blob_sha1} | ~/lookup/showCnt blob",
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True
        )
        output = result.stdout.decode(errors='ignore').splitlines()
            # print(result)
        for line in output[:500]:
            for pattern, lang in LANG_PATTERNS:
                if pattern.search(line):
                    detected.add(lang)
    except Exception:
        pass
    return list(detected)


if __name__ == "__main__":
    for line in sys.stdin:
        blob_sha1 = line.strip()
        if not blob_sha1:
            continue
        langs = detect_languages(blob_sha1)
        if len(langs) >= 1:
            print(blob_sha1, ",".join(langs))