def solution(sizes):

    arr = [(max(w, h), min(w, h)) for w, h in sizes]

    return max(w for w, h in arr) * max(h for w, h in arr)