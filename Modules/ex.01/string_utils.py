def count_letters(text):
    text_sans_espaces = text.replace(" ","")
    return len(text_sans_espaces)
def reverse_text(text):
    return text[::-1]
if __name__ == "__main__":
    exemple = "Python great"
    print(count_letters(exemple))
    print(reverse_text(exemple))