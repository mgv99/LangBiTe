import re

def clean_string(input: str):
    cleaned_value = re.sub('\n',' ',input.strip()).lower()
    # Fixing mistralai/Mistral-7B-v0.1 outputs
    cleaned_value = re.sub('## expert answer', '', cleaned_value.strip()).lower()
    cleaned_value = re.sub('## answer', '', cleaned_value.strip()).lower()
    cleaned_value = re.sub('## expert answeranswer:', '', cleaned_value.strip()).lower()
    cleaned_value = re.sub('## expert answer answer:', '', cleaned_value.strip()).lower()
    cleaned_value = re.sub('##', '', cleaned_value.strip()).lower()
    cleaned_value = re.sub('answer yes', 'yes', cleaned_value.strip()).lower()
    cleaned_value = re.sub('answeryes', 'yes', cleaned_value.strip()).lower()
    cleaned_value = re.sub('answerno', 'no', cleaned_value.strip()).lower()
    cleaned_value = re.sub('answer no', 'no', cleaned_value.strip()).lower()
    return cleaned_value


