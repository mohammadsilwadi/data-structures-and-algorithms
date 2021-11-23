from hash_table import HashTable

def left_join(h1,h2):
    return_date =[]
    for value in h1._HashTable__buckets:
        if value:
            for item in value:
                if h2.contains(item[0]):
                    h2_value = h2.get(item[0])
                    return_date.append([item[0],item[1],h2_value])
                else:
                    return_date.append([item[0],item[1],None])
    return return_date


if __name__ == "__main__":
    hash1 = HashTable()
    hash1.add('good','fine')

    hash2 = HashTable()
    hash2.add('good','bad')


    actual = left_join(hash1, hash2)
    print(actual)
