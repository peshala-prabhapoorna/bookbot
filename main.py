def main():
    path = "books/frankenstein.txt"
    file_contents = read_file(path)
    
    # print stats report
    print(f"--- stats report for {path} ---")
    print(f"word count: {count_words(file_contents)}\n")

    # print character count report
    chars_dict = count_chars(file_contents)
    sorted_chars_dict_list = dict_to_sorted_dict_list(chars_dict)
    print("count of characters:")
    for char in sorted_chars_dict_list:
        print(f"{char['char']}: {char['count']}") 
    print("--- end stats report ---")

def read_file(path):
    file_contents = ""
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def count_words(text):
    return len(text.split())

def count_chars(text):
    chars_dict = dict()
    for char in text.lower():
        if char.isalpha():
            if char in chars_dict:
                chars_dict[char] += 1
            else:
                chars_dict[char] = 1
    return chars_dict
            
def dict_to_sorted_dict_list(dictionary):
    def sort_on(dict):
        return dict["count"]

    dict_list = [{"char": char, "count": count} 
                 for (char, count) in iter(dictionary.items())]
    dict_list.sort(key=sort_on, reverse=True)
    return dict_list

main()
