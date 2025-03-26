# generate_embeddings.py
from langchain.text_splitter import CharacterTextSplitter
from sentence_transformers import SentenceTransformer
import faiss
import pickle

# Load full text
with open("data/full_text.txt", "r") as f:
    full_text = f.read()

# Step 1: Split text into chunks
splitter = CharacterTextSplitter(separator="\n", chunk_size=500, chunk_overlap=50)
chunks = splitter.split_text(full_text)

# Step 2: Generate embeddings
model = SentenceTransformer("all-MiniLM-L6-v2")  # Optionally switch to BioSentVec later
embeddings = model.encode(chunks)

# Step 3: Store in FAISS
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

# Save index and chunks
with open("embeddings/docs.pkl", "wb") as f:
    pickle.dump((index, chunks), f)

print(f"✅ Embedded {len(chunks)} chunks and saved to embeddings/docs.pkl")
