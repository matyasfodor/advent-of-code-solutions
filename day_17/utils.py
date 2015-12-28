def get_variations(volume_left, original_containers):
    containers = original_containers[:]
    if volume_left == 0:
        yield []
        return

    if len(containers) == 0:
        return

    container = containers.pop(0)

    for variation in get_variations(volume_left, containers):
        yield variation

    decreased_value = volume_left - container
    if decreased_value >= 0:
        for variation in get_variations(decreased_value, containers):
            yield [(container, len(containers))] + variation
    return
