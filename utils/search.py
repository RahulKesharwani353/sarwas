import re
import pandas as pd

WORD = re.compile(r"\w+")
def text_to_vector(text):
    from collections import Counter
    words = WORD.findall(text)
    return Counter(words)

def get_cosine(vec1, vec2):
        import math
        intersection = set(vec1.keys()) & set(vec2.keys())
        numerator = sum([vec1[x] * vec2[x] for x in intersection])

        sum1 = sum([vec1[x] ** 2 for x in list(vec1.keys())])
        sum2 = sum([vec2[x] ** 2 for x in list(vec2.keys())])
        denominator = math.sqrt(sum1) * math.sqrt(sum2)

        if not denominator:
            return 0.0
        else:
            return float(numerator) / denominator

def search_results(query):
    df = pd.read_csv('utils/final-dataset.csv')
    df = baba(df=df)
    df['sim_score'] = 0.5
    txt_to_vec_query = text_to_vector(query)
    for i in range(len(df['part_desc'])):
        df['sim_score'] = get_cosine(df['part_desc'][i],txt_to_vec_query)
    return df.sort_values(by=['sim_score'],ascending=False)

def baba(df):
    partition_data_desc = [""]*len(df['partition'].unique())
    for i in range(len(df['partition'])):
        idx = df['partition'][i]
        partition_data_desc[idx] += str(df['description'][i])
    
    for i in range(len(df)):
            df['part_desc'][i] = text_to_vector(partition_data_desc[df['partition'][i]])
    return df