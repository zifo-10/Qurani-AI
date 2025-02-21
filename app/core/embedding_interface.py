from abc import ABC, abstractmethod
from typing import Any, List


class EmbeddingClient(ABC):
    """
    Abstract base class for embedding clients.
    """

    @abstractmethod
    def embed_text(self, texts: List[str], **kwargs: Any) -> List[float]:
        """
        Generate embeddings for the given text(s).

        Parameters:
        -----------
        texts : str | list[str]
            A single text string or a list of text strings to embed.

        Returns:
        --------
        list[float]:
            st of embedding vectors for multiple inputs.
        """
        pass
