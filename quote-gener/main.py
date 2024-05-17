import random

quotes = [
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Strive not to be a success, but rather to be of value. - Albert Einstein",
    "The mind is everything. What you think you become. - Buddha",
    "The best and most beautiful things in the world cannot be seen or even touched - they must be felt with the heart. - Helen Keller",
    "Believe you can and you're halfway there. - Theodore Roosevelt",
]

def generate_quote():
    random_index = random.randint(0, len(quotes) - 1)
    return quotes[random_index]

quote = generate_quote()
print(quote)