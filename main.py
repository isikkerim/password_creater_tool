import optparse
import itertools
import os


"""byte türündeki dosya boyutunu  mb-gb-tb-pt cinsinden gösterir """
def convert_bytes(size):

    # 1 MB = 1024 * 1024 bytes
    # 1 GB = 1024 * 1024 * 1024 bytes
    # 1 TB = 1024 * 1024 * 1024 * 1024 bytes
    # 1 PB = 1024 * 1024 * 1024 * 1024 * 1024 bytes

    power = 2**10       # 1024
    n = 0
    power_labels = {0 : '', 1: 'KB', 2: 'MB', 3: 'GB', 4: 'TB', 5: 'PB'}
    while size > power:
        size /= power
        n += 1
    return f"{size:.2f} {power_labels[n]}"

""" girilen değişkenlere uygun olarak şifre kombinasyonları oluşturur  """
def setPasswords(min_length, max_length, char, output):
    characters = char
    passwords = []

    for length in range(int(min_length), int(max_length) + 1):
        passwords.extend([''.join(password) for password in itertools.product(characters, repeat=length)])

    if output:
        with open(output, 'w') as file:
            for password in passwords:
                file.write(password + '\n')

        # Dosyanın boyutunu hesapla ve yazdır
        file_size = os.path.getsize(output)
        print(f"Şifrelerin yazıldığı dosyanın boyutu: {convert_bytes(file_size)}")

""" user input alınmasını sağlar """
def get_input():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-n", "--min_length", dest="min_length", help="min password length (required) ")
    parse_object.add_option("-x", "--max_length", dest="max_length", help="max password length  (required)")
    parse_object.add_option("-c", "--char", dest="char", help="add char to password  (required)")
    parse_object.add_option("-o", "--output", dest="output", help="output file name (optional)")
    (options, args) = parse_object.parse_args()

    if not (options.min_length and options.max_length and options.char):
        parse_object.error("bütün gerekli argumanları girmelisiniz! ")

    setPasswords(options.min_length, options.max_length, options.char, options.output)


get_input()
