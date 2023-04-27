from passlib.context import CryptContext

hashing_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_hash(plain_content, hashed_content):
    return hashing_context.verify(plain_content, hashed_content)


def hash_content(content):
    return hashing_context.hash(content)
