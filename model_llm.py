from transformers import AutoTokenizer
from transformers import AutoModelForSeq2SeqLM
import torch
import nltk
from nltk.stem import WordNetLemmatizer


def lemmatize_text(text):
        lemmatizer = WordNetLemmatizer()
        words = nltk.word_tokenize(text)
        lemmatized_words = [lemmatizer.lemmatize(word) for word in words]
        return ' '.join(lemmatized_words)



def lemmatize_transcription_file(transcription_file, output_file):
    with open(transcription_file, "r") as f:
         text = f.read()

        
    lemmatized_text = lemmatize_text(text)

    with open(output_file, "w") as f:
        f.write(lemmatized_text)
    return output_file

def genrate_summary(lemmatize_file):
    model_name = "google/flan-t5-small"

    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    max_input_tokens =512
    overlap = 50

    f = open(lemmatize_file,"r")
    text = f.read()
    text = text + "  Genrate Summary of this : "
    tokenized = tokenizer(text,return_tensors='pt',truncation=True,max_length=512)

    input_ids = tokenized['input_ids'][0]
    num_of_chunks = len(input_ids)//max_input_tokens + 1

    chunks = [input_ids[i:i+max_input_tokens] for i in range(0,len(input_ids),max_input_tokens - overlap)]
    summaries = []
    for chunk in chunks:
        chunk_tensor = chunk.unsqueeze(0)
        output =model.generate(chunk_tensor,max_length = 100,min_length = 25)
        summary = tokenizer.decode(output[0], skip_special_tokens=True)
        summaries.append(summary)
    final_summary = " ".join(summaries)
    final_tokenized = tokenizer(final_summary, return_tensors='pt', truncation=True, max_length=max_input_tokens)
    final_output = model.generate(final_tokenized['input_ids'], max_length=100, min_length=30)
    final_summary = tokenizer.decode(final_output[0], skip_special_tokens=True)
    return final_summary

if __name__ == "__main__":
    transcription_file = "transcription.txt" 
    lemmatized_file = "lemmatized_transcription.txt"
    lemmatize_transcription_file(transcription_file,lemmatized_file)
    summary = genrate_summary(lemmatized_file)
    open(lemmatized_file, "w").close()
    print(summary) 









