# https://docs.python.org/3/library/stdtypes.html#mapping-types-dict
def dicts():

    empty_dict = {}

    # No order! Mutable! Can have keys, values of different types.
    # keys must be hashable (__hash__(self))
    ping_pong_wins = {'Chang': 98, 'Steve': 82, 'Amit': 1, 'Alex': 10}
    ping_pong_wins['Chang']

    # He won another - update value
    ping_pong_wins['Chang'] += 1

    # Add an element if key does not exist
    ping_pong_wins['Troy'] = 70

    # Alex left - remove from dict
    # pop returns value, del ping_pong_wins['Alex'] - no return value
    alex_score = ping_pong_wins.pop('Alex')

    # Guard against missing keys!
    # m_score = ping_pong_wins['Markus'] # KeyError: 'Markus'

    # use default value for missing key - does not update original dict!
    m_score = ping_pong_wins.get('Markus', 0)

    # Markus won a game - update ping_pong_wins!
    if 'Markus' in ping_pong_wins:
        ping_pong_wins['Markus'] += 1
    else:
        ping_pong_wins['Markus'] = 1

    # Use setdefault to set a default for a key, if key exists - no change
    players = ['Troy', 'Chang', 'Ryan', 'Amit', 'Steve', 'Markus', 'Matt']

    for player in players:
        ping_pong_wins.setdefault(player, 0)

    # Value for Troy did not change - still 70
    ping_pong_wins['Troy']

    # Matt is 0 (we started while he was on vacation)
    ping_pong_wins['Matt']

    # how many entries?
    len(ping_pong_wins)

    # list - otherwise dict_keys, dict_values, dict_items
    names = list(ping_pong_wins.keys())
    scores = list(ping_pong_wins.values())
    entries_as_tuples = list(ping_pong_wins.items())

    # sort by key
    sorted(ping_pong_wins.items())

    # sorts values - lowest to highest
    sorted(ping_pong_wins.items(), key=lambda kv: kv[1])

    # sorts values - highest to lowest
    sorted(ping_pong_wins.items(), key=lambda kv: kv[1], reverse=True)

    # start over for the next season
    ping_pong_wins.clear()

    # dict as an informal way of creating records
    record_1 = {'first': 'Foo', 'last': 'Bar', 'age': 42}
    record_1['age']

    # replacing update
    last_viewed = {'Bob': 'Black Mirror', 'Jane': 'Longmire', 'Joe': 'Batman'}
    last_hour_update = {'Bob': 'Victoria', 'Joe': 'Superman', 'Alice': 'Babylon Berlin'}
    # overwrite existing keys with new entries in last_hour_update - no update for Jane
    last_viewed.update(last_hour_update)

    # dictionary for comprehension - iterate over items
    # Instead of just movie, add (movie,count) tuple to key
    movie_counts = { key: (value, 1) for (key,value) in last_viewed.items() }

    # Using a dictionary for letter frequency counts
    paragraph = "ask not what your country can do for you"
    letter_freq = {}
    for c in paragraph:
        if c.isalpha():
            if not c in letter_freq:
                letter_freq[c] = 1
            else:
                letter_freq[c] += 1

    # Making a dict by zipping two lists and creating 2-tuples
    keys = ['a','b','c']
    values = [1, 2, 3]

    kvs_zip = zip(keys, values)
    kvs_list = list(kvs_zip)

    kv_dict = dict(kvs_list)


