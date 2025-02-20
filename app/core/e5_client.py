from typing import List, Optional
from sentence_transformers import SentenceTransformer

from app.core.embedding_interface import EmbeddingClient


class E5Client(EmbeddingClient):
    """
    A client for generating text embeddings using the E5 embedding model.

    Attributes:
        model : SentenceTransformer
        The sentence transformer model used for generating embeddings.
    """

    def __init__(self, model_path: Optional[str] = "intfloat/multilingual-e5-small") -> None:
        """
        Initializes the E5Client with a specified model.

        Parameters:
            model_path (Optional[str]): The path or name of the pretrained E5 model to load.
        """
        self.model = SentenceTransformer(model_path)

    def embed_text(self, texts) -> List[float]:
        """
        Generates embeddings for the given text(s).

        Parameters:
            texts (str | list[str]): A single text string or a list of text strings to embed.

        Returns:
            list[float]:
                A single embedding vector if input is a string, 
                otherwise a list of embedding vectors for multiple inputs.
        """
        embeddings = self.model.encode(texts, normalize_embeddings=True)
        return embeddings[0]
