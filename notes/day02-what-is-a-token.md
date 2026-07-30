\# What is a Token?



Large Language Models (LLMs) do not process text in the form of words. Instead, they process \*\*tokens\*\*.



A word can be a single token or it can be split into multiple tokens. For example, the sentence:



"I love learning"



may be represented as three or more tokens depending on the tokenizer used by the model.



A \*\*token\*\* is the smallest unit of text that an AI model processes. A token is not always a complete word; it can be part of a word, a punctuation mark, a number, or other text fragments.



For example, the sentence:



"I love Playing!"



could be tokenized into:



I | love | Playing | !



or differently depending on the tokenizer.



A \*\*tokenizer\*\* is responsible for breaking text into tokens. Different AI models may use different tokenizers, so the same sentence can produce different token sequences.



After tokenization, each token is converted into a unique numeric ID because computers process numbers rather than text.



Every LLM has a maximum number of tokens it can process at one time. This limit is called the \*\*context window\*\*. For example, if an LLM supports 1,000 tokens, it cannot process more than 1,000 tokens in a single request.



The number of tokens also affects AI usage:



\- More input and output tokens generally increase API cost.

\- Processing more tokens usually takes more computation time.

\- The context window determines how much information the model can consider at once.

