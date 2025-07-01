def get_count_words(content):
    arr = content.split()
    return len(arr)

def get_count_chars(content):
    count = dict()
    for char in content:
        c = char.lower()
        if c not in count:
            count[c] = 1
        else:
            count[c] += 1

    return count

def format_count(count):
    def sort_on(items):
        return items["num"]

    arr = []
    for k, v in count.items():
        arr.append({"char": k, "num": v})
    arr.sort(reverse=True, key=sort_on)
    return arr
