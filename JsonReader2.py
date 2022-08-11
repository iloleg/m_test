import json

with open('data.json', 'r') as read_file:
    read_data = json.load(read_file)
    data = {}
    for x in read_data:
        movie = (x['name'])
        ratio = float(x["rating"])
        starts = x['stars']
        for star_list in starts.split(','):
            name = star_list.strip()
            if name in data:
                ratio_u = data[name][0] + ratio
                count = data[name][1] + 1
                data[name] = (ratio_u, count)
            else:
                data[name] = (ratio, 1)

    sorted_data = sorted(data.items(), key=lambda item: item[1])
    table_data = []
    for key, val in sorted_data:
        if val[1] >= 2:
            table_data.append((key, str(val[1]), "{:.2f}".format(val[0] / val[1])))

    for row in table_data: # reformat to table style
        print("Star Name: {: <20}  Movies: {: <3} AVG Rating: {: >3}".format(*row))
