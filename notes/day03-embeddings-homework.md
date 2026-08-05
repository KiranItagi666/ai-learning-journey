# Day 3 Homework – Embeddings

## Q1. What is an embedding?
An embedding is a dense vector of numbers that represents the semantic meaning of a word, sentence, or document. Similar meanings have embeddings that are close together in vector space.

## Q2. Why are token IDs not enough for understanding language?
Token IDs are numerical identifiers assigned by the tokenizer. They do not contain semantic meaning or relationships between words.

## Q3. What is a vector?
A vector is an ordered list of numbers. In AI, vectors are used to represent meaning, and the distance between vectors helps show how related two items are.

## Q4. Why are embeddings useful?
Embeddings capture semantic relationships between words, sentences, and documents. They help with semantic search, recommendations, clustering, and RAG.

## Q5. Explain semantic similarity using car, automobile, and banana.
Car and automobile have close vectors, so they are similar in meaning. Banana is far away from them in vector space, so it is not similar.

Sentence
      │
      ▼
Tokenizer
      │
      ▼
Token IDs
      │
      ▼
Embedding Layer
      │
      ▼
Embedding Vectors
Embedding Vectors
        │
        ▼
Cosine Similarity
        │
        ▼
Semantic Search
        │
        ▼
RAG / AI Agents / ChatGPT
