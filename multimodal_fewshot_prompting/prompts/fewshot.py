
from pathlib import Path
from typing import List

from langchain_core.messages import HumanMessage, SystemMessage

from multimodal_fewshot_prompting.prompts.system import SYSTEM_PROMPT
from multimodal_fewshot_prompting.prompts.task import TASK_PROMPT
from multimodal_fewshot_prompting.vision.image_loader import image_to_base64
from PIL import Image

# Diretório padrão de imagens few-shot
PROJECT_ROOT = Path(__file__).resolve().parents[2]
FEWSHOT_DIR = PROJECT_ROOT / "data" / "fewshot"

def _load_fewshot_example(
    image_path: Path,
    expected_json: str,
) -> HumanMessage:
    """
    Cria um HumanMessage few-shot a partir de uma imagem + JSON esperado
    """
    pil_image = Image.open(image_path)
    image_b64 = image_to_base64(pil_image)

    return HumanMessage(
        content=[
            {
                "type": "image_url",
                "image_url": f"data:image/png;base64,{image_b64}",
            },
            {
                "type": "text",
                "text": TASK_PROMPT,
            },
            {
                "type": "text",
                "text": expected_json,
            },
        ]
    )

def build_few_shot_examples() -> List[HumanMessage]:
    """
    Retorna a lista de exemplos few-shot multimodais
    """

    examples = []

    examples.append(
        _load_fewshot_example(
            FEWSHOT_DIR / "openspeedtest_01.png",
            '{\n  "download": 232.85,\n  "upload": 86.43,\n  "ping": 241.0\n}',
        )
    )

    examples.append(
        _load_fewshot_example(
            FEWSHOT_DIR / "speedtest_01.png",
            '{\n  "download": 612.22,\n  "upload": 256.78,\n  "ping": 4.0\n}',
        )
    )

    return examples

def build_few_shot_prompt(image_b64: str) -> List:
    """
    Constrói o prompt multimodal completo:
    - System message
    - Few-shot examples
    - Human message final (imagem a ser analisada)
    """

    system_message = SystemMessage(content=SYSTEM_PROMPT)

    fewshot_messages = build_few_shot_examples()

    final_human_message = HumanMessage(
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
    )

    return [
        system_message,
        *fewshot_messages,
        final_human_message,
    ]
