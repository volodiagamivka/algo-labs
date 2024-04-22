def search_idx_rabbin_karp(needle, haystack):
    n = len(haystack)
    m = len(needle)
    base = 11
    divisor = 21

    hash_of_needle = 0
    hash_of_haystack = 0

    for i in range(m):
        hash_of_needle += ord(needle[i]) * (base ** (m - i - 1)) % divisor
        hash_of_haystack += ord(haystack[i]) * (base ** (m - i - 1)) % divisor

    for i in range(n - m - 1):
        if hash_of_haystack % divisor == hash_of_needle % divisor:
            if haystack[i : i + m] == needle:
                return i
        if i < n - m:
            hash_of_haystack = (
                hash_of_haystack - ord(haystack[i]) * (base ** (m - 1))
            ) * base + ord(haystack[i + m]) % divisor

    return "Не знайдено індексів входження"
