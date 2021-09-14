"""Implementing the helper functions in python."""

import sys
import requests

def curl(url):
    """
        url will be passed as parameter to the wget function
        if given url is valid, function will download the content from url
        downloaded content will be written into file index.html
    """
    try:
        response = requests.get(url)
        return response.text
    except:
        return "curl: unable to resolve host address " + url

def cat(text):
    """
        Implementing the cat command functionality by defining a function
    """
    result = ""
    lines = text.splitlines()
    for i in range(len(lines)):
        result += lines[i] + "\n"
    return result[:-1]

def tac(text):
    """
        Implementing the tac command functionality by defining a function
    """
    result = ""
    lines = text.splitlines()
    for i in range(len(lines)-1, -1, -1):
        result += lines[i] + "\n"
    return result[:-1]

def tail(text, n_lines=10):
    """
        Implementing the tail command functionality by defining a function
    """
    if text:
        lines = text.splitlines()
        lines = lines[-n_lines:]
        return "\n".join(lines)
    return None

def head(text, n_lines=10):
    """
        Implementing the head command functionality by defining a function
    """
    if text:
        lines = text.splitlines()
        lines = lines[:n_lines]
        return "\n".join(lines)
    return None

def wc(text):
    """
        will create a function of wc which takes text(i.e., content of the entire file)
        as a parameter
    """
    word_count = word_counts(text)
    char_count = char_counts(text)
    line_count = line_counts(text)
    byte_count = byte_counts(text)
    return [line_count, word_count, byte_count, char_count]

def word_counts(text):
    """
        returns the count of words a given file
    """
    list_of_words = text.split()
    return len(list_of_words)

def line_counts(text):
    """
        returns the count of lines a given file
    """
    list_of_lines = text.split("\n")
    return len(list_of_lines) - 1

def char_counts(text):
    """
        returns the count of character a given file
    """
    return len(text)

def byte_counts(text):
    """
        returns the count of bytes a given file
    """
    return len(text.encode('utf-8'))


def is_valid_file():
    """
        Check the file validations
    """
    try:
        file = open(sys.argv[-1], "r")
        file.close()
        return True
    except:
        print("cut: "+sys.argv[-1]+": No such file or directory")
        return False

def readfile(filename):
    """
        Reading the contents of a given file
    """
    try:
        file = open(filename)
        text = file.read()
        return text
    except FileNotFoundError:
        print("tail: cannot open", filename, "for reading: No such file or directory")
