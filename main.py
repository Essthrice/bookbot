from stats import get_book_text, word_count, instance_count, sort_dict, print_report
import sys

def main():
    
    if len(sys.argv) != 2 :
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    
    book_path = sys.argv[1]
    full_text = get_book_text(book_path)
    count = word_count(full_text)
    

    chars = instance_count(full_text)
    sorted_chars = sort_dict(chars)

    print_report(sorted_chars,count,book_path)

main()