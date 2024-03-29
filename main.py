def count_words(text):
    return len(text.split())

def make_list_of_dictionaries(dict):
    list = []
    for key in dict:
        list.append({"letter": key, "num": dict[key]})
    return list

def sort_on(dict):
    return dict["num"]

def count_letter_occurences(text):
    dict = {}
    for char in text:
        if char.lower() not in dict:
            dict[char.lower()] = 1
        else:
            dict[char.lower()] += 1

    return dict

def generate_report(text):
    dict = count_letter_occurences(text)
    count = count_words(text)

    print("--- STARTING REPORT FOR FRANKENSTEIN.TXT ---")
    print(f"This book has {count} words in total \n")

    list_of_dicts = make_list_of_dictionaries(dict)
    list_of_dicts.sort(reverse=True, key=sort_on)

    for item in list_of_dicts:
        for letter in item["letter"]:
            if letter.isalpha():
                print(f"The letter '{letter}' is found {dict[letter]} times")
    
    print("\n--- End of report ---")





def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        generate_report(file_contents)


if __name__ == "__main__":
    main()
