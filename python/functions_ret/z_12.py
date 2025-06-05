def crypt(alphabet, message, key):
    mod = len(alphabet)
    encrypted = []
    key_repeated = (key * ((len(message) // len(key)) + 1))[:len(message)]
    
    for m_char, k_char in zip(message, key_repeated):
        m_idx = alphabet.index(m_char)
        k_idx = alphabet.index(k_char)
        encrypted_idx = (m_idx + k_idx) % mod
        encrypted.append(alphabet[encrypted_idx])
    
    return ''.join(encrypted)


def decrypt(alphabet, message, key):
    mod = len(alphabet)
    decrypted = []
    key_repeated = (key * ((len(message) // len(key)) + 1))[:len(message)]
    
    for m_char, k_char in zip(message, key_repeated):
        m_idx = alphabet.index(m_char)
        k_idx = alphabet.index(k_char)
        decrypted_idx = (m_idx - k_idx) % mod
        decrypted.append(alphabet[decrypted_idx])
    
    return ''.join(decrypted)