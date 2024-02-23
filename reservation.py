from typing import Any, TypedDict
from datetime import datetime


class CancellationDisplay(TypedDict):
    policy: list[str]


class RefundOrChangeOrCredit(TypedDict):
    date_cut_off: datetime | None


class Config(TypedDict):
    double_confirmation: list[str]


class ServiceCharge(TypedDict):
    amount: int
    value: str


class Amounts(TypedDict):
    items: list[Any]
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


class Balance(TypedDict):
    value: str
    modifier: str


class Buy(TypedDict):
    action: str
    after_modifier: str
    before_modifier: str
    init: str
    value: str


class ConfigOrDisplay(TypedDict):
    type: str


class Display(TypedDict):
    balance: Balance
    buy: Buy
    description: list[str]


class Option(TypedDict):
    amounts: Amounts


class PaymentAmounts(TypedDict):
    price_per_unit: float
    resy_fee: int
    service_fee: int
    service_charge: ServiceCharge
    tax: float
    total: float
    reservation_charge: float


class User(TypedDict):
    payment_methods: None


class Payment(TypedDict):
    amounts: PaymentAmounts
    comp: bool
    config: ConfigOrDisplay
    display: Display
    options: list[Option]


class BookToken(TypedDict):
    date_expires: datetime
    value: str


class Cancellation(TypedDict):
    display: CancellationDisplay
    refund: RefundOrChangeOrCredit


class ReservationDetails(TypedDict):
    cancellation: Cancellation
    change: RefundOrChangeOrCredit
    config: Config
    payment: Payment
    user: User
    book_token: BookToken
