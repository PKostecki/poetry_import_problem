from fastpbkdf2 import pbkdf2_hmac

raw = pbkdf2_hmac("sha512", 'test', 'test', 'test', 'test')
