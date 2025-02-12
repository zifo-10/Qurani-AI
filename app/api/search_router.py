from fastapi import APIRouter, Depends

from app.models.aya import QuranModel
from app.services.search_service import SearchService
from app.api.dependencies import get_search_service

quran_search = APIRouter()

@quran_search.get("")
def search(
    query: str,
    search_service: SearchService = Depends(get_search_service)
) -> dict[str, list[QuranModel]]:
    """
    Search for a given query using the search service.

    This endpoint performs a search operation on the provided query string
    and returns relevant results.

    :param query: The search term to look up.
    :param search_service: The search service instance (dependency).
    :return: The search results.
    """
    # Delegate the search operation to the search service
    return search_service.search(query)
