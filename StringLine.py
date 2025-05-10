#  Исходные данные 
lines = [
    "   hELLo WoRLD   ",
    "123 GO!",
    "    python  ",
    "   ",
    "PiV0",
    "MONEY$$$",
    "   TABS\t\t",
    "   oN yOuR leFt  ",
    "finalBOSS123",
    "piña colada",
    "   42  ",
    "   \n\t   ",
    "   CoDe Or dIe   ",
    "HELLO",
    "   brUh MOMENT",
    "sussyBAKA420",
    "π is life",
    "DON'T YELL!",
    "  wOrK hArD  ",
    "piRoGi",
    "oOoOoOoOoOo",
    "YOLO123",
    "   space   man   ",
    "lowerCASE",
    "UPPERCASE",
    "  mixED CaSe  ",
    "   what_the?!   ",
    "2007",
    "   nice123nice   ",
    "    "
]

#Функцию

def process_line(s):
    original = s 
    s = s.strip()

    if len(s) == 0 or s.isspace():
        return "ПУСТАЯ СТРОКА --> o-count: 0"
    if s.isalnum():
        s = s.upper()
    elif all(c.isalpha() or c.isspace() for c in s):
        s = s.title()
    elif any(c.islower() for c in s) and any(c.isupper() for c in s):
        s = s.swapcase()
    if s.lower().startswith("pi"):
        s = "π" + s[2:] 
    o_count = s.lower().count("o")
    return f"{s} --> o-count: {o_count}"


for line in lines:
    print(process_line(line))
#ДЗ Для Артема Сделай Сортировку строк по количеству "o" В конце 