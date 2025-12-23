from multimodal_fewshot_prompting.prompts import get_prompt_builder
from multimodal_fewshot_prompting.vision import image_to_base64
from multimodal_fewshot_prompting.llm.ollama import llm
from multimodal_fewshot_prompting.parsers import speedtest_parser
from PIL import Image



def main(strategy: str):
    image = Image.open('data/validation/speedtest_validation_01.png')
    image_b64 = image_to_base64(image)

    prompt_builder = get_prompt_builder(strategy)

    message = prompt_builder(image_b64)

    response = llm.invoke(message)

    result = speedtest_parser.parse(response.content)

    print('strategy:', strategy)
    print(result)

if __name__ == "__main__":
    print('SpeedTest Result:')
    main("zero-shot")
    print('-----------------------')
    main("few-shot")