from nltk.book import *
from transformers import MarianMTModel, MarianTokenizer
import nltk
nltk.download('book')


model_name = 'Helsinki-NLP/opus-mt-en-el'
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)


book_text = ' '.join(text3)

sentences = book_text.split('.')

with open('translated_book3.txt', 'w', encoding='utf-8') as f:

    for sentence in sentences:

        tokens = tokenizer(sentence, return_tensors='pt')

        translation_tokens = model.generate(**tokens)

        translation = tokenizer.decode(
            translation_tokens[0], skip_special_tokens=True)

        f.write(translation + '\n')
