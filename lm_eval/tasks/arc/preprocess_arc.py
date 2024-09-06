def doc_to_text(doc):
    choice_letters = ["A", "B", "C", "D", "E"]
    choices = doc["choices"]["text"]
    num_choices = len(choices)
    question = doc["question"]
    #text = f"Question: {question}\n"
    text = f"{question.strip()}\n"
    for i in range(num_choices):
        text_i = choices[i]
        text += f"{choice_letters[i]}. {text_i}\n"
    text += "Answer:"
    return text


def doc_to_target(doc):
    idx = doc["sentence"].index("_") + 1
    return doc["sentence"][idx:].strip()


def doc_to_choice(doc):
    #print("choices:", doc["choices"]["text"])
    num_choices = len(doc["choices"]["text"])
    if num_choices == 3:
        return ["A", "B", "C"]
    elif num_choices == 4:
        return ["A", "B", "C", "D"]
    elif num_choices == 5:
        return ["A", "B", "C", "D", "E"]
