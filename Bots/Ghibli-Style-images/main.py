import os

l = "sachin.jpg"

import torch
from diffusers import StableDiffusionPipeline

# Load the Stable Diffusion model (You can use a Ghibli fine-tuned model from Hugging Face)
model_id = "runwayml/stable-diffusion-v1-5"

# Use GPU if available
device = "cuda" if torch.cuda.is_available() else "cpu"

# Load pipeline
pipe = StableDiffusionPipeline.from_pretrained(model_id)
pipe.to(device)

# Define the Ghibli-style prompt
prompt = "Sachin tendulkar playing with his cricket bat"

# Generate the image
image = pipe(prompt).images[0]

# Save the image
image.save("ghibli_style_image.png")

# Show the image
image.show()


