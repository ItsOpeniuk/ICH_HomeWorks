def find_longest_word(data: list) -> iter:
  return max(data, key=len)


if __name__ == '__main__':
    data = ['honey', 'def', 'apple', '']
    result = find_longest_word(data)
    print(result)