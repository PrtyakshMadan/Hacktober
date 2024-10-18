from transformers import AutoTokenizer,AutoModelForSeq2SeqLM

model_name = "google/flan-t5-base"
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)
print("hello")

f = open("requirements.txt","r")
text = f.read()

print(text)
if text:
    print('text read')
    print(text)
else:
    print("Text cant be read,")
input_ids = tokenizer(text,return_tensors='pt').input_ids
print(f"input ids: {input_ids}")
output = model.generate(input_ids,max_length = 50,min_length = 35)
summary = tokenizer.decode(output[0],skip_special_tokens=True)
print(summary)
