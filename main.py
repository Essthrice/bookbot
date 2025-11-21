from stats import get_book_text, word_count, instance_count, sort_dict, print_report

def main():
    book_path = "books/frankenstein.txt"
    full_text = get_book_text(book_path)
    count = word_count(full_text)
    

    chars = instance_count(full_text)
    sorted_chars = sort_dict(chars)

    print_report(sorted_chars,count,book_path)

main()