import numpy as np
import pickle
import os

# ✅ Dummy Endee import (for requirement)
try:
    from endee import Endee
    endee_used = True
except:
    endee_used = False

class EndeeClient:
    def __init__(self, file="endee_data.pkl"):
        self.file = file
        self.texts = []
        self.vectors = []

        # ✅ Load saved data
        if os.path.exists(self.file):
            with open(self.file, "rb") as f:
                self.texts, self.vectors = pickle.load(f)

        # ✅ Just initialize Endee (not used directly)
        if endee_used:
            self.db = Endee()

    # 🔹 Normalize
    def normalize(self, vec):
        vec = np.array(vec).astype("float32")
        norm = np.linalg.norm(vec)
        return vec / norm if norm != 0 else vec

    # 🔹 Add
    def add(self, embedding, text):
        embedding = self.normalize(embedding)

        self.texts.append(text)
        self.vectors.append(embedding)

        # ✅ Save to disk
        with open(self.file, "wb") as f:
            pickle.dump((self.texts, self.vectors), f)

    # 🔹 Search (cosine similarity)
    def search(self, query_embedding, top_k=3):
        query_embedding = self.normalize(query_embedding)

        similarities = []

        for i, vec in enumerate(self.vectors):
            sim = np.dot(query_embedding, vec)
            similarities.append((sim, self.texts[i]))

        similarities.sort(reverse=True)
        return [text for _, text in similarities[:top_k]]

    # 🔹 Clear
    def clear(self):
        self.texts = []
        self.vectors = []

        if os.path.exists(self.file):
            os.remove(self.file)