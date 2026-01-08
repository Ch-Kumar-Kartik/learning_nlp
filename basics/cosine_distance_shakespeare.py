from shakespeare_data import shakespeare_plays, sample_queries
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity as sklearn_cosine_sim
import numpy as np
import pandas as pd
import math

corpus = list(shakespeare_plays.values())  # text of all plays
play_names = list(shakespeare_plays.keys())  # play names

# tfidf matrix
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(corpus)  # learn the vocab/unique words and convert into a tfidf vector matrix

print(f"TF-IDF Matrix shape: {tfidf_matrix.shape}") # 10 plays * vocabulary size
print(f"Number of plays: {len(play_names)}")
print(f"Vocabulary size: {len(vectorizer.get_feature_names_out())}\n")

# query define 
query_text = sample_queries[0]  
print(f"Query: '{query_text}'\n")

# query transform into tfidf vector
query_vector = vectorizer.transform([query_text])  

# calculate cosine similarity between query and each play
similarities = sklearn_cosine_sim(query_vector, tfidf_matrix)[0]  # Returns array of similarities

# dataframe
results = pd.DataFrame({
    'Play': play_names,
    'Similarity': similarities,
    'Distance': 1 - similarities
})

# sort by similarity
results = results.sort_values('Similarity', ascending=False)

print("="*70)
print(f"Ranking plays by similarity to query: '{query_text}'")
print("="*70)
print(results.to_string(index=False))
print("\n")

# top 3 most similar plays
print("="*70)
print("Top 3 Most Similar Plays:")
print("="*70)
for idx, row in results.head(3).iterrows():
    print(f"{row['Play']}: {row['Similarity']:.4f}")

# Bonus: Test with different queries
print("\n" + "="*70)
print("Testing all sample queries:")
print("="*70)

for i, query in enumerate(sample_queries):
    query_vec = vectorizer.transform([query])
    sims = sklearn_cosine_sim(query_vec, tfidf_matrix)[0]
    top_play_idx = np.argmax(sims)
    print(f"\nQuery {i+1}: '{query}'")
    print(f"  Most similar play: {play_names[top_play_idx]} (similarity: {sims[top_play_idx]:.4f})")
