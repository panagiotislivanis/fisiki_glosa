from nltk.book import *
import nltk
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

model_name = "facebook/nllb-200-distilled-600M"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
translator = pipeline("translation", model=model, tokenizer=tokenizer,
                      src_lang="eng_Latn", tgt_lang="ell_Grek", max_length=400)


book_text = ' '.join(text3)


sentences = nltk.sent_tokenize(book_text)


with open('translated_book3.txt', 'w', encoding='utf-8') as f:

    for sentence in sentences:

        translation = translator(sentence)[0]['translation_text']
        print(translation)

        f.write(translation + '\n')
