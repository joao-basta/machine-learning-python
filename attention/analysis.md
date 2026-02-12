# Analysis

### Layer 1, Head 3

**Relationship**: This head appears to be a **"Self-Attention"** or **"Identity"** head.

**Description**: In this diagram, there is a very bright, clear diagonal line running from the top-left to the bottom-right. This indicates that each individual token is paying the maximum amount of attention to itself.

**Inference**: This suggests that in the very first layer, BERT is focused on establishing the representation and identity of each individual word before it begins to mix that information with the surrounding context in deeper layers.

* **Sentence 1**: "We turned down a narrow lane and passed through a small [MASK]."
* **Sentence 2**: "The quick brown fox jumps over the lazy [MASK]."

---

### Layer 1, Head 11

**Relationship**: This head appears to be a **"Delimiter"** or **"Special Token"** head.

**Description**: In this diagram, there is a sharp vertical line on the right side of the grid. Almost every token in the sequence is paying its primary attention to the **period (.)** and the **[SEP]** token.

**Inference**: This suggests this head is responsible for identifying the boundaries of the sentence or the end of a thought, rather than analyzing relationships between nouns, verbs, or adjectives.

* **Sentence 1**: "We turned down a narrow lane and passed through a small [MASK]."
* **Sentence 2**: "Artificial intelligence is changing the way we [MASK]."