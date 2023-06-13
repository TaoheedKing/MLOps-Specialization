

def test_long_dictionaries():
  result = {'key': 'value', 'lastname': 'king', 'firstname': 'taoheed'}
  expected = {'key': 'value', 'lastame': 'king', 'firstname': 'taoheed'}
  assert result == expected