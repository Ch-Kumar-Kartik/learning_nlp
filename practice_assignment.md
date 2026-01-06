# 📚 NLP Practice Assignment: Knowledge Check

## Overview
This assignment is designed to test your understanding of NLP concepts you've been learning, including:
- Text Preprocessing (Tokenization, Stemming, Lemmatization, Stopword Removal)
- Bag of Words (BoW)
- TF-IDF
- Cosine Similarity/Distance

**Datasets Available:**
- `datasets/SMSSpamCollection.txt` - SMS Spam classification dataset
- `datasets/all_kindle_review.csv` - Kindle book reviews
- `datasets/shakespeare_data.py` - Shakespeare play excerpts
- `datasets/hamlet.txt` - Hamlet's famous soliloquy

---

## Part 1: Text Preprocessing (20 points)

### Task 1.1: Custom Preprocessing Pipeline (10 points)
Create a Python script `preprocessing_practice.py` that:

1. Load the `hamlet.txt` file
2. **Using NLTK** (but without sklearn vectorizers), implement:
   - **Sentence tokenization** (split into sentences)
   - **Word tokenization** (split into words)
   - **Lowercasing**
   - **Punctuation removal** (using `string.punctuation` or regex)
   - **Stopword removal** (you can use NLTK's stopwords list)
   - **Stemming** (using PorterStemmer from NLTK)

3. Print the original text and the preprocessed tokens

**Expected Output Format:**
```
Original: "To be, or not to be, that is the question:"
Preprocessed: ['question']
```

### Task 1.2: Stemming vs Lemmatization Comparison (10 points)
Using the first 100 messages from `SMSSpamCollection.txt`:

1. Apply **Porter Stemmer** to all messages
2. Apply **WordNet Lemmatizer** to all messages
3. Compare the results by finding **5 words** that differ between stemming and lemmatization
4. Write your observations in markdown comments within your code

**Hint:** Look for words like "running", "better", "feet", etc.

---

## Part 2: Bag of Words Implementation (25 points)

### Task 2.1: Manual BoW (15 points)
Create a script `bow_practice_manual.py` that:

1. Use these 3 documents:
   ```python
   documents = [
       "I love machine learning and deep learning",
       "Machine learning is amazing",
       "Deep learning requires more data"
   ]
   ```

2. **Manually implement Bag of Words** WITHOUT using `CountVectorizer`:
   - Build a vocabulary (unique words across all documents)
   - Create a document-term matrix where each row is a document and each column is a word count
   - Output the vocabulary and the matrix

**Expected Output:**
```
Vocabulary: ['i', 'love', 'machine', 'learning', 'and', 'deep', 'is', 'amazing', 'requires', 'more', 'data']
Document-Term Matrix:
[[1, 1, 1, 2, 1, 1, 0, 0, 0, 0, 0],
 [0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0],
 [0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1]]
```

### Task 2.2: BoW for Spam Classification (10 points)
Using `SMSSpamCollection.txt`:

1. Load the dataset
2. Preprocess the text (lowercase, remove stopwords, stemming)
3. Create a BoW representation using `CountVectorizer`
4. Answer these questions in comments:
   - What is the vocabulary size?
   - What are the top 10 most frequent words in spam messages?
   - What are the top 10 most frequent words in ham messages?

---

## Part 3: TF-IDF Implementation (25 points)

### Task 3.1: Manual TF-IDF Calculation (15 points)
Create a script `tfidf_manual.py` that:

1. Use the same 3 documents from Part 2

2. **Manually calculate TF-IDF** WITHOUT using `TfidfVectorizer`:
   
   **Formulas to implement:**
   ```
   TF(t, d) = (Number of times term t appears in document d) / (Total number of terms in document d)
   
   IDF(t) = log(Total number of documents / Number of documents containing term t)
   
   TF-IDF(t, d) = TF(t, d) × IDF(t)
   ```

3. Show the TF-IDF scores for the word "learning" in all 3 documents

4. Verify your results by comparing with `TfidfVectorizer` output

### Task 3.2: Shakespeare Play Analysis (10 points)
Using `datasets/shakespeare_data.py`:

1. Import the Shakespeare plays data
2. Use TF-IDF to find the **top 5 most important/unique words** for each play
3. Create a simple "play recommender":
   - Given a user query (e.g., "love and jealousy"), find the most relevant play
   - Print the similarity scores for all plays

---

## Part 4: Cosine Similarity & Distance (20 points)

### Task 4.1: Manual Cosine Similarity (10 points)
Create a script `cosine_manual.py` that:

1. **Manually implement cosine similarity** WITHOUT using sklearn:
   ```python
   def cosine_similarity(vec1, vec2):
       # Your implementation here
       # Formula: (A · B) / (||A|| × ||B||)
       pass
   ```

2. Test with these vectors:
   ```python
   vec_a = [3, 4, 0, 0]
   vec_b = [4, 3, 0, 0]
   vec_c = [0, 0, 4, 3]
   ```

3. Calculate and print:
   - Similarity between vec_a and vec_b
   - Similarity between vec_a and vec_c
   - Distance (1 - similarity) for both pairs

4. **Question:** Why is the similarity between vec_a and vec_c equal to 0? Explain in comments.

### Task 4.2: Document Similarity Matrix (10 points)
Using the first 5 messages from `SMSSpamCollection.txt`:

1. Create TF-IDF vectors for each message
2. Compute a 5×5 similarity matrix showing the cosine similarity between all pairs
3. Print the matrix as a pandas DataFrame
4. Identify which two messages are most similar and explain why

---

## Part 5: Bonus Challenge (10 points)

### Kindle Review Sentiment Analyzer
Using `datasets/kindle_review/all_kindle_review.csv`:

1. Load the dataset (it contains reviews and ratings)
2. Preprocess the review text
3. Split into positive (rating >= 4) and negative (rating <= 2) reviews
4. Use TF-IDF to find:
   - Top 10 words associated with positive reviews
   - Top 10 words associated with negative reviews
5. Create a simple function that takes a review text and predicts if it's positive or negative based on word presence

---

## Submission Guidelines

1. Create all scripts in the `/home/ch_kumar_kartik/Books_Notes/Notes/NLP/codes/` directory
2. Name your files as specified in each task:
   - `preprocessing_practice.py`
   - `bow_practice_manual.py`
   - `tfidf_manual.py`
   - `cosine_manual.py`
   - (Bonus) `kindle_sentiment.py`
3. Include comments explaining your approach
4. Run each script and ensure it produces output without errors

---

## Grading Criteria

| Part | Task | Points |
|------|------|--------|
| 1 | Preprocessing Pipeline | 10 |
| 1 | Stemming vs Lemmatization | 10 |
| 2 | Manual BoW | 15 |
| 2 | BoW for Spam | 10 |
| 3 | Manual TF-IDF | 15 |
| 3 | Shakespeare Analysis | 10 |
| 4 | Manual Cosine Similarity | 10 |
| 4 | Document Similarity Matrix | 10 |
| 5 | Bonus: Kindle Analysis | 10 |
| **Total** | | **100** |

---

## Tips & Resources

- Review your existing notebooks: `bow_practical.ipynb`, `tf_idf_practice.ipynb`
- Check `cosine_distance.py` for reference on cosine calculations
- Use `numpy` for vector operations
- Use `pandas` for data manipulation
- Remember: The goal is to understand the concepts, not just use sklearn functions!

**Good luck! 🚀**
