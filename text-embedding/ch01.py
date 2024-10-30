from sentence_transformers import SentenceTransformer
import numpy as np

# 加载预训练的 Sentence-BERT 模型
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

def get_embedding(text: str) -> np.ndarray:
    """生成文本的向量表示"""
    embedding = model.encode(text)
    return embedding

# 示例文本
text = "我爱北京天安门"
vector = get_embedding(text)
print(vector)
