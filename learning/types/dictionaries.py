# https://docs.python.org/3/library/stdtypes.html#mapping-types-dict
def dicts():

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

    # how many entries?
    len(ping_pong_wins)

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


