from nltk.translate.bleu_score import sentence_bleu
from nltk.tokenize import sent_tokenize, word_tokenize
import nltk
nltk.download('punkt')


with open("text3.txt", 'r') as f:
    reference_text = f.read()
with open("2/translated_book3.txt", 'r', encoding='utf-8') as f:
    translation1 = f.read()
with open("3/translated_book3.txt", 'r', encoding='utf-8') as f:
    translation2 = f.read()
with open("Helsinki-NLP/translated_book3.txt", 'r', encoding='utf-8') as f:
    translation3 = f.read()

reference_sentences = sent_tokenize(reference_text)
translation1_sentences = sent_tokenize(translation1)
translation2_sentences = sent_tokenize(translation2)
translation3_sentences = sent_tokenize(translation3)

scores1, scores2, scores3 = [], [], []
for ref_sentence, trans1, trans2, trans3 in zip(reference_sentences, translation1_sentences, translation2_sentences, translation3_sentences):
    ref_words = word_tokenize(ref_sentence)
    candidate1 = word_tokenize(trans1)
    candidate2 = word_tokenize(trans2)
    candidate3 = word_tokenize(trans3)

    score1 = sentence_bleu([ref_words], candidate1)
    score2 = sentence_bleu([ref_words], candidate2)
    score3 = sentence_bleu([ref_words], candidate3)

    scores1.append(score1)
    scores2.append(score2)
    scores3.append(score3)

print("Average BLEU score for translation 1:", sum(scores1) / len(scores1))
print("Average BLEU score for translation 2:", sum(scores2) / len(scores2))
print("Average BLEU score for translation 3:", sum(scores3) / len(scores3))
