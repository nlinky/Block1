import names


from dataclasses import dataclass
from faker import Faker
fake = Faker()


@dataclass(frozen=True)
class TestUserRegister:
    first_name: str
    last_name: str
    email: str
    password: str


@dataclass(frozen=True)
class TestUserLogin:
    email: str
    password: str


# str(time.time()) + '@mail.org'
UserLogin = TestUserLogin('ttest@test.test', '123456')
UserRegister1 = TestUserRegister(names.get_first_name(), names.get_last_name(), fake.email(), '123qwe789')
UserRegister2 = TestUserRegister(names.get_first_name(gender='male'), names.get_last_name(), fake.email(), '123qwe789')
UserRegister3 = TestUserRegister(names.get_first_name(gender='female'), names.get_last_name(), fake.email(), '123qwe789')
