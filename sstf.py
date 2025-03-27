def sstf(requests, head_start):
    requests = requests.copy()
    seek_sequence = []
    total_seek_time = 0
    current_position = head_start

    while requests:
        nearest = min(requests, key=lambda x: abs(x - current_position))
        seek_sequence.append(nearest)
        total_seek_time += abs(nearest - current_position)
        current_position = nearest
        requests.remove(nearest)

    return seek_sequence, total_seek_time
