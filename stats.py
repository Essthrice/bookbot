def get_book_text(title):
    with open(title) as f:
    
        file_contents = f.read()
        return file_contents

def word_count(text):
    word_list = text.split()
    return len(word_list)

def instance_count(text):
    #create uniform data
    text = text.lower()
    
    intstance_dict = {}
    
    counter = 0
    total_letters = len(text)
    print(f"total letters in text = {total_letters}")
    for letter in text:
        counter += 1
        if letter in intstance_dict:
            intstance_dict[letter] =   intstance_dict[letter] + 1
        else:
            intstance_dict[letter]= 1
        
    print(intstance_dict)
    