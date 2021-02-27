import random

if __name__ == '__main__':
    """ the seeder module creates sample data using the given template
        the template is in the seeder_data file,
        it specifies the attributes and values our data has

        output: data.csv
    """

    # read template
    with open("Cloud/storage/data/seeder_data_template.csv", "r") as file_object:
        seeder = file_object.read().split('\n')

    with open("Cloud/storage/data/data.csv", "a") as file_object:
        # for each row in template, create data in random numbers
        # and write the row in a file
        for i in seeder:
            temp = i.split(',')

            for i in range(random.randint(25, 45)):
                file_object.write(temp[0] +',')

                if temp[1] == 'low':
                    file_object.write(str(random.randint(1, 100)) +',')
                elif temp[1] == 'high':
                    file_object.write(str(random.randint(1, 300)) +',')

                if temp[2] == 'low':
                    file_object.write(str(random.randint(1, 10)) +',')
                elif temp[2] == 'high':
                    file_object.write(str(random.randint(11, 30)) +',')

                file_object.write(temp[3] +',')

                file_object.write(temp[4])

                file_object.write('\n')

    # read the whole data to manipulate
    with open("Cloud/storage/data/data.csv", "r") as file_object:
        array = file_object.read().split('\n')

    random.shuffle(array)

    array2 = ''
    for i in array:
        array2 += i
        array2 += '\n'

    with open("Cloud/storage/data/data.csv", "w") as file_object:
        array = file_object.write(array2)