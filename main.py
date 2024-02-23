import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from collections import defaultdict
from heapq import nlargest

def create_frequency_table(text):
    stopWords = set(stopwords.words("english"))
    words = word_tokenize(text.lower())
    freqTable = defaultdict(int)

    for word in words:
        if word not in stopWords:
            freqTable[word] += 1

    return freqTable

def score_sentences(sentences, freqTable):
    sentenceValue = defaultdict(float)

    for sentence in sentences:
        for word, freq in freqTable.items():
            if word in sentence.lower():
                sentenceValue[sentence] += freq

    return sentenceValue

def summarize(text, num_sentences):
    sentences = sent_tokenize(text)
    freqTable = create_frequency_table(text)
    sentence_scores = score_sentences(sentences, freqTable)
    summarized_sentences = nlargest(num_sentences, sentence_scores, key=sentence_scores.get)
    summary = ' '.join(summarized_sentences)
    return summary

if __name__ == "__main__":
    file_path =  input("Enter the path to the text file: ")
    with open(file_path, 'r') as file:
        text = file.read()
    
    num_sentences = 1000# Change this to the number of sentences you want in the summary
    summary = summarize(text, num_sentences)
    print("Summary:")
    print(summary)


    output_file_path = input("Enter the path to save the summary text file: ")
    with open(output_file_path, 'w') as output_file:
        output_file.write(summary)
    print("Summary saved to:", output_file_path)
