def dicts():

    # No order! Mutable! Can have keys, values of different types.
    # keys must be hashable (__hash__(self))
    ping_pong_scores = {'Chang': 98, 'Steve': 82, 'Amit': 1}
    ping_pong_scores['Chang']
    ping_pong_scores['Chang'] += 1

    # Add an element
    ping_pong_scores['Troy'] = 70

    # m_score = ping_pong_scores['Markus'] # KeyError: 'Markus'
    m_score = ping_pong_scores.get('Markus',0)

    # dict as an informal way of creating records
    record_1 = {'first': 'Foo', 'last': 'Bar', 'age': 42}
    record_1['age']

    # list - otherwise dict_keys, dict_values, dict_items
    names = list(ping_pong_scores.keys())
    scores = list(ping_pong_scores.values())
    entries_as_tuples = list(ping_pong_scores.items())

    # sort by key
    sorted(ping_pong_scores.items())

    # sorts values - lowest to highest
    sorted(ping_pong_scores.items(), key=lambda kv: kv[1])

    # sorts values - highest to lowest
    sorted(ping_pong_scores.items(), key=lambda kv: kv[1], reverse=True)
