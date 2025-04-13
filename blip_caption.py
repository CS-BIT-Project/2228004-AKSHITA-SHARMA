from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image

processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

def generate_image_caption(image_path):
    try:
        image = Image.open(image_path).convert("RGB")
        inputs = processor(images=image, return_tensors="pt")
        outputs = model.generate(**inputs, max_length=50, num_beams=5)
        caption = processor.decode(outputs[0], skip_special_tokens=True)
        return caption
    except Exception as e:
        print(f"Error generating caption: {e}")
        return ""

    # # Spotify credentials
    # SPOTIFY_CLIENT_ID = "d48f514a873145dd8059b91b21e71651"
    # SPOTIFY_CLIENT_SECRET = "6fc3e06d70b04c44ab6f896bb7109aa8"
