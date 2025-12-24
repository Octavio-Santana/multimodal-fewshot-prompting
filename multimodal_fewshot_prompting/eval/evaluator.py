import json
from pathlib import Path
from PIL import Image

from multimodal_fewshot_prompting.prompts.factory import get_prompt_builder
from multimodal_fewshot_prompting.vision import image_to_base64
from multimodal_fewshot_prompting.parsers.speedtest import speedtest_parser
from multimodal_fewshot_prompting.llm.ollama import llm


PROJECT_ROOT = Path(__file__).resolve().parents[2]
VALIDATION_DIR = PROJECT_ROOT / "data" / "validation"


def evaluate(strategy: str, tolerance: float = 0.1):
    prompt_builder = get_prompt_builder(strategy)

    labels = json.loads(
        (VALIDATION_DIR / "labels.json").read_text()
    )

    results = []

    for sample in labels:
        image = Image.open(VALIDATION_DIR / sample["image"])
        image_b64 = image_to_base64(image)

        messages = prompt_builder(image_b64)
        response = llm.invoke(messages)

        try:
            prediction = speedtest_parser.parse(response.content)
            success = True
        except Exception:
            prediction = None
            success = False

        results.append({
            "image": sample["image"],
            "parsed": success,
            "prediction": prediction,
            "expected": sample,
        })

    return results
