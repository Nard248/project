from myPythonHelperModule import *


# # Part 1:
# The Message object ## Question 1. Create a class called Message. Create the init function with self and
# text arguments to initialize the Message object. The text argument is a string, and it is the text of the message to
# encrypt. The attributes of the Message object are msg_txt (a string) and accepted_words (a list coming from the
# extract_words function from the helper module.)
class Message:
    def __init__(self, msg_txt, accepted_words=extract_words("words.txt")):
        self.msg_txt = msg_txt
        self.accepted_words = accepted_words

    # Question 2: Create a method called get_message_text with the to access the self.msg_txt outside the class,
    # return a string of the shifted

    def get_message_text(self):
        return self.msg_txt

    # Question 3:
    # Create a method called get_accepted_words to  access a COPY of the list accepted_words outside the class

    def get_accepted_words(self):
        return self.accepted_words

    # Question 4:
    # Create a method called make_shift_dict that takes the shift as an input.
    # This method applies a shift to all the lowercase and uppercase letters and saves the results in a dictionary.
    # Note that shift is an integer and cannot be less than 0 or larger than 26.
    # For example:

    @staticmethod
    def make_shift_dict(shift):
        changed_lc = f'{string.ascii_lowercase[shift:]}{string.ascii_lowercase[:shift]}'
        changed_up = f'{string.ascii_uppercase[shift:]}{string.ascii_uppercase[:shift]}'
        changed = f'{changed_lc}{changed_up}'
        mapped_dictionary = dict(zip(string.ascii_letters, changed))
        return mapped_dictionary

    def apply_shift(self, shift_):
        if 0 < shift_ < 26:
            return_string = ''
            letters = self.make_shift_dict(shift_)
            for char in self.msg_txt:
                if char in letters.keys():
                    return_string = return_string + letters.get(char)
                else:
                    return_string = return_string + char
            return return_string
        else:
            raise IndexError("index out of range (0 to 26)")


'''
a = Message("Hello")
print(a.make_shift_dict(2))

Output: 
{'a': 'c', 'b': 'd', 'c': 'e', 'd': 'f', 'e': 'g', 'f': 'h', 'g': 'i', 
'h': 'j', 'i': 'k', 'j': 'l', 'k': 'm', 'l': 'n', 'm': 'o', 'n': 'p', 
'o': 'q', 'p': 'r', 'q': 's', 'r': 't', 's': 'u', 't': 'v', 'u': 'w', 
'v': 'x', 'w': 'y', 'x': 'z', 'y': 'a', 'z': 'b', 
'A': 'C', 'B': 'D', 'C': 'E', 'D': 'F', 'E': 'G', 'F': 'H', 'G': 'I', 
'H': 'J', 'I': 'K', 'J': 'L', 'K': 'M', 'L': 'N', 'M': 'O', 'N': 'P', 
'O': 'Q', 'P': 'R', 'Q': 'S', 'R': 'T', 'S': 'U', 'T': 'V', 'U': 'W', 
'V': 'X', 'W': 'Y', 'X': 'Z', 'Y': 'A', 'Z': 'B'}

For each alphabet letter saved as a key, it associates its shifted letter based on the shift input you give. If the 
shift was 4, this dictionary would've been {'a': 'e', 'b': 'f', 'c': 'g', 'd': 'h', ...., 'X': 'B', 'Y': 'C', 
'Z': 'D'} etc. 

Hint: In this function, you may use the string module's ascii_lowercase and ascii_uppercase letters.

'''

# Question 5:
'''Create a method called apply_shift that takes the shift integer as an input. Given a Message object or its 
children, this method applies the shift given to it as input to that object and return a string of the encrypted 
final value. Note that shift is an integer and cannot be less than 0 or larger than 26. Example: a = Message("Hello") 
print(a.apply_shift(2)) 

Output: 
"Jgnnq"

Hint: In this function, you may use the output of the make_shift_dict function.
'''

# Part 2: AnyTextMessage Inherited class


# Question 6: 
'''
Create a child class of Message called: AnytextMessage.
In the init function: 
Initialize the AnytextMessage object with a text, which is a string and a shift, which is an integer. 

An AnytextMessage object inherits from the Message class and has five attributes: msg_txt, accepted_words, shift, 
encr_shift_dict [the dictionary of the shifted letters], enc_msg_txt (the final encrypted text saved as a string) '''


class AnyTextMessage(Message):
    def __init__(self, msg_txt, shift):
        super().__init__(msg_txt)
        self.shift = shift
        self.accepted_words = self.get_accepted_words()
        self.encr_shift_dict = self.make_shift_dict(self.shift)
        self.encr_msg_txt = self.apply_shift(self.shift)

    def get_shift(self):
        return self.shift

    def get_encr_dict(self):
        return self.make_shift_dict(self.shift)

    def get_encr_msg(self):
        return self.apply_shift(self.shift)

    def change_shift(self, new_shift):
        shift = new_shift
        self.shift = shift


# Question 7:
'''
Create a function called get_shift that will return the shift given to an AnytextMessage object. 
'''
# Question 8:
'''
Create a function called get_encr_dict that will return a copy of the dictionary of the encrypted letters.
'''
# Question 9: 
'''
Create a function called get_encr_msg that will return the string of the encrypted message. 
'''
# Question 10:
'''
Create a function called change_shift that takes a shift value as an input and changes the shift value of an existing AnytextMessage object. This method returns nothing.
'''


# Part 3:CaesarsDecoder

class Caesarsdecoder(Message):
    def __init__(self, msg_txt):
        super().__init__(msg_txt)
        self.msg_txt = msg_txt
        self.accepted_words = self.get_accepted_words()

    # noinspection PyGlobalUndefined
    @property
    def decrypt_message(self):
        global final_text, index
        text = self.msg_txt
        match_count = 0
        for i in range(1, 26):
            temp_count = 0
            decrypted_text = self.apply_shift(i)
            for word in decrypted_text:
                if word in self.accepted_words:
                    temp_count += 1
            if temp_count >= match_count:
                match_count = temp_count
                index = i
                final_text = decrypted_text
        list_ = [index, final_text]
        return tuple(list_)


# Question 11
'''
Create a child class of Message called CaesarsDecoder. 
In the init function, initialize a CaesarsDecoder object with text which is a string. 
Let msg_txt and accepted words be the attributes of this class. 
'''

# Question 12: 
'''
Create a method called decrypt_message.
In this method, decrypt the msg_txt by trying every possible shift value 
and find the "best" one. 
We will define "best" as the shift that creates the maximum number of real words when we use apply_shift(shift) on the message text. 
If s is the original shift value used to encrypt the message, then we would expect 26 - s to be the best shift value for decrypting it.
This method returns a tuple of the best shift value used to decrypt the message and the decrypted message text using that shift value
'''

sec_story = get_story_text()
final = Caesarsdecoder(sec_story)
print(final.decrypt_message)
