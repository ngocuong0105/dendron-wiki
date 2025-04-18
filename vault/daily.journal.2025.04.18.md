---
id: jgo06popz81qnmpz10ilpld
title: '2025-04-18'
desc: ''
updated: 1745000603916
created: 1744999959816
traitIds:
  - journalNote
---

#  Chain of Thought

[o1 release](https://openai.com/index/learning-to-reason-with-llms/)


- Essentially the model has been trained on how to think and it goes through an explicit reasoning process before giving its final answer.
- The tradeoff being made is:
- Vastly improved problem solving capabilities for queries where there are verifiably correct answers.
- 100x or more slower than non-reasoning models since the LLM is producing all those internal reasoning tokens.  A “fast” query with a reasoning model is 10s before you get any output.  A slow query is minutes.
- 5x more expensive than non-reasoning models.
- This tradeoff is tunable.  The longer you let the model reason, the more capable it is.
- **Important** The reasoning models do NOT improve the capabilities for subjective tasks.  OpenAI even observed that people tend to prefer the text of gpt-4o vs o1.  The improved capabilities are just for when there are verifiably correct answers.