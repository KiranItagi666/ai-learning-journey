import tiktoken

# ------------------------------------------------------------
# Model Configuration
# Update prices as needed based on OpenAI pricing.
# Prices are in USD per 1 million INPUT tokens.
# ------------------------------------------------------------

MODELS = {
    "1": {
        "name": "GPT-5",
        "encoding": "o200k_base",
        "price": 1.25
    },
    "2": {
        "name": "GPT-5 Mini",
        "encoding": "o200k_base",
        "price": 0.25
    },
    "3": {
        "name": "GPT-5 Nano",
        "encoding": "o200k_base",
        "price": 0.05
    },
    "4": {
        "name": "GPT-4",
        "encoding": "cl100k_base",
        "price": 2.50
    },
    "5": {
        "name": "GPT-3.5 Turbo",
        "encoding": "cl100k_base",
        "price": 0.50
    }
}

print("=" * 60)
print("🤖 OpenAI Token & Cost Calculator")
print("=" * 60)

print("\nAvailable Models:\n")

for key, model in MODELS.items():
    print(f"{key}. {model['name']}")

choice = input("\nChoose a model (1-5): ").strip()

if choice not in MODELS:
    print("❌ Invalid model selected.")
    exit()

selected = MODELS[choice]

encoder = tiktoken.get_encoding(selected["encoding"])

price_per_million = selected["price"]

print("\n" + "=" * 60)
print(f"Selected Model : {selected['name']}")
print(f"Tokenizer      : {selected['encoding']}")
print(f"Input Price    : ${price_per_million}/1M tokens")
print("=" * 60)

session_tokens = 0
session_cost = 0.0
request_count = 0

while True:

    text = input("\nEnter text ('exit' to quit): ")

    if text.lower() == "exit":
        break

    tokens = encoder.encode(text)
    decoded = encoder.decode(tokens)

    token_count = len(tokens)

    estimated_cost = (token_count / 1_000_000) * price_per_million

    session_tokens += token_count
    session_cost += estimated_cost
    request_count += 1

    print("\n" + "-" * 60)
    print(f"Original Text : {text}")
    print(f"Token Count   : {token_count}")
    print(f"Token IDs     : {tokens}")
    print(f"Decoded Text  : {decoded}")
    print(f"Estimated Cost: ${estimated_cost:.8f}")
    print("-" * 60)

print("\n")
print("=" * 60)
print("📊 Session Summary")
print("=" * 60)

print(f"Model Used          : {selected['name']}")
print(f"Requests Processed  : {request_count}")
print(f"Total Tokens        : {session_tokens}")
print(f"Estimated Total Cost: ${session_cost:.8f}")

print("=" * 60)
print("👋 Thank you for using the Token Calculator!")
