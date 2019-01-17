import unicodedata

class Japanese:
    def is_japanese(string):
        for ch in string:
            name = unicodedata.name(ch)
            if "CJK UNIFIED" in name:
                return True
            return False
