import plotly.express as px
normal_distribution = {
    "A": 8.2,
    "B": 1.5,
    "C": 2.8,
    "D": 4.3,
    "E": 12.7,
    "F": 2.2,
    "G": 2.0,
    "H": 6.1,
    "I": 7.0,
    "J": 0.16,
    "K": 0.77,
    "L": 4.0,
    "M": 2.4,
    "N": 6.7,
    "O": 7.5,
    "P": 1.9,
    "Q": 0.12,
    "R": 6.0,
    "S": 6.3,
    "T": 9.1,
    "U": 2.8,
    "V": 0.98,
    "W": 2.4,
    "X": 0.15,
    "Y": 2.0,
    "Z": 0.074,
}
def analysis(text):
        dictt = {}
        dict_repeat = {}
        dict_tri = {}
        text = text.rstrip("\n")
        for letter1 in text:
                for letter2 in text:
                        if f"{letter1}{letter2}" in text:
                                if letter1 == letter2:
                                        dict_repeat[f"{letter1}{letter2}"] = text.count(f"{letter1}{letter2}")
                                else:
                                        dictt[f"{letter1}{letter2}"] = text.count(f"{letter1}{letter2}")
                                for letter3 in text:
                                        if f"{letter1}{letter2}{letter3}" in text:
                                                dict_tri[f"{letter1}{letter2}{letter3}"] = text.count(f"{letter1}{letter2}{letter3}")
        text = text.lower()
        text = list(text)
        text.sort(reverse=False)
        text = ''.join(text)
        Dict_letter_count = dict([(i, (text.count(i) / len(text) * 100)) for i in text])
        chart_input = px.bar(y = Dict_letter_count.values(), x = Dict_letter_count.keys())
        chart_normal = px.bar(y = normal_distribution.values(), x = normal_distribution.keys())

        for letter1 in text:
                for letter2 in text:
                        if f"{letter1}{letter2}" in text:
                                if letter1 == letter2:
                                        dict_repeat[f"{letter1}{letter2}"] = text.count(f"{letter1}{letter2}")
                                else:
                                        dictt[f"{letter1}{letter2}"] = text.count(f"{letter1}{letter2}")
        chart_input_bigramm = px.bar(y = dictt.values(), x = dictt.keys())
        chart_input_bigramm_repeat = px.bar(y =dict_repeat.values(), x = dict_repeat.keys())
        chart_input_tri = px.bar(y =dict_tri.values(), x = dict_tri.keys())
        chart_input.show()
        chart_normal.show()
        chart_input_bigramm.show()
        chart_input_bigramm_repeat.show()
        chart_input_tri.show()
if __name__ == "__main__":
        print(analysis("Helloeoghhgoegh\n"))
        analysis("APShfouwwwwwwwwwweeeeeeeeeeg0hq0ghthq0jkrt-2u3y20thqtwgj")
        #print(test_dict("APShfoug0hq0ghthq0jkrt-2u3y20thqtwgj"))
