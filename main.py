import base64

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_'


def get_short_code_from_media_id(media_id):
    media_id_bytes = media_id.to_bytes(9, 'big')
    b64_encoded = base64.b64encode(media_id_bytes, b'-_')
    b64_decoded = b64_encoded.decode()
    short_code = b64_decoded.replace('A', ' ').lstrip().replace(' ', 'A')

    return short_code


def get_media_id_from_short_code(short_code):
    media_id = 0

    for one_letter in short_code:
        media_id_64 = media_id * 64
        alphabet_index = ALPHABET.index(one_letter)
        media_id = media_id_64 + alphabet_index

    return media_id
