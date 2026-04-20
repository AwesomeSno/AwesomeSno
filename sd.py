from diffusers import StableDiffusionPipeline
import torch

# Load the Stable Diffusion pipeline
print("Loading model...")
pipe = StableDiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-2-1-base")
pipe.to("cuda" if torch.cuda.is_available() else "cpu")

# Define your prompt
prompt = "A whimsical jester in a dramatic pose, wearing colorful traditional jester attire with bells. High detail, studio lighting, ultra-realistic."

# Generate an image
print("Generating image...")
image = pipe(prompt, num_inference_steps=50, guidance_scale=7.5).images[0]

# Save the image
output_path = "jester_image.png"
image.save(output_path)
print(f"Image saved at {output_path}")
