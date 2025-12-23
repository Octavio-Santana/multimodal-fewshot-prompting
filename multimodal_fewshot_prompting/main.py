from multimodal_fewshot_prompting.prompts import build_prompt
from multimodal_fewshot_prompting.vision import image_to_base64
from multimodal_fewshot_prompting.llm.ollama import llm
from PIL import Image

image = Image.open('data/validation/speedtest_validation_01.png')
image_b64 = image_to_base64(image)

message = build_prompt(image_b64)

response = llm.invoke(message)
print(response)