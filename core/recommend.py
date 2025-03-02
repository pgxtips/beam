from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

tags = ["sports, fitness", "tech, gadgets", "travel, adventure", "sports, outdoors"]
vectorizer = TfidfVectorizer()
tag_matrix = vectorizer.fit_transform(tags)

similarity = cosine_similarity(tag_matrix)
print(similarity)  # Higher values = more similar content
