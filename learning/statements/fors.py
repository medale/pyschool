# https://docs.python.org/3/reference/compound_stmts.html#the-for-statement

def country_to_caps():
    countries = ['USA','France','Germany']
    capitols = ['Washington, D.C.', 'Paris', 'Berlin']

    countries_to_capitols = dict(zip(countries, capitols))
    return countries_to_capitols


def simple_for():
    countries_to_capitols = country_to_caps()

    capitols_to_countries = {}

    # We want to iterate over all items
    for k,v in countries_to_capitols.items():
        capitols_to_countries[v] = k

    # should use dictionary for comprehension
    caps_to_country = {v:k for k,v in countries_to_capitols.items()}


def find_first_match():
    numbers = ['1145', '1004', '1023', '4321', '42']

    # find first number that either start with 10 or end with 1
    match = None

    for num in numbers:
        if num.startswith('10'):
            match = num
            # break out of the closest for loop
            break
        if num.endswith('1'):
            match = num
            break

    return match


def find_all_matches():
    numbers = ['1145', '1004', '1023', '4321', '42']

    # find all numbers that either start with 10 or end with 1
    matches = []

    for num in numbers:
        if num.startswith('10'):
            matches.append(num)
            # continue with next num in numbers - skip the other if
            continue
        if num.endswith('1'):
            matches.append(num)

    return matches


def finding_primes():
    # find primes between 2 and 100
    primes = [2,3]
    for i in range(4,101):
        for div in range(2, i):
            if i % div == 0:
                break
        # execute else only if break never gets executed
        else:
            primes.append(i)

    return primes


def main():
    first_match = find_first_match()
    print(first_match)

    all_matches = find_all_matches()
    print(','.join(all_matches))

    primes = finding_primes()
    print(','.join(primes))



if __name__== "__main__":
    main()






