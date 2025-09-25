from transformers import pipeline

def get_t5_generator():
    return pipeline("text2text-generation", model="t5-base")

generator = get_t5_generator()

def generate_caption(product_name):
    prompt = f"Write a catchy Instagram caption for a product called '{product_name}'"
    result = generator(prompt, max_length=50)
    return result[0]['generated_text']
