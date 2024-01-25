import gradio as gr
import imagehash
from PIL import Image

# Function to compare two images


def compare_images(image1, image2):
    # Convert images to PIL format
    pil_image1 = Image.open(image1)
    pil_image2 = Image.open(image2)

    # Calculate hashes
    hash1 = imagehash.average_hash(pil_image1)
    hash2 = imagehash.average_hash(pil_image2)

    # Compare and return result
    if hash1 - hash2 == 0:
        return "Duplicate Detected"
    else:
        return "No Duplicate Detected"


# Create Gradio interface
iface = gr.Interface(
    fn=compare_images,
    inputs=[gr.Image(type='filepath'), gr.Image(type='filepath')],
    outputs="text",
    title="Image Duplicate Checker",
    description="Upload two images to check if they are duplicates."
)

# Run the app
iface.launch()
