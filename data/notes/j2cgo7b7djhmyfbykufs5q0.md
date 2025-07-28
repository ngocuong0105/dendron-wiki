
Here I put all my thoughts, my resarch, things I've learned and read about LLMs.

# Resources
- [Dario Modei Blog](https://darioamodei.com/)
- 

# Models
LLM models so far are decrtibed as reasoning and models that are good for creative tasks and agentic planning.

- DeepSeek-R1 chinese AI lab DeepSeek reasoning model
- 

# OpenAI
- gpt models, flagship models for OpenAI
- o-series reasoning modeils

#TODO https://platform.openai.com/docs/models#models-overview



# DeepSeek

## R1

- [R1 HuggingFace model](https://huggingface.co/deepseek-ai/DeepSeek-R1)

reasoning model with 671 billion parameters. Under MIT License.

#TODO https://huggingface.co/deepseek-ai/DeepSeek-R1

# Prompt engineering

#TODO https://platform.openai.com/docs/guides/prompt-engineering

# Dario Amodei

[https://darioamodei.com](https://darioamodei.com)

# Three Dynamics of AI Development

1. Scaling laws
- $1M model might solve 20% of important coding tasks
- $10M model might solve 40%
- $100M model might solve 60% and so on

Another factor of 10 might be the differene between an undergraduate and PhD skill level.

2. Shifting the curve
- improvement on model architecture (tweaks ontransforers that the the underlying of today's models)
- engineering improvements, finding a way to run the model more efficiently on the underlying hardware
- CM = "compute multiplier". Frontier AI companies are able to find those compute multiplers

3. Shifting the paradigm
- From 2020-2023 the main thing being scaled was pretrained models
- In 2024 the idea of using reinforecement learning to train models to generate chains of thought has become the new focus of scaling
- new paradigm involves starting with the ordinary type of pretrained models, and then as a second stage using RL to add the reasoning skills
- as of 2025 we are at a unique "crossover point" where thre is a powerful new paradigm that is early on the scaling curve and threfore can make big gains quickly.


- [read section after DeepSeek's Models](https://darioamodei.com/on-deepseek-and-export-controls)

# Industry impact

The "developer loop" might change substantially.  I.e., today if you're doing a large task you might do something like:
1. Work with your PM to figure out what they want
2. Write some code
3. Iterate with PM that you've built the thing they want
4. Iterate on a WIP PR with your technical stakeholders
5. Write some tests
6. Do more iteration on PR

Where in the future/soon/now it might be more like
1. Work with PM (and maybe the AI) to figure out what they want
2. Work with AI and your technical stakeholders to translate that PM plan to create a technical plan
3. Have AI implement a large fraction of the technical plan via chaos coding
4. Do some cleanup on the PR

# P(doom)

median 5% , 14.4% average from AI CEOs and researchers responses.
