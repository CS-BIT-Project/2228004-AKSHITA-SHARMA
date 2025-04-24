from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image

# Load BLIP model and processor
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base", use_fast=True)
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

def generate_image_caption(image_path):
    """Generates a caption for an uploaded image using BLIP."""
    try:
        image = Image.open(image_path).convert("RGB")
        inputs = processor(image, return_tensors="pt")
        caption_ids = model.generate(**inputs)
        caption = processor.decode(caption_ids[0], skip_special_tokens=True)
        return caption
    except Exception as e:
        return f"Error generating caption: {e}"

