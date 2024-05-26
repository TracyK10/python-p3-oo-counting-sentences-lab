#!/usr/bin/env python3

class MyString:
  def __init__(self, value=''):
    self.value = value
    
  @property
  def value(self):
    return self._value
  
  @value.setter
  def value(self, word):
    if(type(word) == str):
      self._value = word
    else:
      print("The value must be a string.")
  
  def is_sentence(self):
    return self._value.endswith(".")
    
  def is_question(self):
    return self._value.endswith("?")
  
  def is_exclamation(self):
    return self._value.endswith("!")
    
  def count_sentences(self):
    # count = 0
    # for char in self._value:
    #   if char == "." or char == "?" or char == "!":
    #     count += 1
    # return count
    value = self._value
    for punctuation in ['!', "?", '.']:
      value = value.replace(punctuation, '.')
    sentences = filter(None, value.split('.'))
    return len(list(sentences))

#examples
string = MyString()
string.value = "This is a string! It has three sentences. Right?"
print(string.count_sentences())