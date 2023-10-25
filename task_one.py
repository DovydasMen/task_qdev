import re
from typing import Dict, List, Any


class TextHandler:

    @staticmethod
    def get_string_without_punctuation(paragraph: str) -> str:
        """Recieve string with all punctuation. Function return string without punctuation. Uses regex expresion."""
        return re.sub(r"[^\w\s]", "", paragraph)
    
    @staticmethod
    def get_list_of_words_from_sentence(sentence_list: str)-> List[str]:
        return [word for word in sentence_list.split(" ")]
    
    @staticmethod
    def get_list_in_lover_cases(paragraph: str) -> List[str]:
        """Recieve string with diffrent capital letters. Funcions returns list of strings with all letters lowered."""
        return [word.lower() for word in paragraph.split(" ")]

    @staticmethod
    def get_unique_words_count(words_list: List[str]) -> Dict[str, int]:
        """Returns dictionary with calculated unique word count. To count it correctly you should provide list filled only with lower letters because of same word being capitalized it counts as diffrent value."""
        unique_words_count = {}
        for word in words_list:
            if word not in unique_words_count:
                unique_words_count[f"{word}"] = 1
            else:
                unique_words_count[f"{word}"] += 1
        return unique_words_count

    @staticmethod
    def print_three_most_used_words(unique_values_counter: Dict[str, int]) -> None:
        """Funcions prints out the top 3 most used words. Provided dictionary format should be: {str : int}."""
        first_max_key = max(unique_values_counter, key=unique_values_counter.get)
        print(first_max_key)
        del unique_values_counter[first_max_key]
        secound_max_key = max(unique_values_counter, key=unique_values_counter.get)
        print(secound_max_key)
        del unique_values_counter[secound_max_key]
        third_max_value = max(unique_values_counter, key=unique_values_counter.get)
        print(third_max_value)

    @staticmethod
    def get_list_of_sentences(paragraph: str) -> List[str]:
        "Returns sentences placed in list, paragraph is splitted after every dot, and removed last whitespace after last dot."
        return paragraph.strip(".").split(".")

    @staticmethod
    def get_string_from_list(word_list: List[str]) -> str:
        """Returns string expresion after getting list of strings."""
        sentence = ""
        for word in word_list:
            sentence += word
        return sentence

    @staticmethod
    def get_calculated_word_count_and_sentence(sentences_list: List[str]) -> Dict[str, Any]:
        """Returns dictionary with all counted words in each sentence and sentences it selfs."""
        sentence_informmation = {}
        counter = 0
        for sentence in sentences_list:
            set_uped_sentence = sentence.strip().split(" ")
            sentence_lenght = len(set_uped_sentence)
            counter += 1
            sentence_in_str = word_manipulator.get_string_from_list(sentence)
            sentence_informmation[f"sentence_{str(counter)}"] = {
                "sentence": f"{sentence_in_str}",
                "lenght_in_words": sentence_lenght,
            }
        return sentence_informmation

    @staticmethod
    def print_shortest_sentence_and_words_count(
        dict_information: Dict[str, Any]
    ) -> None:
        """Prints out the shortest sentence and quantity of words in the shortest sentence."""
        min_letters_count: int = min(
            (count["lenght_in_words"] for count in dict_information.values())
        )
        sentence = ""
        for key, value in dict_information.items():
            if value["lenght_in_words"] == min_letters_count:
                sentence = value["sentence"]
        print(
            f"This is the shortest sentence: {sentence}, which have {min_letters_count} words."
        )

    @staticmethod
    def get_word_with_every_secound_letter_captalized(word_in_list: str)-> str:
        letters_in_word = []
        upper_letter = True
        for letter in word_in_list:
            letters_in_word.append(letter.upper() if upper_letter else letter.lower())
            upper_letter = not upper_letter
        return "".join(letters_in_word)
    
    @staticmethod    
    def get_paragraph_with_every_secound_letter_captalized(paragraph: str)-> None:
        words_list = word_manipulator.get_list_in_lover_cases(paragraph)
        concerted_paragraph = ""
        for word in words_list:
            concerted_paragraph+= word_manipulator.get_word_with_every_secound_letter_captalized(word) + " "
        print(concerted_paragraph)

    @staticmethod
    def print_reversed_paragraph(paragraph: str)-> None:
        paragraph_into_list_sentences = word_manipulator.get_list_of_sentences(paragraph)
        whole_reversed_paragraph = []
        for sentence in paragraph_into_list_sentences:
            striped_sentence = sentence.strip()
            reversed_sentence = word_manipulator.get_list_of_words_from_sentence(striped_sentence)
            reversed_sentence.reverse()
            whole_reversed_paragraph.append(reversed_sentence)
        reversed_paragraph = ""
        for sentence in whole_reversed_paragraph:
            sentence +="."
            
            for word in sentence:
                if word != ".":
                    reversed_paragraph += word + " "
                else:
                    reversed_paragraph +=word
        final_version= reversed_paragraph.replace(" .",". ")
        print(final_version)

if __name__ == "__main__":
    word_manipulator = TextHandler()
    # sentence = word_manipulator.get_string_without_punctuation("The European languages are members of the same family. Their separate existence is a myth. For science, music, sport, etc, Europe uses the same vocabulary. The languages only differ in their grammar, their pronunciation and their most common words. Everyone realizes why a new common language would be desirable: one could refuse to pay expensive translators. To achieve this, it would be necessary to have uniform grammar, pronunciation and more common words. If several languages coalesce, the grammar of the resulting language is more simple and regular than that of the individual languages. The new common language will be more simple and regular than the existing European languages. It will be as simple as Occidental; in fact, it will be Occidental. To an English person, it will seem like simplified English, as a skeptical Cambridge friend of mine told me what Occidental is.")
    # lowered_words_listed = word_manipulator.get_list_in_lover_cases(sentence)
    # unique_value_counted = word_manipulator.get_unique_words_count(lowered_words_listed)
    # print(unique_value_counted)
    # word_manipulator.print_three_most_used_words(unique_values_counter=unique_value_counted)
    good = word_manipulator.get_list_of_sentences(
        "The European languages are members of the same family. Their separate existence is a myth. For science, music, sport, etc, Europe uses the same vocabulary. The languages only differ in their grammar, their pronunciation and their most common words. Everyone realizes why a new common language would be desirable: one could refuse to pay expensive translators. To achieve this, it would be necessary to have uniform grammar, pronunciation and more common words. If several languages coalesce, the grammar of the resulting language is more simple and regular than that of the individual languages. The new common language will be more simple and regular than the existing European languages. It will be as simple as Occidental; in fact, it will be Occidental. To an English person, it will seem like simplified English, as a skeptical Cambridge friend of mine told me what Occidental is."
    )
    # print(good)
    # this_dict = word_manipulator.get_calculated_sentences(good)
    # word_manipulator.print_shortest_sentence_and_letter_count(this_dict)

    word_manipulator.print_reversed_paragraph("The European languages are members of the same family. Their separate existence is a myth. For science, music, sport, etc, Europe uses the same vocabulary. The languages only differ in their grammar, their pronunciation and their most common words. Everyone realizes why a new common language would be desirable: one could refuse to pay expensive translators. To achieve this, it would be necessary to have uniform grammar, pronunciation and more common words. If several languages coalesce, the grammar of the resulting language is more simple and regular than that of the individual languages. The new common language will be more simple and regular than the existing European languages. It will be as simple as Occidental; in fact, it will be Occidental. To an English person, it will seem like simplified English, as a skeptical Cambridge friend of mine told me what Occidental is.")