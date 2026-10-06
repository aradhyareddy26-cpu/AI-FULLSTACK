from diffusers import stableDiffusionPipeline
pipe = StableDiffusionPipeline.from_pretrained(
    "runwaym1/stable-diffusion-v1-5"
).to("cpu")
prompt = "Sunset in a futuristic city."
image = pipe(prompt, num_inferenc_steps=8).images[0]
image.show()
