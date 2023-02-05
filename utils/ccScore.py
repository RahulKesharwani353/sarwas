def CC_score_generator(asin,review,ratings,W_review=0.7,W_rating=0.3):
    from textblob import TextBlob
    import numpy as np
    import pandas as pd
   
    review_polar = TextBlob(review).sentiment.polarity
    ratings_avg = np.mean(ratings)
   
    df = pd.read_csv("utils/existing_dataset.csv")
   
    df['CC_score'][df['asin']==asin] = np.add(np.multiply(review_polar,W_review),np.multiply(ratings_avg,W_rating))
    df.to_csv("utils/existing_dataset.csv",index=False)
                                             
    return np.add(np.multiply(review_polar,W_review),np.multiply(ratings_avg,W_rating))