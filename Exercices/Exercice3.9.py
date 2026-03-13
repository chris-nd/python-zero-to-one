import base64

def encode_bas64(s):
    return base64.b64encode(s.encode())

print(encode_bas64("Hello"))
print(encode_bas64("Python"))

# Approche manuelle
# def encode_base64(s):
#     base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
#     data = s.encode('utf-8')
#     result = ""
    
#     # Traiter 3 octets à la fois
#     i = 0
#     while i < len(data):
#         # Prendre 3 octets (ou moins si fin)
#         byte1 = data[i]
#         byte2 = data[i+1] if i+1 < len(data) else 0
#         byte3 = data[i+2] if i+2 < len(data) else 0
        
#         # Convertir en 24 bits
#         combined = (byte1 << 16) | (byte2 << 8) | byte3
        
#         # Extraire 4 groupes de 6 bits
#         result += base64_chars[(combined >> 18) & 0x3F]
#         result += base64_chars[(combined >> 12) & 0x3F]
#         result += base64_chars[(combined >> 6) & 0x3F] if i+1 < len(data) else '='
#         result += base64_chars[combined & 0x3F] if i+2 < len(data) else '='
        
#         i += 3
    
#     return result

# print(encode_base64("Hello"))
# print(encode_base64("Python"))