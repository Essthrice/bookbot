def get_book_text(title):
    with open(title) as f:
    
        file_contents = f.read()
        return file_contents

def word_count(text):
    word_list = text.split()
    return len(word_list)

def instance_count(text):
    #create uniform data
    text = text.strip()
    text = text.lower()
    text = text.replace(" ", "")
    

    intstance_dict = {}
    
    counter = 0
    for letter in text:
        counter += 1
        if letter in intstance_dict:
            intstance_dict[letter] =   intstance_dict[letter] + 1
        else:
            intstance_dict[letter]= 1
        
    return intstance_dict


def sort_on(item):
    return item["num"]

def sort_dict(dict):
    list_of_chars = []
    
    
    for key, value in dict.items():
        temp_dict1 = {}
        temp_dict1["char"] = key
        temp_dict1["num"] = value
        list_of_chars.append(temp_dict1)
    

    list_of_chars.sort(reverse = True, key=sort_on)

    return list_of_chars




def print_report(text,word_count,book):

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at{book}" )
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for list in text:

        char = list['char']
        num = list['num']
        if  char.isalpha():          
            print(f"{char}: {num}")

    print("============= END ===============")
        