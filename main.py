from stats import get_book_text, word_count, instance_count

def main():
    full_text = get_book_text("books/frankenstein.txt")
    count = word_count(full_text)
    
    print(f"Found {count} total words")

    instance_count(full_text)
main()