def search_idx_rabbin_karp(needle, haystack):
    n = len(haystack)
    m = len(needle)
    q = 10
    hash_of_needle = 0
    hash_of_haystack = 0

    for i in range(m):
        hash_of_needle += ord(needle[i]) * (q ** (m - i - 1))
        hash_of_haystack += ord(haystack[i]) * (q ** (m - i - 1))

    for i in range(n - m + 1):
        if hash_of_haystack == hash_of_needle:
            if haystack[i : i + m] == needle:
                return i
        if i < n - m:
            hash_of_haystack = (
                hash_of_haystack - ord(haystack[i]) * (q ** (m - 1))
            ) * q + ord(haystack[i + m])

    return "Не знайдено індексів входження"
