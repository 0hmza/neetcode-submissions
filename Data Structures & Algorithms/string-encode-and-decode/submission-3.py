class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return str(2)
        if strs == [""]:
            return str(3)
        return ".".join(strs)
    def decode(self, s: str) -> List[str]:
        if s == str(2):
            return []
        if s == str(3):
            return [""]
        return s.split('.')
        