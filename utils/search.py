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
    from sklearn.metrics.pairwise import cosine_similarity
    import numpy as np
    from sklearn.feature_extraction.text import TfidfVectorizer
    df = pd.read_csv('utils/existing_dataset.csv')

    partition_data_desc = [""]*len(df['partition'].unique())
    for i in range(len(df['partition'])):
        idx = df['partition'][i]
        partition_data_desc[idx] += str(df['description'][i]) + str(df['title'][i])

     # Use vectorized operations to calculate text vectors
    vectorizer = TfidfVectorizer()
    descriptions = partition_data_desc
    X = vectorizer.fit_transform(descriptions)

    title_vector = vectorizer.transform([str(query)])
    scores = cosine_similarity(title_vector, X)
    # Find the partition with the highest score
    partition_num = np.argmax(scores)


    # df['sim_score'] = 0
    # txt_to_vec_query = text_to_vector(query)
    # for i in range(len(df['part_desc'])):
    #     df['sim_score'] = get_cosine(df['part_desc'][i],txt_to_vec_query)
    # return df[df['partition']==df['partition'][df['sim_score'].idxmax()]]
    return df[df['partition']==partition_num].sort_values(by=['CC_score'],ascending=False).reset_index(drop=True).head(10)
