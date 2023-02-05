def asin_and_partition_num_generate(title, desc):
        """Outputs the partition and asin Number of a new product by its title and description while appending a row in the existing dataset"""
       
        import pandas as pd
        import numpy as np
        from multiprocessing import Pool
        from sklearn.feature_extraction.text import TfidfVectorizer
        from sklearn.metrics.pairwise import cosine_similarity

        df = pd.read_csv("utils/SARWAS_dataset.csv")
       
        partition_data_desc = [""]*len(df['partition'].unique())
        for i in range(len(df['partition'])):
            idx = df['partition'][i]
            partition_data_desc[idx] += str(df['description'][i]) + str(df['title'][i])
        # Use vectorized operations to calculate text vectors
        vectorizer = TfidfVectorizer()
        descriptions = partition_data_desc
        X = vectorizer.fit_transform(descriptions)

        title_vector = vectorizer.transform([str(title+" "+desc)])
        scores = cosine_similarity(title_vector, X)

        # Find the partition with the highest score
        partition_num = np.argmax(scores)
       
       
        #Generate asin number
        asin_list = df['asin'].unique()
        asin = int(np.random.randint(low=100000))
        while asin in asin_list:
            asin = int(np.random.randint(low=100000))
       
        #Append and write to dataset
        new_row = {"asin": asin, "title": title, "description": desc, "partition": partition_num, "CC_score": 0}
        df = df.append(new_row, ignore_index=True)
        df.to_csv("utils/existing_dataset.csv", index=False)
       
        return partition_num,asin