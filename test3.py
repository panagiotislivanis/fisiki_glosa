import openai
from nltk.book import text3
import time
import os
from nltk.tokenize import word_tokenize

# Ορίστε το API κλειδί σας
openai.api_key = "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"

# Ορίστε το μοντέλο που θέλετε να χρησιμοποιήσετε
model_name = "gpt-3.5-turbo"
filename = "text3.txt"

# Ανοίγετε το αρχείο για εγγραφή
# Αντικαταστήστε "book-name" με το όνομα του βιβλίου που θέλετε

# Χωρίστε το κείμενο σε τμήματα των 4090 tokens
# segments = [content[i:i+10] for i in range(0, len(content), 10)]
# print(segments)

words = list(text3)

# Χωρισμός της λίστας λέξεων σε τμήματα ανά 10 λέξεις
segments = [words[i:i+3200] for i in range(0, len(words), 3200)]
final_text = " "
# Εκτύπωση των τμημάτων
for segment in segments:
    input_text = "translate this into greek ' " + " ".join(segment)+"'"
    while True:
        try:
            response = openai.ChatCompletion.create(
                model=model_name,
                messages=[{"role": "user", "content": input_text}]
            )
            break
        except openai.error.RateLimitError as e:
            print("RateLimitError occurred. Retrying after 60 seconds...")
            time.sleep(60)

    translation = response.choices[0].message['content']
    final_text += translation + " "
    time.sleep(2)  # Αναμονή 2 δευτερολέπτων μεταξύ των αιτημάτων
if len(final_text.split()) >= len(words):
    print("Η μετάφραση ολοκληρώθηκε.")
else:
    print("Η μετάφραση διακόπηκε.")

with open("final_text.txt", "w", encoding="utf-8") as file:
    file.write(final_text)
"""
words = word_tokenize()

# Χρησιμοποιήστε τη μέθοδο join για να ενώσετε τις λέξεις πίσω σε κείμενο
joined_text = " ".join(words)

# Χρησιμοποιήστε τον βρόχο for για να διαιρέσετε το κείμενο σε τμήματα ανά 10 λέξεις
segments = [joined_text[i:i+10] for i in range(0, len(joined_text), 10)]

# Εκτύπωση των τμημάτων
for segment in segments:
    print(segment)
    time.sleep(5)
    # input_text = "translate this into greek ".join(segment)
    # print(input_text)
"""
"""
# Μεταφράστε και αποθηκεύστε κάθε τμήμα
for segment in segments:
    print("Μετάφραση τμήματος \n")
    # print
    input_text = "translate this into greek ".join(segments)
    print(input_text)
    time.sleep(1)

    response = openai.ChatCompletion.create(
        model=model_name,
        messages=[{"role": "user", "content": input_text}]
    )
    # Ανάκτηση του μεταφρασμένου κειμένου από την απάντηση του μοντέλου
    translation = response.choices[0].message['content']
    # Αποθήκευση του μεταφρασμένου κειμένου σε ένα αρχείο με κωδικοποίηση UTF-8
    with open(f"translation_{i+1}.txt", "w", encoding="utf-8") as file:
        file.write(translation)
    print(f"Η μετάφραση τμήματος {i+1} ολοκληρώθηκε.")



    """
