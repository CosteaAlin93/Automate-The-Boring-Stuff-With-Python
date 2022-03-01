The long and tiring method. 

![cc5e39c88a1e4d70bca751d778a5ec45.png](:/eb931a077d05470885e5e3c08d09bb81)

---

A bit more elaborate:

![3c28ec917dbba447efa937f0f4282f4d.png](:/338febbca1a442cca4776cee110ab11f)

---

Simpler:

![4ffbb3f4210d641982cf78081f75c293.png](:/df7b8e43e9c54350a731b0f5964697e2)


- .search(message) to find first occurence
```
import re

message = 'Call me at 444-555-6666 today, as from tomorrow I`ll only be available at 444-555-7777'
phoneNumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumberRegex.search(message)
print(mo.group())
```

---

- .findall(message)    to find all occurences
![73525f939fa16ae503c3388084e77abc.png](:/ea078d7b32844157a5f1dbbc89eadfce)

---

RECAP:

![2cd5cf75cc76287778d77b74ebd8acde.png](:/6d54d15778d440d08f536597ccaa4ee5)

---

![ed0efe597b33a0f6639ebbe37db8a4ab.png](:/9ad498e96f5649f5a2a6d86532c14fce)

---

![1baffd14530dd5428119fe7d50798028.png](:/471c2ad1b55b41bba5ef2fe455eefd49)

---

- Find paranthesis with the escape character '\'
![197e3e1f91d31a5b6de563599dd3ea5d.png](:/4138fa47d5434308b52bc3008030359a)

---

PIPE

![8a52c3aec072b6cb2cf723a4eb941153.png](:/af53eb60abcf42e99677ed23dfd207a4)

---

RECAP:

![16b8d11388191465c3f2fae84ab7dda0.png](:/ddea7dc93df44cee987ce8c052a8c009)

---

- ? - never or one appeareance of the mentioned text
![9dd86055152d1673c362592a2ddadbcf.png](:/e50ab60ccab442278d41f84a71105bbd)
	- ? Can be escaped with \
	
- 	The \* character:  Zero or more times
![72224076a0082377ca9e441d7d24c90f.png](:/b96db6c921ef456599fb11c013001ee0)

- The plus character + : one more more repetitions. Never none.
![8e44b6ba0c3bbad53b6344b4f8c50783.png](:/ce9ff91feb4844a4804c441bbadadd55)

- {x} : specific number of repetitions
![621f5232d2fcaf9aeaa6a290bdf736ee.png](:/fc5b8346081742878f6435ca9dd12585)

- {x,y} : at least x, at most y
![196bdc84112b2f6d5aaad5675f7fd2a7.png](:/fa4cf471c0114ec28835c4c7dfa0c6ff)
	 - {,3} : 0 to 3
	 - {3,}: 3 to more
	 - {3,5}? -- Non greedy match (the smallest possible string)
	 ![d3fb909af28c0083f4a20c7e22c02fe0.png](:/de88ab6a7d174b23b458157d02b423ca)
	 
	
	
---

Greedy matches : Python tries to match the longest string possible.

RECAP:
---


![4c508aebd7b476e916bd305bc54c51fc.png](:/549c77aa293143aeb543dc718d2aeb47)

---

