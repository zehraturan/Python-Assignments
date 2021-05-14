text = input ("Enter a text: ").strip().lower()

list_text = list(text)
dict_text = dict()

for i in list_text :
  if i in dict_text.keys() :
     dict_text[i] += 1
  else :
    dict_text[i] = 1
print(dict_text)