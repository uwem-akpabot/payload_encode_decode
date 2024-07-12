import base64

def encode_payload(payload, salt_key, salt_index):
    # Encode the payload with a salt key and index into a base64 value.

    if not isinstance(payload, str) or not isinstance(salt_key, str):
        raise TypeError("Both payload and salt key must be strings.")
    if not isinstance(salt_index, int) or salt_index < 0 or salt_index > len(payload):
        raise ValueError("Salt index must be a non-negative integer within the payload length.")
    
    # Insert the salt key into the payload at the specified index
    salted_payload = payload[:salt_index] + salt_key + payload[salt_index:]
    
    # Encode the salted payload in base64
    base64_encoded = base64.b64encode(salted_payload.encode('utf-8')).decode('utf-8')
    
    return base64_encoded

def decode_payload(encoded_payload, salt_key, salt_index):
    # Decode the base64 encoded payload using the salt key and index.
    
    if not isinstance(encoded_payload, str) or not isinstance(salt_key, str):
        raise TypeError("Both encoded payload and salt key must be strings.")
    if not isinstance(salt_index, int) or salt_index < 0:
        raise ValueError("Salt index must be a non-negative integer.")
    
    # Decode the base64 encoded payload
    salted_payload = base64.b64decode(encoded_payload).decode('utf-8')
    
    # Check if the salt key is at the specified index
    if salted_payload[salt_index:salt_index + len(salt_key)] != salt_key:
        raise ValueError("Incorrect salt key or salt index.")
    
    # Remove the salt key from the salted payload at the specified index
    original_payload = salted_payload[:salt_index] + salted_payload[salt_index + len(salt_key):]
    
    return original_payload

# Example usage
payload = "JobDemo"
salt_key = "567"
salt_index = 5

encoded_payload = encode_payload(payload, salt_key, salt_index)
print("Encoded Payload:", encoded_payload)

# Correct decoding
try:
    decoded_payload = decode_payload(encoded_payload, salt_key, salt_index)
    print("Decoded Payload:", decoded_payload)
except ValueError as e:
    print("Decoding failed:", e)

# Incorrect decoding with wrong salt key
try:
    decoded_payload = decode_payload(encoded_payload, "456", salt_index)
    print("Decoded Payload with wrong salt key:", decoded_payload)
except ValueError as e:
    print("Decoding failed with wrong salt key:", e)

# Incorrect decoding with wrong salt index
try:
    decoded_payload = decode_payload(encoded_payload, salt_key, 3)
    print("Decoded Payload with wrong salt index:", decoded_payload)
except ValueError as e:
    print("Decoding failed with wrong salt index:", e)




# import base64

# def encode_payload(payload, salt_key, salt_index):
#     if not isinstance(payload, str) or not isinstance(salt_key, str):
#         raise TypeError("Both payload and salt key must be strings.")
#     if not isinstance(salt_index, int) or salt_index < 0 or salt_index > len(payload):
#         raise ValueError("Salt index must be a non-negative integer within the payload length.")
    
#     # Insert the salt key into the payload at the specified index
#     salted_payload = payload[:salt_index] + salt_key + payload[salt_index:]
    
#     # Encode the salted payload in base64
#     base64_encoded = base64.b64encode(salted_payload.encode('utf-8')).decode('utf-8')
    
#     return base64_encoded

# def decode_payload(encoded_payload, salt_key, salt_index):
#     if not isinstance(encoded_payload, str) or not isinstance(salt_key, str):
#         raise TypeError("Both encoded payload and salt key must be strings.")
#     if not isinstance(salt_index, int) or salt_index < 0:
#         raise ValueError("Salt index must be a non-negative integer.")
    
#     # Decode the base64 encoded payload
#     salted_payload = base64.b64decode(encoded_payload).decode('utf-8')
    
#     # Remove the salt key from the salted payload at the specified index
#     original_payload = salted_payload[:salt_index] + salted_payload[salt_index + len(salt_key):]
    
#     return original_payload

# # e.g.
# payload = "PythonJobDemo"
# salt_key = "999"
# salt_index = 5

# encoded_payload = encode_payload(payload, salt_key, salt_index)
# print("Encoded Payload:", encoded_payload)

# decoded_payload = decode_payload(encoded_payload, salt_key, salt_index)
# print("Decoded Payload:", decoded_payload)
