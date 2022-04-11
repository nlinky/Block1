from dataclasses import dataclass


@dataclass(frozen=True)
class TestBillingAddress:
    city: str
    address1: str
    zip: int
    phone: int


BillingAddress = TestBillingAddress('City', 'Address1', 440000, 89876543210)
