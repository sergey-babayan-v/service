import re


class Parser:
    remove_chars = ['(', ')', '-', '\n', "  ", "\t\t"]

    def normalize(self, value):
        normalized = value
        for char in self.remove_chars:
            normalized = normalized.replace(char, "")
        start = normalized.index("body")
        return normalized[start:]

    def get_regexprs(self):
        return [
            re.compile(r"(\+?\d)?[ \t]?(\d{3}[ \t]?(\d{7}|\d{3}[ \t]\d{2}[ \t]\d{2}))")
        ]

    def get_numbers(self, html_str):
        phones = []
        normalized = self.normalize(html_str)
        for regexpr in self.get_regexprs():
            groups = regexpr.findall(normalized)
            for group in groups:
                code = "8"
                body = group[1].replace(" ", "").replace("\t", "")
                phones.append(code+body)
        return set(phones)
