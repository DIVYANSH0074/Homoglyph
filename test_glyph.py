import unittest

from reg_ds.homoglyph import homoglyph_regex


class ADFGeneratorGlyphsTest(unittest.TestCase):
    def test_MTCO_regex(self):
        pattern = {'regex': ['(?i)(Sections?)?\\s*', '(?<!-)(?P<titleChapterSection>((?:\\d+[A-Z]*(?:\\-)\\d+([A-Za-z]*)(?:-)\\d+[A-Za-z]*((\\s+|\\Z)(?:\\,\\s+)?))((\\band\\b|\\bor\\b)?\\s*))+)(?:MCA)?'], 'adf': {'repo': 'US-MTCO', 'titleChapterSection': '{}'}, 'split_regex': {'titleChapterSection': {'title': '(?P<title>\\d+[A-Z]*)(?:\\-)(?:(\\d(\\S(?!\\;))*(?:\\s+|\\Z)(\\,\\s+)?))((\\band\\b|\\bor\\b)?\\s*)', 'chapter': '(?:\\d+[A-Z]*)(\\-)(?P<chapter>(\\d*(?:\\.)?\\d*))(\\s+|\\Z)?((\\band\\b|\\bor\\b)?\\s*)', 'section': '(?:\\d+[A-Z]*)(\\-)(?:\\d+)(\\-)(?P<section>(\\d+))'}}, 'name': 'section_symbol TITLE CHAPTER SECTION', 'example': 'Section 2-3-103, MCA'}
        pattern_h = {'regex': ['(?i)(Sections?)?\\s*', '(?<![˗۔‐‑‒–⁃−\\-➖Ⲻ﹘—])(?P<titleChapterSection>((?:\\d+[A-Z]*(?:[˗۔‐‑‒–⁃−\\-➖Ⲻ﹘—])\\d+([A-Za-z]*)(?:[˗۔‐‑‒–⁃−\\-➖Ⲻ﹘—])\\d+[A-Za-z]*((\\s+|\\Z)(?:\\,\\s+)?))((\\band\\b|\\bor\\b)?\\s*))+)(?:MCA)?'], 'adf': {'repo': 'US-MTCO', 'titleChapterSection': '{}'}, 'split_regex': {'titleChapterSection': {'title': '(?P<title>\\d+[A-Z]*)(?:[˗۔‐‑‒–⁃−\\-➖Ⲻ﹘—])(?:(\\d(\\S(?!\\;))*(?:\\s+|\\Z)(\\,\\s+)?))((\\band\\b|\\bor\\b)?\\s*)', 'chapter': '(?:\\d+[A-Z]*)([˗۔‐‑‒–⁃−\\-➖Ⲻ﹘—])(?P<chapter>(\\d*(?:\\.)?\\d*))(\\s+|\\Z)?((\\band\\b|\\bor\\b)?\\s*)', 'section': '(?:\\d+[A-Z]*)([˗۔‐‑‒–⁃−\\-➖Ⲻ﹘—])(?:\\d+)([˗۔‐‑‒–⁃−\\-➖Ⲻ﹘—])(?P<section>(\\d+))'}}, 'name': 'section_symbol TITLE CHAPTER SECTION', 'example': 'Section 2-3-103, MCA'}
        self.assertEqual(pattern_h, homoglyph_regex(pattern))

    def test_WYST_regex(self):
        pattern = {'regex': ['(?i)(W\\.S\\.\\s*)', '(?P<title>(\\d+))(\\-?)', '(?P<chapter>(\\d+))(\\-?)', '(?P<section>(\\d+))((\\(\\w+\\))+)?'], 'adf': {'repo': 'US-WYST', 'title': '{}', 'chapter': '{}', 'section': '{}'}, 'name': 'title, chapter and section', 'example': 'W.S. 13-2-802(a)(vi)'}
        pattern_h = {'regex': ['(?i)(W\\.S\\.\\s*)', '(?P<title>(\\d+))([˗۔‐‑‒–⁃−\\-➖Ⲻ﹘—]?)', '(?P<chapter>(\\d+))([˗۔‐‑‒–⁃−\\-➖Ⲻ﹘—]?)', '(?P<section>(\\d+))((\\(\\w+\\))+)?'], 'adf': {'repo': 'US-WYST', 'title': '{}', 'chapter': '{}', 'section': '{}'}, 'name': 'title, chapter and section', 'example': 'W.S. 13-2-802(a)(vi)'}
        self.assertEqual(pattern_h, homoglyph_regex(pattern))

    def test_ARCO_regex(self):
        pattern = {'regex': ['(?i:)(§+|Section)\\s*(?P<titleChapterSection>((?:\\d+(?:\\-)(?:\\d+)(?:\\-)(?:\\d+))', '((\\,|\\—|\\band\\b|\\bor\\b|\\b|through)\\s)*)+)\\s*'], 'adf': {'repo': 'US-ARCO', 'titleChapterSection': '{}'}, 'split_regex': {'titleChapterSection': {'title': '(?i)(?P<title>(\\d+[()0-9]*))(?:\\-)(\\d+[()0-9]*)(?:\\-)(\\d+[()0-9]*)', 'chapter': '(?i)(\\d+[()0-9]*)(?:\\-)(?P<chapter>(\\d+[()0-9]*))(?:\\-)(\\d+[()0-9]*)', 'section': '(?i)(\\d+[()0-9]*)(?:\\-)(\\d+[()0-9]*)(?:\\-)(?P<section>(\\d+[()0-9]*))'}}, 'example': '§§ 13-5-1004'}
        pattern_h = {'regex': ['(?i:)(§+|Section)\\s*(?P<titleChapterSection>((?:\\d+(?:[˗۔‐‑‒–⁃−\\-➖Ⲻ﹘—])(?:\\d+)(?:[˗۔‐‑‒–⁃−\\-➖Ⲻ﹘—])(?:\\d+))', '((\\,|[˗۔‐‑‒–⁃−\\-➖Ⲻ﹘—]|\\band\\b|\\bor\\b|\\b|through)\\s)*)+)\\s*'], 'adf': {'repo': 'US-ARCO', 'titleChapterSection': '{}'}, 'split_regex': {'titleChapterSection': {'title': '(?i)(?P<title>(\\d+[()0-9]*))(?:[˗۔‐‑‒–⁃−\\-➖Ⲻ﹘—])(\\d+[()0-9]*)(?:[˗۔‐‑‒–⁃−\\-➖Ⲻ﹘—])(\\d+[()0-9]*)', 'chapter': '(?i)(\\d+[()0-9]*)(?:[˗۔‐‑‒–⁃−\\-➖Ⲻ﹘—])(?P<chapter>(\\d+[()0-9]*))(?:[˗۔‐‑‒–⁃−\\-➖Ⲻ﹘—])(\\d+[()0-9]*)', 'section': '(?i)(\\d+[()0-9]*)(?:[˗۔‐‑‒–⁃−\\-➖Ⲻ﹘—])(\\d+[()0-9]*)(?:[˗۔‐‑‒–⁃−\\-➖Ⲻ﹘—])(?P<section>(\\d+[()0-9]*))'}}, 'example': '§§ 13-5-1004'}
        self.assertEqual(pattern_h, homoglyph_regex(pattern))

    def test_ECFR_regex(self):
        pattern = {'regex': ['(?i)(Sub-part)\\s*(?P<subpart>[a-zA-Z0-9]*)\\s*of\\s*the\\s*federal\\s*regulations\\s*,?\\s*section\\s*(?P<partSection>\\d+[a-z0-9A-Z.()]*)'], 'adf': {'repo': 'US-ECFR', 'partSection': '{}', 'subpart': '{}'}, 'split_regex': {'partSection': {'part': '(?P<part>\\d+)(\\.)(?:(\\d(\\S(?!\\;))*(\\s+|\\Z)(\\,\\s+)?))((\\band\\b|\\bor\\b)?\\s*)', 'section': '(?:\\d+)(\\.)(?P<section>(\\d(\\S(?!\\;))*(\\s+|\\Z)(\\,\\s+)?))((\\band\\b|\\bor\\b)?\\s*)'}}, 'name': 'TEXT', 'example': 'chapter 3'}
        pattern_h = {'regex': ['(?i)(Sub-part)\\s*(?P<subpart>[a-zA-Z0-9]*)\\s*of\\s*the\\s*federal\\s*regulations\\s*,?\\s*section\\s*(?P<partSection>\\d+[a-z0-9A-Z.()]*)'], 'adf': {'repo': 'US-ECFR', 'partSection': '{}', 'subpart': '{}'}, 'split_regex': {'partSection': {'part': '(?P<part>\\d+)(\\.)(?:(\\d(\\S(?!\\;))*(\\s+|\\Z)(\\,\\s+)?))((\\band\\b|\\bor\\b)?\\s*)', 'section': '(?:\\d+)(\\.)(?P<section>(\\d(\\S(?!\\;))*(\\s+|\\Z)(\\,\\s+)?))((\\band\\b|\\bor\\b)?\\s*)'}}, 'name': 'TEXT', 'example': 'chapter 3'}
        self.assertEqual(pattern_h, homoglyph_regex(pattern))

    def test_NYSE_CHICAGO_regex(self):
        pattern = {'regex': ['(?i)(?:Article\\s*)(?P<article>\\d+)(?:(\\,)?\\s*Rules?\\s*)', '(?P<partRule>(\\d+(\\S(?!\\;))*(\\s+|\\Z)(\\,\\s+)?(\\band\\b|\\bor\\b|\\b\\-\\b|\\b&\\b)?\\s*)+)'], 'adf': {'repo': 'US-NYSE_CHICAGO', 'article': '{}', 'partRule': '{}'}, 'split_regex': {'partRule': {'rule': '(?P<rule>(\\d+[A-Z]*))(?:(\\S(?!\\;))*(\\s+|\\Z)(\\,\\s+)?)((\\band\\b|\\bor\\b|\\b\\-\\b)?\\s*)'}}, 'name': 'Article article_number Rules rule_number', 'example': 'Article 20 Rules 9, 9A, and 11'}
        pattern_h = {'regex': ['(?i)(?:Article\\s*)(?P<article>\\d+)(?:(\\,)?\\s*Rules?\\s*)', '(?P<partRule>(\\d+(\\S(?!\\;))*(\\s+|\\Z)(\\,\\s+)?(\\band\\b|\\bor\\b|\\b[˗۔‐‑‒–⁃−\\-➖Ⲻ﹘—]\\b|\\b&\\b)?\\s*)+)'], 'adf': {'repo': 'US-NYSE_CHICAGO', 'article': '{}', 'partRule': '{}'}, 'split_regex': {'partRule': {'rule': '(?P<rule>(\\d+[A-Z]*))(?:(\\S(?!\\;))*(\\s+|\\Z)(\\,\\s+)?)((\\band\\b|\\bor\\b|\\b[˗۔‐‑‒–⁃−\\-➖Ⲻ﹘—]\\b)?\\s*)'}}, 'name': 'Article article_number Rules rule_number', 'example': 'Article 20 Rules 9, 9A, and 11'}
        self.assertEqual(pattern_h, homoglyph_regex(pattern))

    def test_OKST_regex(self):
        pattern = {'regex': ['(?i)(sections?)\\s*', '(?P<section>(\\d+(\\-)\\d+[.;,A-Za-z]*((\\-)\\d+[\\.;A-Za-z]*)?\\s*(\\s+|\\Z)(\\,\\s)?))'], 'adf': {'repo': 'US-OKST', 'section': '{}', 'title': 'this'}, 'name': 'text section', 'example': 'Section 2-2 or section 2-2-1993'}
        pattern_h = {'regex': ['(?i)(sections?)\\s*', '(?P<section>(\\d+([˗۔‐‑‒–⁃−\\-➖Ⲻ﹘—])\\d+[.;,A-Za-z]*(([˗۔‐‑‒–⁃−\\-➖Ⲻ﹘—])\\d+[\\.;A-Za-z]*)?\\s*(\\s+|\\Z)(\\,\\s)?))'], 'adf': {'repo': 'US-OKST', 'section': '{}', 'title': 'this'}, 'name': 'text section', 'example': 'Section 2-2 or section 2-2-1993'}
        self.assertEqual(pattern_h, homoglyph_regex(pattern))


if __name__ == '__main__':
    unittest.main()