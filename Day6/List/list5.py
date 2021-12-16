from typing import List

sample: List[str] = ['abc', 'xyz', 'aba', '1221', 'appllppa', 'apdjlrn']
a = sample[0]
for i in range(len(sample)):
    if len(sample[i]) > 3:
        le = len(sample[i])
        st = sample[i]
        if st[1] == st[i]:
            print(sample[i])
