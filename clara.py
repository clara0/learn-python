# verify email address - @ & . at end


def verifyEmail(myEmail):
    twoParts = myEmail.split('@')
    invalidSymbols = '!~`#$%^&*()-+={[}]|\\:;"\'<,>?/ '
    domain = twoParts[-1]
    valid = False

    if len(twoParts) != 2:
        valid = False
    elif '.' in domain and '.' is not domain[-1]:
        valid = True

    for i in myEmail:
        if i in invalidSymbols:
            valid = False
            break

    return valid


while True:
    email = input('Enter an email: ').strip()
    if email == '':
        continue

    x = verifyEmail(email)
    print(f'{email} is a valid email address? {x}')


