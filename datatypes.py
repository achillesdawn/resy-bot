from dataclasses import dataclass
from typing import TypedDict, Optional


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


class VenueSlotDate(TypedDict):
    end: str
    start: str


class VenueTable(TypedDict):
    id: list[int]


class PaymentInfo(TypedDict):
    cancellation_fee: Optional[float]
    deposit_fee: float
    is_paid: bool
    payment_structure: int
    service_charge: str
    venue_share: int


Size = TypedDict('Size', {'assumed': int})


class VenueSlotMeta(TypedDict):
    size: Size


class VenueSlotConfig(TypedDict):
    id: int
    token: str
    type: str


class VenueSlot(TypedDict):
    date: VenueSlotDate
    table: VenueTable
    quantity: int
    payment: PaymentInfo
    meta: VenueSlotMeta
    config: VenueSlotConfig


Inventory = TypedDict(
    "Inventory", {
        "reservation": str,
        "event": str,
        "walk-in": str
    }
)


class Scheduled(TypedDict):
    date: str
    inventory: Inventory


class ScheduleData(TypedDict):
    scheduled: list[Scheduled]
    last_calendar_day: str
