import base64
from io import BytesIO
from PIL import Image


def image_to_base64(pil_image: Image.Image) -> str:
    """
    Convert PIL images to Base64 encoded strings

    :param pil_image: PIL image
    :return: Re-sized Base64 string
    """
    # garante que está em RGB (remove canal alpha/transparência)
    if pil_image.mode == "RGBA":
        pil_image = pil_image.convert("RGB")
        
    buffered = BytesIO()
    pil_image.save(buffered, format="JPEG")  # You can change the format if needed
    img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
    return img_str

