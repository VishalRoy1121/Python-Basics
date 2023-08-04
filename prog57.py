# WAP to create a class to reverse a string, word by word

class ReverseWords:
    def __init__(self, sentence):
        self.sentence = sentence

    def reverse(self):
        words = self.sentence.split()
        words = words[::-1]
        rev_sentence = " ".join(words)

        return rev_sentence


sentence = "Hello World"
rw = ReverseWords(sentence)
rev_sentence = rw.reverse()
print(rev_sentence)
