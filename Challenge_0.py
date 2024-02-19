message = ("Naljnl, Pnrfne jnf n fxvyyrq pbzzhavpngbe, naq ur hfrq n inevrgl bs zrgubqf gb xrrc uvf zrffntrf frperg "
           "sebz uvf rarzvrf. Bar bs gurfr zrgubqf jnf gur Pnrfne pvcure, n fvzcyr grpuavdhr gb boshfpngr "
           "pbzzhavpngvbaf. SYNT{ebgngr_gung_nycunorg}")


def decrypted_message(encrypted, shift):
    decrypted = ''
    for char in encrypted:
        if 65 <= ord(char) <= 90:
            decrypted_char = chr((ord(char) + shift - 65) % 26 + 65)
            decrypted += decrypted_char
        elif 97 <= ord(char) <= 122:
            decrypted_char = chr((ord(char) + shift - 97) % 26 + 97)
            decrypted += decrypted_char
        else:
            decrypted += char

    return decrypted


for i in range(26):
    print(i, decrypted_message(message, i))


print(ord('A'), ord('Z'))
print(ord('a'), ord('z'))
