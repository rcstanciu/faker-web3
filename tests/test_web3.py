from string import hexdigits
from unittest import TestCase

from faker import Faker

from faker_web3 import Web3Provider

fake = Faker()
fake.add_provider(Web3Provider)


class PrivateKeyTests(TestCase):
    def test_generate_private_key(self):
        assert fake.web3_private_key() is not None

    def test_does_not_generate_repeating_private_keys(self):
        keys = [fake.web3_private_key() for i in range(100)]
        self.assertCountEqual(list(set(keys)), keys)

    def test_returns_the_correct_format(self):
        key = fake.web3_private_key()
        assert len(key) == 32 * 2 + 2  # 32 bytes * 2 chars each byte + 2 (0x prefix)

        assert key[0:2] == "0x"
        for char in key[2:]:
            assert char in hexdigits
