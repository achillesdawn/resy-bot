from dataclasses import dataclass
from typing import TypedDict

@dataclass
class VenueInfo:
    id: int
    name: str
    location: str

class RateInfo(TypedDict):
    name: str
    scale: int
    score: float
    total: int

class ContactInfo(TypedDict):
    phone_number: str
    url: str

class VenueMetadata(TypedDict):
    description: str
    keywords: list[str]

class VenueTicketData(TypedDict):
    average_str: str

class VenueIdSources(TypedDict):
    resy: int

class VenueContent(TypedDict):
    name: str
    body: str
class VenueData(TypedDict):
    id: VenueIdSources
    type: str
    name: str
    url_slug: str
    rater: list[RateInfo]
    min_party_size: int
    max_party_size: int
    is_active: bool
    contact: ContactInfo
    large_party_message: str
    ticket: VenueTicketData
    metadata: VenueMetadata
    content: list[VenueContent]


