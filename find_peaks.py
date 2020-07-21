def pick_peaks(arr):
    """
    Find the peaks in array of heights - in case of a plaleau peak, return the
    position of the first occurence, i.e for [1,2,2,2,1] - the return value
    would be pos: [1], peaks:[2]. The first and last element cannot be a peak.
    See also:
    https://www.codewars.com/kata/5279f6fe5ab7f447890006a7/solutions/python
    """
    res = {
        'pos': [],
        'peaks': []
    }
    if not arr or len(arr) == 1:
        return res
    curr_peak, curr_pos = [], []
    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            curr_peak, curr_pos = [arr[i]], [i]
        elif arr[i] < arr[i-1]:  # peak found
            res['pos'] += curr_peak
            res['peaks'] += curr_pos
            curr_peak, curr_pos = [], []
    return res


print(pick_peaks([1, 2, 3, 6, 4, 1, 2, 3, 2, 1]))
