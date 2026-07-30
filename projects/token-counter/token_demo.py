print("Step 1")

import tiktoken

print("Step 2")
encoding = tiktoken.get_encoding("cl100k_base")
print("Step 3")

text = "I love learning AI."

tokens = encoding.encode(text)

print("Step 4")

print(tokens)
