from nltk.book import *
from transformers import MarianMTModel, MarianTokenizer
import nltk
nltk.download('book')

# Select the translation model from English to Greek
model_name = 'facebook/nllb-200-3.3B'
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)

# Use the third book from nltk
book_text = ' '.join(text3)

# Split the text into sentences
sentences = book_text.split('.')

# Open a .txt file to save the translation
with open('translated_book3.txt', 'w', encoding='utf-8') as f:
    # Translate each sentence of the book
    for sentence in sentences:
        # Tokenization
        tokens = tokenizer(sentence, return_tensors='pt')

        # Perform the translation
        translation_tokens = model.generate(**tokens)

        # Decode the tokens to get the text
        translation = tokenizer.decode(
            translation_tokens[0], skip_special_tokens=True)

        # Save the translation to the .txt file
        f.write(translation + '\n')
