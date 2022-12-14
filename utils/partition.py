def partition(title, desc):
    import pandas as pd
    import re

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

    def rahu(df,title,desc):

        import numpy as np

        #Generate asin number
        asin_list = df['asin'].unique()
        asin = int(np.random.randint(low=max(df['asin'])+1))
        while asin in asin_list:
            asin = int(np.random.randint(low=max(df['asin'])+1))

        #Find best partition
        maxi,partition_num = 0,0
        for i in range(len(df['part_desc'])):
            score = get_cosine(text_to_vector(title),df['part_desc'][i])
            if score>=maxi:
                maxi = score
                partition_num = df['partition'][i]    

        df.loc[len(df.index)] = [asin,title,0.,desc,partition_num,None]
        for i in range(len(df)):
            df['part_desc'][i] = text_to_vector(partition_data_desc[df['partition'][i]])
        df.to_csv("utils/final-dataset.csv",index=False)
        print("df overwrited", partition_num)
        return partition_num




    df = pd.read_csv('utils/final-dataset.csv')
    partition_data_desc = [""]*len(df['partition'].unique())
    for i in range(len(df['partition'])):
        idx = df['partition'][i]
        partition_data_desc[idx] += str(df['description'][i])
        
    for i in range(len(df)):
            df['part_desc'][i] = text_to_vector(partition_data_desc[df['partition'][i]])

    d = rahu(df,title=title,desc=desc)

    return d