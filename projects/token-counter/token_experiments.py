import tiktoken

texts = [
    "Hello AI",
    "I love learning AI.",
    "Kubernetes",
    "DevOps Engineer",
    "ನಮಸ್ಕಾರ",
    "🤖🚀",
]

encodings = {
    "gpt2": tiktoken.get_encoding("gpt2"),
    "cl100k_base": tiktoken.get_encoding("cl100k_base"),
    "o200k_base": tiktoken.get_encoding("o200k_base"),
}

for text in texts:
    print("=" * 60)
    print(f"Text: {text}")

    for name, enc in encodings.items():
        tokens = enc.encode(text)
        decoded = enc.decode(tokens)

        print(f"\n{name}")
        print(f"Token count : {len(tokens)}")
        print(f"Token IDs   : {tokens}")
        print(f"Decoded     : {decoded}")