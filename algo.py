def find_connected_airports(airport, routes, result):
    immidiate_connections = [
        route for route in routes if route[0] == airport and route[1] not in result]
    if len(immidiate_connections) > 0:
        for _, dest in immidiate_connections:
            result.append(dest)
            find_connected_airports(dest, routes, result)

    unique_result = set([item for item in result if item != airport])
    return unique_result


def find_adjs(routes):
    adjs = {}
    for route in routes:
        adjs[route[0]] = [
            route[1]] if route[0] not in adjs else adjs[route[0]] + [route[1]]
    return adjs


def find_connections(airports, routes, starting_airport):
    connections_by_airport = [(airport, find_connected_airports(
        airport, routes, [])) for airport in airports if airport != starting_airport]

    required_connections_count = 0
    new_connections = {}
    airports_covered = set()
    airports_set = set(airports)

    while airports_covered != airports_set:
        airport_with_max_connection = max(
            connections_by_airport, key=lambda c: len(c[1] - airports_covered))
        connections_by_airport.remove(airport_with_max_connection)

        if len(airport_with_max_connection[1] - airports_covered) > 0 and len(airport_with_max_connection[1] - set(new_connections.keys())) > 0:
            required_connections_count += 1
            new_connections[airport_with_max_connection[0]
                            ] = airport_with_max_connection[1]
            airports_covered |= set(
                [airport_with_max_connection[0]]) | airport_with_max_connection[1]

    return required_connections_count, new_connections


def walk_routes(from_airport, adj_map, walked_airports=None):
    walked_airports = walked_airports if walked_airports is not None else {}
    airport_routes = adj_map[from_airport] if from_airport in adj_map else []
    for destination_airport in airport_routes:
        if destination_airport not in walked_airports:
            walked_airports[destination_airport] = True
            walk_routes(destination_airport, adj_map, walked_airports)
    return walked_airports


def find_airport_with_max_unwalked_routes(airports, walked_airports, adjs):
    airports_set = set(airports)
    walked_airports_set = set(walked_airports.keys())
    for index, airport in enumerate(airports_set - walked_airports_set):
        if index == 0 or len(set(adjs[airport]) - walked_airports_set) > len(set(adjs[airport_with_max_routes]) - walked_airports_set):
            airport_with_max_routes = airport
    return airport_with_max_routes


def find_new_connections(airports, routes, starting_airport):
    new_connections = []
    adjs = find_adjs(routes)
    airports_with_no_inbound = set(
        airports) - set([item for l in adjs.values() for item in l])
    new_connections.extend(list(airports_with_no_inbound))
    walked_airports = {}
    walked_airports[starting_airport] = True

    for name in airports_with_no_inbound:
        walked_airports = {**walked_airports, **
                           walk_routes(name, adjs, walked_airports)}

    airports_with_inbounds = set(airports) - airports_with_no_inbound
    while set(walked_airports.keys()) != airports_with_inbounds:
        airport_with_max_adj_unwalked_routes = find_airport_with_max_unwalked_routes(
            airports, walked_airports, adjs)
        walked_airports = {**walked_airports, **
                           walk_routes(airport_with_max_adj_unwalked_routes, adjs, walked_airports)}
        new_connections.append(airport_with_max_adj_unwalked_routes)

    return new_connections


def main():
    airports = (
        'TLV', 'BGI', 'CDG', 'DEL', 'DOH', 'DSM', 'EWR', 'EYW', 'HND', 'ICN',
        'JFK', 'LGA', 'LHR', 'ORD', 'SAN', 'SFO', 'SIN', 'BUD'
    )

    routes = (
        ('DSM', 'ORD'),
        ('ORD', 'BGI'),
        ('BGI', 'LGA'),
        ('SIN', 'CDG'),
        ('CDG', 'SIN'),
        ('CDG', 'BUD'),
        ('DEL', 'DOH'),
        ('DEL', 'CDG'),
        ('TLV', 'DEL'),
        ('EWR', 'HND'),
        ('HND', 'ICN'),
        ('HND', 'JFK'),
        ('ICN', 'JFK'),
        ('JFK', 'LGA'),
        ('EYW', 'LHR'),
        ('LHR', 'SFO'),
        ('SFO', 'SAN'),
        ('SFO', 'DSM'),
        ('SAN', 'EYW')
    )

    # print(adjs)
    starting_airport = 'LGA'
    print(find_new_connections(airports, routes, starting_airport))
    # new_connections_count, connections = find_connections(
    #     airports, routes, starting_airpairport_with_max_adj_unwalked_routesort)
    # print(f'{new_connections_count} connections are required to {", ".join(list(connections.keys()))} airports')


if __name__ == '__main__':
    main()
