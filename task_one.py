import re
from typing import Dict, List, Any


class ParagraphHandler:
    @staticmethod
    def get_string_without_punctuation(paragraph: str) -> str:
        """Function returns string without punctuation. Function uses regex expresion."""
        return re.sub(r"[^\w\s]", "", paragraph)

    @staticmethod
    def get_list_of_words_from_sentence(sentence: str) -> List[str]:
        """Function returns list filled with strings."""
        return sentence.split(" ")

    @staticmethod
    def get_list_of_sentences(paragraph: str) -> List[str]:
        "Function returns sentences placed in list. Paragraph is splitted after every dot and whitespaces are removed after last dot."
        return paragraph.strip(".").split(".")

    @staticmethod
    def get_word_list_with_lowered_letters(paragraph: str) -> List[str]:
        """Function returns list of strings with all letters lowered."""
        return [word.lower() for word in paragraph.split(" ")]

    @staticmethod
    def get_unique_words_count(words_list: List[str]) -> Dict[str, int]:
        """Function returns dictionary with calculated unique word count. To count it correctly you should provide list filled with lower letters only."""
        unique_words_count = {}
        for word in words_list:
            if word not in unique_words_count:
                unique_words_count[word] = 1
            else:
                unique_words_count[word] += 1
        return unique_words_count

    @staticmethod
    def get_three_most_used_words(unique_words_count: Dict[str, int]) -> List[str]:
        """Function prints out the top 3 most used words. Provided dictionary format should be: {str : int}."""
        most_used_words = []
        first_max_key = max(unique_words_count, key=unique_words_count.get)
        most_used_words.append(first_max_key)
        del unique_words_count[first_max_key]
        secound_max_key = max(unique_words_count, key=unique_words_count.get)
        most_used_words.append(secound_max_key)
        del unique_words_count[secound_max_key]
        third_max_value = max(unique_words_count, key=unique_words_count.get)
        most_used_words.append(third_max_value)
        return most_used_words

    @staticmethod
    def get_string_from_list(words_list: List[str]) -> str:
        """Function returns string expresion after getting list of strings."""
        sentence = ""
        for word in words_list:
            sentence += word
        return sentence

    @staticmethod
    def get_calculated_word_count_and_sentence(
        sentences_list: List[str],
    ) -> Dict[str, Any]:
        """Function returns dictionary with all counted words in each sentence and the sentence itself."""
        sentences_information: Dict[str, Any] = {}
        counter = 0
        for sentence in sentences_list:
            modified_sentence = sentence.strip().split(" ")
            sentence_lenght = len(modified_sentence)
            counter += 1
            sentence_in_str = paragraph_handler.get_string_from_list(sentence)
            sentences_information[f"sentence_{str(counter)}"] = {
                "sentence": f"{sentence_in_str}",
                "lenght_in_words": sentence_lenght,
            }
        return sentences_information

    @staticmethod
    def get_shortest_sentence_and_words_count(
        dict_information: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Function prints out the shortest sentence and count of words in the shortest sentence."""
        shortest_sentence_and_words_count = {}
        min_words_count: int = min(
            (count["lenght_in_words"] for count in dict_information.values())
        )
        shortest_sentence_and_words_count["lenght_in_words"] = min_words_count
        for value in dict_information.values():
            if value["lenght_in_words"] == min_words_count:
                shortest_sentence_and_words_count["sentence"] = value["sentence"]
        return shortest_sentence_and_words_count
        


    @staticmethod
    def get_word_with_every_secound_letter_capitalized(word: str) -> str:
        letters_in_word = []
        upper_letter = True
        for letter in word:
            letters_in_word.append(letter.upper() if upper_letter else letter.lower())
            upper_letter = not upper_letter
        return "".join(letters_in_word)

    @staticmethod
    def get_paragraph_with_every_secound_letter_captalized(paragraph: str) -> str:
        words_list = paragraph_handler.get_word_list_with_lowered_letters(paragraph)
        converted_paragraph = ""
        for word in words_list:
            converted_paragraph += (
                paragraph_handler.get_word_with_every_secound_letter_capitalized(word)
                + " "
            )
        return converted_paragraph

    @staticmethod
    def get_reversed_paragraph(paragraph: str) -> str:
        sentences_list = paragraph_handler.get_list_of_sentences(paragraph)
        reversed_paragraph_list = []
        for sentence in sentences_list:
            striped_sentence = sentence.strip()
            reversed_sentence = paragraph_handler.get_list_of_words_from_sentence(
                striped_sentence
            )
            reversed_sentence.reverse()
            reversed_paragraph_list.append(reversed_sentence)
        reversed_paragraph = ""
        for sentence in reversed_paragraph_list:
            sentence += "."
            for word in sentence:
                if word != ".":
                    reversed_paragraph += word + " "
                else:
                    reversed_paragraph += word
        final_paragraph_version = reversed_paragraph.replace(" .", ". ")
        return final_paragraph_version


if __name__ == "__main__":
    paragraph_handler = ParagraphHandler()
    string_without_punctuation = paragraph_handler.get_string_without_punctuation(
        "The European languages are members of the same family. Their separate existence is a myth. For science, music, sport, etc, Europe uses the same vocabulary. The languages only differ in their grammar, their pronunciation and their most common words. Everyone realizes why a new common language would be desirable: one could refuse to pay expensive translators. To achieve this, it would be necessary to have uniform grammar, pronunciation and more common words. If several languages coalesce, the grammar of the resulting language is more simple and regular than that of the individual languages. The new common language will be more simple and regular than the existing European languages. It will be as simple as Occidental; in fact, it will be Occidental. To an English person, it will seem like simplified English, as a skeptical Cambridge friend of mine told me what Occidental is."
    )
    list_of_strings_in_lower = paragraph_handler.get_word_list_with_lowered_letters(
        string_without_punctuation
    )
    words_counter = paragraph_handler.get_unique_words_count(list_of_strings_in_lower)
    print(
        f"Here are listed all words with it count in paragraph:\n {words_counter}\n"
    )
    print("The top three most used words are:")
    words_list = paragraph_handler.get_three_most_used_words(words_counter)
    for word in words_list:
        print(word)
    list_of_strings = paragraph_handler.get_list_of_sentences("The European languages are members of the same family. Their separate existence is a myth. For science, music, sport, etc, Europe uses the same vocabulary. The languages only differ in their grammar, their pronunciation and their most common words. Everyone realizes why a new common language would be desirable: one could refuse to pay expensive translators. To achieve this, it would be necessary to have uniform grammar, pronunciation and more common words. If several languages coalesce, the grammar of the resulting language is more simple and regular than that of the individual languages. The new common language will be more simple and regular than the existing European languages. It will be as simple as Occidental; in fact, it will be Occidental. To an English person, it will seem like simplified English, as a skeptical Cambridge friend of mine told me what Occidental is."
    )
    sentences_information = paragraph_handler.get_calculated_word_count_and_sentence(list_of_strings)
    shortest_sentence = paragraph_handler.get_shortest_sentence_and_words_count(sentences_information)
    print(f"\nThe shortest sentence is:{shortest_sentence['sentence']}. It consist of {shortest_sentence['lenght_in_words']} words.")
    print("\nHere is the paragraph in which the first and every other letter from every word is capitalized:")
    print(paragraph_handler.get_paragraph_with_every_secound_letter_captalized("The European languages are members of the same family. Their separate existence is a myth. For science, music, sport, etc, Europe uses the same vocabulary. The languages only differ in their grammar, their pronunciation and their most common words. Everyone realizes why a new common language would be desirable: one could refuse to pay expensive translators. To achieve this, it would be necessary to have uniform grammar, pronunciation and more common words. If several languages coalesce, the grammar of the resulting language is more simple and regular than that of the individual languages. The new common language will be more simple and regular than the existing European languages. It will be as simple as Occidental; in fact, it will be Occidental. To an English person, it will seem like simplified English, as a skeptical Cambridge friend of mine told me what Occidental is."))
    print("\nHere is a version of the paragraph in which all words are in reversed order:")
    print(paragraph_handler.get_reversed_paragraph("The European languages are members of the same family. Their separate existence is a myth. For science, music, sport, etc, Europe uses the same vocabulary. The languages only differ in their grammar, their pronunciation and their most common words. Everyone realizes why a new common language would be desirable: one could refuse to pay expensive translators. To achieve this, it would be necessary to have uniform grammar, pronunciation and more common words. If several languages coalesce, the grammar of the resulting language is more simple and regular than that of the individual languages. The new common language will be more simple and regular than the existing European languages. It will be as simple as Occidental; in fact, it will be Occidental. To an English person, it will seem like simplified English, as a skeptical Cambridge friend of mine told me what Occidental is."))
    
