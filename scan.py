def scan(requests, head_start, disk_size, direction='right'):
    requests = sorted(requests)
    seek_sequence = []
    total_seek_time = 0
    current_position = head_start

    if direction == 'right':
        right = [r for r in requests if r >= head_start]
        left = [r for r in requests if r < head_start][::-1]
    else:
        right = [r for r in requests if r > head_start]
        left = [r for r in requests if r <= head_start][::-1]
        right, left = left, right

    for r in right:
        seek_sequence.append(r)
        total_seek_time += abs(current_position - r)
        current_position = r

    if direction == 'right' and current_position != disk_size - 1:
        total_seek_time += abs(current_position - (disk_size - 1))
        current_position = disk_size - 1
    elif direction == 'left' and current_position != 0:
        total_seek_time += abs(current_position - 0)
        current_position = 0

    for r in left:
        seek_sequence.append(r)
        total_seek_time += abs(current_position - r)
        current_position = r

    return seek_sequence, total_seek_time
