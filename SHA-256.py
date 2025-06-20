import hashlib

def get_sha256_hash(text):
    """Returns the SHA-256 hash of the given text."""
    encoded_text = text.encode()
    hash_object = hashlib.sha256(encoded_text)
    return hash_object.hexdigest()

def main():
    print(" SHA-256 Hash Generator")
    print("----------------------------")
    
    user_input = input("Enter any word, number, or sentence: ")
    hash_result = get_sha256_hash(user_input)
    
    print("\nHA-256 Hash:")
    print(hash_result)

if __name__ == "__main__":
    main()

