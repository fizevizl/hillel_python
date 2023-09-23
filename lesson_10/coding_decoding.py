
byte_str = b'rxx3xa9sumxc3xa9'
decoded_string = byte_str.decode()
print(decoded_string)

latin_str = decoded_string.encode('Latin1')
print(latin_str)

st = latin_str.decode('Latin1')
print(st)
