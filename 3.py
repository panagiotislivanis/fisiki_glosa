from nltk.book import *
import nltk
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

# Επιλέξτε το μοντέλο μετάφρασης αγγλικών-ελληνικών
model_name = "facebook/nllb-200-distilled-600M"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
translator = pipeline("translation", model=model, tokenizer=tokenizer,
                      src_lang="eng_Latn", tgt_lang="ell_Grek", max_length=400)

# Χρησιμοποιήστε το τρίτο βιβλίο από τη βιβλιοθήκη nltk
book_text = ' '.join(text3)

# Διαχωρίστε το κείμενο σε προτάσεις
sentences = nltk.sent_tokenize(book_text)

# Ανοίξτε ένα αρχείο .txt για να αποθηκεύσετε τη μετάφραση
with open('translated_book3.txt', 'w', encoding='utf-8') as f:
    # Μεταφράστε κάθε πρόταση του βιβλίου
    for sentence in sentences:
        # Εκτέλεση της μετάφρασης
        translation = translator(sentence)[0]['translation_text']
        print(translation)
        # Αποθηκεύστε τη μετάφραση στο αρχείο .txt
        f.write(translation + '\n')
