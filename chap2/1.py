def sort_by_distance(data):
    return data['distance']


def main():
    files_numb = 0
    filesbeing_read = []
    more_than_once = []
    total_distance = 0
    number_of_line = 0
    a = open('f2016_cs8_<hac105>_a3.data.output.csv', 'w')
    a.write('/Users/macbookpro/PycharmProjects/CS0008-f2016/Ch1-Ex3/f2016_cs8_a3.data.1.csv\n')
    a.write('/Users/macbookpro/PycharmProjects/CS0008-f2016/Ch1-Ex3/f2016_cs8_a3.data.2.csv\n')
    a.write('/Users/macbookpro/PycharmProjects/CS0008-f2016/Ch1-Ex3/f2016_cs8_a3.data.3.csv\n')
    a.close()
    y = open('monster input file.cvs', 'r')
    for x in y:
        x = x[0:-1]
        t = open(x, 'r')
        for line in t:
            number_of_line += 1
            line = line.rstrip()
            line = line.split(',')
            try:
                line[1] = float(line[1])
                total_distance += line[1]
            except:
                y = 0
            k = 0
            for s in filesbeing_read:
                if line[0] in s.values():
                    k = 1
                    try:
                        d1 = s.get('distance', 'Error')
                        value = d1 + line[1]
                        s['distance'] = float(value)
                        if line[0] in more_than_once:
                            y = 0
                        else:
                            more_than_once.append(line[0])
                    except:
                        y = 0
            if k == 0:
                new_data = {}
                new_data['name'] = line[0]
                new_data['distance'] = line[1]
                filesbeing_read.append(new_data)
    filesbeing_read.sort(key=sort_by_distance)
    total_participant = number_of_line - 3 - len(more_than_once)

    print('Number of Input files read', 3)
    print('Total number of lines read', number_of_line - 3)
    print('total distance run ', total_distance)
    date = filesbeing_read[-2]
    print('max distance run', date['distance'])
    print('name', date['name'])
    date1 = filesbeing_read[0]
    print('min distance run', date1['distance'])
    print('name', date1['name'])
    print('Total number of participants', total_participant)
    print('participants with multiple records', len(more_than_once))


main()
