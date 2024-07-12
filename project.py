# Percy Ratheko

from data import countries_and_capitals, countries, capitals, countries_capitals_dictionary
import re


def write_countries_capitals_to_file(filename):
    """
    This function takes one parameter: a filename. The filename is first validated by using a regular expression. Valid
    filenames must follow these rules: Must contain only letters or digits.
    Must be of length 1-8 characters, plus a “.txt” file extension. For example,these are all valid filenames
    a.txt
    5x.txt
    AbcE123z.txt
    If the filename is not valid, prompt the user for another filename inside the function. This process must continue
    over and over until the user enters a valid filename. Use a regular expression to validate the filename.

    Once the user has entered a valid filename, open the file for writing only, and process
    the countries_capitals_dictionary variable. Use a for/in loop to process the dictionary (for country, capital in
    countries_capitals_dictionary.items():) We will use it to write that data in the following format, to the file
    named by the user

    :param filename: user's filename
    """
    while not re.search("^[a-zA-Z0-9]{1,8}\.txt$", filename):
        filename = input("Enter a valid filename(Must be of length 1-8 characters, plus a “.txt” file extension)")
        # user will be prompted over and over again till they enter a valid filename.

    with open(filename, "w") as file:  # "w" will over-write any previous filenames.
        for country, capital in countries_capitals_dictionary.items():
            file.write(f"The capital of {country} is {capital}.\n")  # this f string would be printed on a new line.


# write_countries_capitals_to_file("bonnnnnnuuuuuuuuuuuu.txt") : for testing purposes, before calling at main script.

def save_capitals():
    """
    This function opens files for writing only. Uses regular expressions to find all the capital cities that meet the
    following patterns, and writes them to the files with the following names. Closes each file when it’s finished.
    """
    with open("vowel_vowel_vowel.txt", "w") as file:  # file for capital cities which contain three consecutive vowels
        for capital in capitals:
            if re.search("[aeiou]{3}", capital, re.IGNORECASE):
                file.write(capital + "\n")

    with open("cons_cons_cons.txt", "w") as file:  # the file for capitals which contain three consecutive consonants
        for capital in capitals:
            if re.search("[b-df-hj-np-tv-z]{3}", capital, re.IGNORECASE):
                file.write(capital + "\n")

    with open("i_before_e.txt", "w") as file:  # the file for capitals which contain i somewhere before e. E.g :Ireland
        for capital in capitals:
            if re.search("(ie)|i[a-z ,]{1,20}e", capital, re.IGNORECASE):
                file.write(capital + "\n")

    with open("a_a.txt", "w") as file:  # the file for capitals which Start with a, and end with a
        for capital in capitals:  # ^a[a-z ,]a$ didn't write anything to file had to at least specify num of characters.
            if re.search("^a[a-z ,]{1,20}a$", capital, re.IGNORECASE):
                file.write(capital + "\n")

    with open("end_with_vowel.txt", "w") as file:  # the file for capitals that End with a vowel
        for capital in capitals:
            if re.search("[aeiou]$", capital, re.IGNORECASE):
                file.write(capital + "\n")

    with open("weird.txt", "w") as file:  # Contains apostrophe, space, or x
        for capital in capitals:
            if re.search("[' x]", capital, re.IGNORECASE):
                file.write(capital + "\n")

    with open("not_start.txt", "w") as file:  # Does not start with a-e, l-p, or s
        for capital in capitals:  # our regex will instead look for capitals which start with the remaining letters.
            if re.search("^[f-kq-rt-z]", capital, re.IGNORECASE):
                file.write(capital + "\n")


# save_capitals() : for testing purposes , before calling it at the main script







