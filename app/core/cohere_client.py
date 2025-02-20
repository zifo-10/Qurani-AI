import cohere

from app.core.embedding_interface import EmbeddingClient


class CohereClient(EmbeddingClient):
    def __init__(self, api_key: str):
        """
        Initialize the Cohere client with the provided API key.

        :param api_key: The API key to use for authentication.
        """
        self.client = cohere.Client(api_key=api_key)

    def embed_text(self, texts, model = "embed-multilingual-light-v3.0", input_type = "search_query", embedding_types = ["float"]) -> list:
        """
        Embed a list of texts using the specified model and input type.

        This method embeds a list of texts using the specified model and input type,
        returning the resulting embeddings.

        :param texts:  The list of texts to embed.
        :param model: The model to use for embedding.
        :param input_type: The input type for the texts.
        :param embedding_types: The types of embeddings to return.
        :return: The embeddings for the input texts.
        """
        try:
            # Embed the provided texts
            embed = self.client.embed(
                texts=texts,
                model=model,
                input_type=input_type,
                embedding_types=embedding_types,
            )
            vector = embed.embeddings.model_dump()['float_'][0]
            # Return the vector
            return vector
        except Exception as e:
            raise ValueError(f"Failed to embed text: {e}")
