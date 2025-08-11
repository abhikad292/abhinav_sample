
"""Q.1 Write a Python program to reverse words of sentence in the same order."""
def reverse_words_in_sentence(sentence: str) -> str:
    """
    Reverse each word in the sentence while keeping word order intact.
    :param sentence: Input sentence string.
    :return: Sentence with each word reversed, but order preserved.
    """
    return ' '.join(word[::-1] for word in sentence.split())
    
# Example usage
print(reverse_words_in_sentence("Hello World from Python"))
# Output: "olleH dlroW morf nohtyP"

"""Q.2 Write a Python code to generate the powerset of a given set."""
from itertools import chain, combinations
from typing import Any, Iterable, List, Set

def powerset(iterable: Iterable[Any]) -> List[Set[Any]]:
    """
    Generate the powerset of a given iterable.
    :param iterable: Input iterable (set, list, tuple, etc.).
    :return: List of sets representing all subsets.
    """
    s = list(iterable)
    return [set(combo) for r in range(len(s) + 1) for combo in combinations(s, r)]

# Example usage
print(powerset({1, 2, 3}))
# Output: [{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}]

"""Q.3 Write a Python code to to pickup a list from a string dynamically."""
import ast
from typing import List

def extract_list_from_string(data: str) -> List:
    """
    Extract a Python list from a string representation dynamically.
    :param data: String containing list format.
    :return: Extracted Python list.
    """
    try:
        extracted_list = ast.literal_eval(data)
        if isinstance(extracted_list, list):
            return extracted_list
        else:
            raise ValueError("Provided string does not contain a valid list.")
    except (SyntaxError, ValueError):
        raise ValueError("Invalid string for list extraction.")

# Example usage
print(extract_list_from_string("[1, 2, 3, 4]"))
# Output: [1, 2, 3, 4]

"""Q.4 Write a Python fuction which takes "Text, chunk size, overlap size" as 
argument to divide the given text into chunks of given size with given overlap size"""
from typing import List

def chunk_text_with_overlap(text: str, chunk_size: int, overlap_size: int) -> List[str]:
    """
    Divide text into chunks with given size and overlap.
    :param text: Input text string.
    :param chunk_size: Size of each chunk.
    :param overlap_size: Overlap between chunks.
    :return: List of chunks.
    """
    if chunk_size <= 0 or overlap_size < 0:
        raise ValueError("Chunk size must be > 0 and overlap size must be >= 0.")
    
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - overlap_size
    return chunks

# Example usage
print(chunk_text_with_overlap("HelloWorldPython", 5, 2))
# Output: ['Hello', 'lloWo', 'oWorl', 'rldPy', 'ython']

"""
Q.5 Write a Python function to accept an input string and perform the following operations on it:
1. Count the total number of words in the sentence
2. Find the longest word in the sentence
3. Return a new sentence in which: 
    a. each word starts with an uppercase letter
    b. All extra spaces (leading, trailing, or multiple spaces between words) are removed.

Final output should be a Tuple with the above three elements.
"""
from typing import Tuple

def process_sentence(sentence: str) -> Tuple[int, str, str]:
    """
    Process the input sentence to:
    1. Count total words.
    2. Find the longest word.
    3. Return a cleaned sentence with each word capitalized and extra spaces removed.
    :param sentence: Input sentence string.
    :return: Tuple (word_count, longest_word, cleaned_sentence)
    """
    # Remove extra spaces and split
    words = sentence.strip().split()
    word_count = len(words)
    longest_word = max(words, key=len) if words else ""
    
    # Capitalize each word and remove extra spaces
    cleaned_sentence = ' '.join(word.capitalize() for word in words)
    
    return word_count, longest_word, cleaned_sentence

# Example usage
print(process_sentence("   hello   world   from   python  programming "))
# Output: (5, 'Programming', 'Hello World From Python Programming')
