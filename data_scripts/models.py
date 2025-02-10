from pydantic import BaseModel, Field
from typing import List


class MongoSchema(BaseModel):
    ayah: str = Field(description="Ayah")
    tasfeer: str = Field(description='Ayah Tafseer')
    tasfeer_name: str = Field(description='Tafseer name')
    aya_index: int = Field(description='Ayah number')
    sura_index: int = Field(description='Sura number')
    sura_name: dict = Field(description='Sura name in different language')
    sura_type: dict = Field(description="Sura place")
    chunks: List[str] = Field(description='Chunk')
