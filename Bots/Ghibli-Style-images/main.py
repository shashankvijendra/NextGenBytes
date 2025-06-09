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
prompt = "A handsome man with wavy black hair, expressive deep brown eyes, and a well-groomed mustache. He is wearing a classic black suit with a white shirt and striped tie, exuding a vintage charm. The background is softly blurred, with a dramatic lighting effect highlighting his facial features. He holds a single red rose delicately in his hand, conveying a romantic and elegant aura."

# Generate the image
image = pipe(prompt).images[0]

# Save the image
image.save("ghibli_style_image.png")

# Show the image
image.show()


