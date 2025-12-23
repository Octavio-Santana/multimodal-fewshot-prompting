from langchain_core.messages import HumanMessage, SystemMessage

from multimodal_fewshot_prompting.prompts.system import SYSTEM_PROMPT
from multimodal_fewshot_prompting.prompts.task import TASK_PROMPT


def build_zero_shot_prompt(image_b64: str):
    return [
        SystemMessage(content=SYSTEM_PROMPT),
        HumanMessage(
            content=[
                {
                    "type": "image_url",
                    "image_url": f"data:image/png;base64,{image_b64}",
                },
                {
                    "type": "text",
                    "text": TASK_PROMPT,
                },
            ]
        ),
    ]
