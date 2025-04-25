def look(requests, head_start, direction='right'):
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

    for r in right + left:
        seek_sequence.append(r)
        total_seek_time += abs(current_position - r)
        current_position = r

    return seek_sequence, total_seek_time
