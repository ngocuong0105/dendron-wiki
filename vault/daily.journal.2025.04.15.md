---
id: vh4nk7anolei6ph11tgtgam
title: '2025-04-15'
desc: ''
updated: 1744836760355
created: 1744712302323
traitIds:
  - journalNote
---
# AI Industry Developments

#AI

- Most LLMs are really just a fancy autocomplete. Given a set of words (tokens) 
they are able to predict what the next word most likely is. They use billion of parameters to do this.
- In 2022 LLM practitioners, realized that if they ask the LLM to show its thought process, and use it as prompts, LLMs
can do much better in reasoning tasks **chain of thought prompting**.
- Open AI o1 wrapped this idea into a model and this model showed much better reasoning capabilities. **chain of thoughts (CoTs)**.
This new “reasoning model” goes through extensive internal reasoning in order to decompose problems, brainstorm ideas, check its work, iterate, etc.  Think of it like an internal monologue.
- [**IMPORTANT**] Reasoning models are best when we have verifiable tasks. That is why they are good for coding since we can verify if a code is correct by writing tests.
- One day LLMs reasoning models will be good at solving math problems too. Solutions are currently verifiable only by human, but once we are able to automate this process then models trained with chain of thoughts idea + self-verification will be able to solve hard math problems.

## Reasoning Models

As of today best reasoning models are o3 (OpenAI), Sonnet 3.7 (Anthropic backed by Amazon)

Deep Research 

Operators, Computer-Using Agent. This is fucking awesome. It opens the browser and starts looking at the screen, moves the mouse and clicks...

AI Agent, Assistant, Bot

- Agents perform complex operations, can reason on their own, and proactively make decisions. It has a "self" and is able to "think". Examples: Operators and Deep Research Products
- Assistants assist human when working on tasks. Best example is the vanilla chatGPT, VsCode Co-pilot
- Bot perform simple repetitive tasks, web scrappers, autocomplete, dial-call operators, classic call center support automation


[o1 release, CoT](https://openai.com/index/learning-to-reason-with-llms/)


