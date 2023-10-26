import unittest

from task_one import ParagraphHandler

class TestTextHandler(unittest.TestCase):

    def test_get_string_without_punctuation(self):
        paragraph_handler = ParagraphHandler()
        paragraph_without_punctuation = paragraph_handler.get_string_without_punctuation("Please! remove... all? punctuation; from' this. text:")
        self.assertEqual(paragraph_without_punctuation, "Please remove all punctuation from this text")

    def test_list_of_words_from_sentence(self):
        paragraph_handler = ParagraphHandler()
        words_list = paragraph_handler.get_list_of_words_from_sentence("The European languages are members of the same family.")
        self.assertEqual(words_list, ["The","European", "languages", "are", "members", "of", "the", "same", "family."])

    def test_get_list_of_sentences(self):
        paragraph_handler = ParagraphHandler()
        sentences_list = paragraph_handler.get_list_of_sentences("For science, music, sport, etc, Europe uses the same vocabulary. The languages only differ in their grammar, their pronunciation and their most common words.")
        self.assertAlmostEqual(sentences_list, ["For science, music, sport, etc, Europe uses the same vocabulary", " The languages only differ in their grammar, their pronunciation and their most common words"])

    def test_get_word_list_with_lowered_letters(self):
        paragraph_handler = ParagraphHandler()
        paragraph_without_punctuation = paragraph_handler.get_string_without_punctuation("For science, music, sport, etc, Europe uses the same vocabulary. The languages only differ in their grammar, their pronunciation and their most common words.")
        word_list_with_lowered_letters = paragraph_handler.get_word_list_with_lowered_letters(paragraph_without_punctuation)
        self.assertEqual(word_list_with_lowered_letters,["for", "science", "music", "sport", "etc", "europe", "uses", "the", "same", "vocabulary", "the", "languages", "only", "differ", "in", "their", "grammar", "their", "pronunciation", "and", "their", "most", "common", "words"])

    def test_get_unique_words_count(self):
        paragraph_handler = ParagraphHandler()
        unique_words_count = paragraph_handler.get_unique_words_count(["their", "separate", "existence", "is", "a", "myth", "is", "is", "a", "myth"])
        self.assertEqual(unique_words_count, {"their":1, "separate":1, "existence": 1, "is": 3, "a": 2, "myth":2})

    def test_get_three_most_used_words(self):
        paragraph_handler = ParagraphHandler()
        most_used_words = paragraph_handler.get_three_most_used_words({"their":1, "separate":1, "existence": 1, "is": 3, "a": 2, "myth":2})
        self.assertEqual(most_used_words,["is", "a", "myth"])

    def test_get_string_from_list(self):
        paragraph_handler = ParagraphHandler()
        sentence = paragraph_handler.get_string_from_list(["The ","European ", "languages ", "are ", "members ", "of ", "the ", "same ", "family."])
        self.assertEqual(sentence, "The European languages are members of the same family.")

    # def test_get_calculated_word_count_and_sentence(self):
    #     paragraph_handler = ParagraphHandler()
    #     sentence_list = paragraph_handler.get_calculated_word_count_and_sentence(["For science, music, sport, etc, Europe uses the same vocabulary", " The languages only differ in their grammar, their pronunciation and their most common words."])
    #     self.assertEqual(sentence_list, {"sentence_one": {"sentence" : "For science, music, sport, etc, Europe uses the same vocabulary", "lenght_in_words":10}, "sentence_two":{"sentence": "The languages only differ in their grammar, their pronunciation and their most common words","lenght_in_words": 14 }})
    
    def test_get_word_with_every_secound_letter_capitalized(self):
        


if __name__ == "__main__":
    unittest.main()