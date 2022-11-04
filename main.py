from fastpbkdf2 import pbkdf2_hmac as _pbkdf2_hmac

raw = _pbkdf2_hmac("sha512", 'test', 'test', 'test', 'test')
