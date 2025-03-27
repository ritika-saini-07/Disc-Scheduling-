def fcfs(requests, head_start):
    seek_sequence = []
    total_seek_time = 0
    current_position = head_start

    for request in requests:
        seek_sequence.append(request)
        total_seek_time += abs(request - current_position)
        current_position = request

    return seek_sequence, total_seek_time
