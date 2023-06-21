book = { }
book['tom'] = {
    'name': 'tom',
    'address': '1 red street, NY',
    'phone': 9898989898
}
book['bob'] = {
    'name': 'bob',
    'address': '1 green street, NY',
    'phone': 234234234
}

import json
s = json.dumps(book)
with open('D://DATA Science//book.txt', 'w') as f:
    f.write(s)