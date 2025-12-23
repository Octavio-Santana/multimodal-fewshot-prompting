from multimodal_fewshot_prompting.prompts.zeroshot import build_zero_shot_prompt
from multimodal_fewshot_prompting.prompts.fewshot import build_few_shot_prompt


def get_prompt_builder(strategy: str):
    strategies = {
        "zero-shot": build_zero_shot_prompt,
        "few-shot": build_few_shot_prompt,
    }

    if strategy not in strategies:
        raise ValueError(
            f"Invalid strategy '{strategy}'. "
            f"Use one of: {list(strategies.keys())}"
        )

    return strategies[strategy]
