from pydantic import BaseModel, Field


class QuranModel(BaseModel):
    ayah_ar: str = Field(description="Arabic Ayah")
    ayah_en: str = Field(description="English Ayah")
    Ayah_without_tashkil: str = Field(description="Ayah without tashkil")
    tafsir: str = Field(description='Ayah Tafseer')
    tafsir_name: str = Field(description='Tafseer name')
    surah_no: int = Field(description='Surah number')
    surah_name_ar: str = Field(description="Surah name in Arabic")
    surah_name_en: str = Field(description="Surah name in English")
    ayah_no_surah: int = Field(description="Ayah index in surah.")
    ayah_no_quran: int = Field(description="Ayah index in Quran")
    juz_no: int = Field(description="Juz index of ayah.")
    quarter_no: int = Field(description="Quarter index of ayah.")
    total_ayah_surah: int = Field(description="Total ayah number of surah.")
    total_ayah_quran: int = Field(description="Total ayah ayah of Quran.")
    has_sajdah: bool = Field(description="Ayah has sajdah.")
    sajdah_no: int = Field(description="Sajdah number in Quran.")
    is_meccan: bool = Field(description="Ayah is Meccan or Midian.")
