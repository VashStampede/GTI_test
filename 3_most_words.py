import re
from collections import Counter

text = "Seba CJ2 are based around concept of a boot with integrated padding. \
        This brings benefits of reduced weight and increased precision of following your movements by skate.\
        While CJ Carbon are made, as name suggests, with carbon fibre shell, CJ 2 uses a composite material equivalent.\
        As a result, skate is a bit heavier than its more high end counterpart, but also a bit more flexible. \
        This makes the skate feeling less rigid out of the box and will appeal to skaters who prefer a bit\
        more ankle freedom as well as skates that bend more on tricks. It’s worth to note that while CJ\
        2 are still a nice boot for custom setups with big wheels, they won’t offer the same level of energy\
        transfer efficiency as carbon made ones. If you are after a boot to attach your Wizard frames to – CJ Carbon are \
        still the top choice. On the plus side – composite shell means that skate costs less overall."
words = re.findall(r'\w+', text)
c = Counter(words)

print (c.most_common(3))