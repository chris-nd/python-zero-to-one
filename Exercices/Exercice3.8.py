import chardet

def detect_encoding(b: bytes):
    # Essayer différents encodages
    encodings = ['ascii', 'utf-8', 'latin-1', 'cp1252']
    
    for encoding in encodings:
        try:
            s = b.decode(encoding)
            if encoding == 'ascii' and s.isascii():
                return "ASCII"
            return encoding.upper()
        except UnicodeDecodeError:
            continue
    
    return "Encodage inconnu"

print(detect_encoding(b'Hello'))
print(detect_encoding(b'\xc3\xa9t\xc3\xa9'))

# 2ème approche
# def detect_encoding(b: bytes):
#     result = chardet.detect(b)
#     return result['encoding']

# print(detect_encoding(b'Hello'))
# print(detect_encoding(b'\xc3\xa9t\xc3\xa9'))
