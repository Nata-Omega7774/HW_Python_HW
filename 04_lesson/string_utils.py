class StringUtils:
    def capitalize(self, string: str) -> str:
        return string.capitalize()
    
    def trim(self, string: str) -> str:
        return string.lstrip()
    
    def to_list(self, string: str, delimeter=",") -> list:
        if not string:
            return []
        return string.split(delimeter)
    
    def contains(self, string: str, symbol: str) -> bool:
        return symbol in string
    
    def delete_symbol(self, string: str, symbol: str) -> str:
        return string.replace(symbol, "")
    
    def startswith(self, string: str, symbol: str) -> bool:
        return string.startswith(symbol)
    
    def endswith(self, string: str, symbol: str) -> bool:
        return string.endswith(symbol)
    
    def is_empty(self, string: str) -> bool:
        return not string.strip()
    
    def list_to_string(self, lst: list, joiner=", ") -> str:
        if joiner is None:
            joiner = ", "
        return joiner.join(map(str, lst))
