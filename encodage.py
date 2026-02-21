# coding: utf-8

print("Café")  # String with accented character
print(b"Caf\xc3\xa9")  # Byte string with UTF-8 encoding
print("Café".encode('utf-8'))  # Encoding string to bytes
print(b"Caf\xc3\xa9".decode('utf-8'))  # Decoding bytes to string
print("Emoji: 😊")  # String with emoji
print("Emoji: 😊".encode('utf-8'))  # Encoding emoji string to bytes
print(b"Emoji: \xf0\x9f\x98\x8a".decode('utf-8'))  # Decoding bytes to string with emoji
print("中文字符")  # String with Chinese characters
print("中文字符".encode('utf-8'))  # Encoding Chinese characters to bytes
print(b"\xe4\xb8\xad\xe6\x96\x87\xe5\xad\x97".decode('utf-8'))  # Decoding bytes to string with Chinese characters
print("Special chars: ñ, ü, å")  # String with special characters
print("Special chars: ñ, ü, å".encode('utf-8'))  #
print(b"Special chars: \xc3\xb1, \xc3\xbc, \xc3\xa5".decode('utf-8'))  # Decoding bytes to string with special characters

# Encoding special characters to bytes

print(b"Special chars: \xc3\xb1, \xc3\xbc, \xc3\xa5")
print("Special chars: ñ, ü, å".encode('utf-8'))  # Encoding special characters to bytes
print(b"Special chars: \xc3\xb1, \xc3\xbc, \xc3\xa5".decode('utf-8'))  # Decoding bytes to string with special characters
print(b"Special chars: \xc3\xb1, \xc3\xbc, \xc3\xa5")  # Encoding special characters to bytes
print("Special chars: ñ, ü, å".encode('utf-8'))  # Encoding special characters to bytes
print(b"Special chars: \xc3\xb1, \xc3\xbc, \xc3\xa5".decode('utf-8'))  # Decoding bytes to string with special