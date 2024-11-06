def acronym(s):
    acronym = ''.join([kata[0].upper() for kata in s.split()])
    print(acronym)
acronym('mahkamah konstitusi')