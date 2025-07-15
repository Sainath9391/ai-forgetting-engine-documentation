# AI-Powered Forgetting Engine

The AI-Powered Forgetting Engine is an experimental system designed to make AI memory behave more like human memory.
Instead of just adding new data forever, it applies memory decay, emotional salience, and selective retention to forget information that is no longer important.

This keeps AI models lighter, more efficient, and sometimes even a bit imperfect in a human-like way.

---

## Table of Contents

* About the Project
* Why this Project Matters
* Real-world Use Cases
* Tech Stack
* Key Features
* Architecture & Data Flow
* Technical Overview
* Implementation & Code Explanation
* Example Output
* How it all Connects
* Future Improvements & Research Directions
* Business & Research Impact
* Installation
* Usage
* Contributing
* License

---

## About the Project

Traditional AI systems keep accumulating data, which can lead to outdated or irrelevant knowledge.
This project explores the idea of AI that can also forget by:

* Applying memory decay over time
* Using emotional salience so important memories decay slower
* Simulating imperfect recall

The goal is to bring AI memory closer to how people actually remember and forget.

---

## Why this Project Matters

* Avoids overfitting on old or low-value data
* Keeps AI models dynamic and more lightweight
* Produces more human-like and natural responses
* Adds an ethical angle by actively forgetting personal data

---

## Real-world Use Cases

* Chatbots that forget old conversations naturally
* Virtual assistants that remove outdated reminders
* Storytelling tools where characters misremember events
* Simulations for studying memory disorders
* Privacy-aware systems that decay private data over time

---

## Tech Stack

* Python
* Simple database or key-value store (SQLite or Redis)
* Exponential decay algorithms
* Optional vector databases (FAISS) for efficient retrieval

---

## Key Features

* Automatic memory decay based on time
* Emotional salience to protect important memories
* Keeps only top-k most relevant data
* Imperfect recall to simulate human-like errors
* Modular and easy to customize

---

## Architecture & Data Flow

New data → feature extraction → scoring → forgetting engine → memory store → probabilistic recall → AI output

---

## Technical Overview

| Component       | Purpose                                       |
| --------------- | --------------------------------------------- |
| Encoder         | Scores importance and extracts features       |
| Forgetting core | Applies decay and filters low-importance data |
| Memory store    | Holds the evolving set of memories            |
| Retriever       | Recalls data, sometimes imperfectly           |
| Output          | Used by chatbots, stories, or analytics       |

---

## Implementation & Code Explanation

* `src/decay.py`: Implements the exponential decay function:

  ```python
  import math
  def decay(salience, age, rate=0.01):
      return salience * math.exp(-rate * age)
  ```
* `src/memory.py`: Defines the Memory class with content, salience, and timestamp
* `examples/sample_run.py`: Demonstrates adding, decaying, and recalling memories
* Emotional scoring slows decay for higher importance data
* Probabilistic recall adds occasional imperfection

---

## Example Output

Stored: “Met John at the conference.”

* After some days, salience drops from 0.9 to around 0.4
* Recall might return: “Met someone at a meeting, talked about tech.”

---

## How it all Connects

1. Data is scored by the encoder
2. Forgetting engine applies decay over time
3. Memory store keeps only the most relevant data
4. Retriever fetches memories, sometimes slightly distorted
5. AI application uses these for answers or generation

---

## Future Improvements & Research Directions

* Link related memories as a graph
* Adjustable forgetting rate controlled by user
* Large language model integration
* Visualize what is remembered vs forgotten
* Test fairness and bias in forgetting

---

## Business & Research Impact

* Helps AI systems feel more natural and relatable
* Reduces storage and model bloat
* Supports privacy by design
* Can be used in mental health research, education, and storytelling

---

## Installation

```bash
git clone https://github.com/yourusername/ai-forgetting-engine.git
cd ai-forgetting-engine
pip install -r requirements.txt
```

---

## Usage

```bash
python examples/sample_run.py
```

---

## Contributing

Fork the repository, create a new branch, commit your changes, and open a pull request.

---

## License

MIT License

A system that doesn’t just learn — it forgets, too.
