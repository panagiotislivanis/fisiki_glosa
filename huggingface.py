from transformers import MarianMTModel, MarianTokenizer

# Define the model and tokenizer, replace 'en-el' with the language pair you're interested in
model_name = 'Helsinki-NLP/opus-mt-en-el'
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)

# Example text
text = 'Hello, how are you?'

# Tokenize the text
tokenized_text = tokenizer.prepare_seq2seq_batch([text], return_tensors='pt')

# Perform the translation and decode the output
translation = model.generate(**tokenized_text)
translated_text = tokenizer.batch_decode(translation, skip_special_tokens=True)

print(translated_text[0])  # This should print the translated text
