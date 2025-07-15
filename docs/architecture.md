# 🏗 Architecture

## Overview
- Memory Encoder: extracts features & computes salience
- Forgetting Engine Core: applies decay & selective retention
- Memory Store: stores dynamic memory data
- Memory Retriever: probabilistically recalls memories
- Output Layer: chatbot / storytelling / personal assistant

## Flow
1. New data → Encoder
2. Apply decay & filter
3. Store in DB
4. Retrieve when queried
