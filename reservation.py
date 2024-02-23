from __future__ import annotations

from typing import Any, TypedDict, List
from datetime import datetime

class ReservationDetails(TypedDict):
    cancellation: Cancellation
    change: RefundOrChangeOrCredit
    config: Config
    payment: Payment
    user: User
    book_token: BookToken

class Cancellation(TypedDict):
    display: Display
    refund: RefundOrChangeOrCredit

class Display(TypedDict):
    policy: List[str]

class RefundOrChangeOrCredit(TypedDict):
    date_cut_off: Union[None, datetime]

class Config(TypedDict):
    double_confirmation: List[str]


class Payment(TypedDict):
    amounts: Amounts
    comp: bool
    config: ConfigOrDisplay
    display: Display
    options: List[Option]

class Amounts(TypedDict):
    items: List[Any]
    reservation_charge: float
    subtotal: float
    add_ons: int
    quantity: int
    resy_fee: int
    service_fee: int
    service_charge: ServiceCharge
    tax: float
    total: float
    surcharge: int
    price_per_unit: float

class ServiceCharge(TypedDict):
    amount: int
    value: str

class ConfigOrDisplay(TypedDict):
    type: str

class Display(TypedDict):
    balance: Balance
    buy: Buy
    description: List[str]

class Balance(TypedDict):
    value: str
    modifier: str

class Buy(TypedDict):
    action: str
    after_modifier: str
    before_modifier: str
    init: str
    value: str

class Option(TypedDict):
    amounts: Amounts

class Amounts(TypedDict):
    price_per_unit: float
    resy_fee: int
    service_fee: int
    service_charge: ServiceCharge
    tax: float
    total: float

class User(TypedDict):
    payment_methods: None


class Config(TypedDict):
    allow_bypass_payment_method: int
    allow_multiple_resys: int
    enable_invite: int
    enable_resypay: int
    hospitality_included: int


class Icon(TypedDict):
    url: Union[None, str]

class Locale(TypedDict):
    language: str


class BookToken(TypedDict):
    date_expires: datetime
    value: str
