def files():
    import requests
    yawl_response = requests.get('https://raw.githubusercontent.com/elasticdog/yawl/master/yawl-0.3.2.03/word.list')

    if yawl_response.status_code == requests.codes.ok:
        yet_another_word_list = yawl_response.text

        # Write a file (default mode is r for read, a - appending write)
        # Specify encoding if chance that file will be read on different machine
        fout = open('io/yawl.txt', mode='w', encoding='utf-8')
        fout.write(yet_another_word_list)
        fout.close()
    else:
        print('Got response code {} when trying to retrieve yawl'.format(yawl_response.status_code))

    # still in scope even though it was in body of if statement
    yet_another_word_list[:2]

    fin = open('io/yawl.txt', encoding='utf-8')
    # takes number of chars to read arg
    wordsStr = fin.read()
    fin.close()

    words = wordsStr.split('\n')