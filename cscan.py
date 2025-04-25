def c_scan(requests, head_start, disk_size):
    requests = sorted(requests)
    seek_sequence = []
    total_seek_time = 0
    current_position = head_start

    right = [r for r in requests if r >= head_start]
    left = [r for r in requests if r < head_start]

    for r in right:
        seek_sequence.append(r)
        total_seek_time += abs(current_position - r)
        current_position = r

    if current_position != disk_size - 1:
        total_seek_time += abs(current_position - (disk_size - 1))
        current_position = 0
        total_seek_time += disk_size - 1  # move from end to start (wrap around)

    for r in left:
        seek_sequence.append(r)
        total_seek_time += abs(current_position - r)
        current_position = r

    return seek_sequence, total_seek_time
