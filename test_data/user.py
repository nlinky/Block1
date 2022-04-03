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

    # first_name = names.get_first_name()
    # last_name = names.get_last_name()
    # email = fake.email()
    # password = '123qwe789'


@dataclass(frozen=True)
class TestUserLogin:
    email: str
    password: str

    # email = 'ttest@test.test'
    # password = '123456'


# str(time.time()) + '@mail.org'
UserLogin = TestUserLogin('ttest@test.test', '123456')
#UserLogin = TestUserLogin(TestUserLogin.email, TestUserLogin.password)
UserLoginInvalid = TestUserLogin('qwe', '1')
UserRegister1 = TestUserRegister(names.get_first_name(), names.get_last_name(), fake.email(), '123qwe789')
# UserRegister1 = TestUserRegister(TestUserRegister.first_name, TestUserRegister.last_name, TestUserRegister.email, TestUserRegister.password)
UserRegister2 = TestUserRegister(names.get_first_name(gender='male'), names.get_last_name(), fake.email(), '123qwe789')
UserRegister3 = TestUserRegister(names.get_first_name(gender='female'), names.get_last_name(), fake.email(), '123qwe789')
