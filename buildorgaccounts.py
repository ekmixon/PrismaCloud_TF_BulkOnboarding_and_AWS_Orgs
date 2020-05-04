import sys

read_file_ids = "awsids.txt"
read_file_configs = "awsconfig.txt"
print_file = "awsaccounts.csv"

def print_to_csv(id_file, config_file, print_file_name):

    try:

        with open(id_file, 'r') as file_1:

            file_content_1 = file_1.read()

            print("read file content from " + id_file)

        if not file_content_1:

            print("no data in ID file")

            return

        with open(config_file, 'r') as file_2:

            file_content_2 = file_2.read()

            print("read file content from " + config_file)

        if not file_content_2:

            print("no data in config file")

            return

        with open(print_file_name, 'w') as csv_file:

            acct_file = []

            id_list = file_content_1.splitlines()

            config_list = file_content_2.splitlines()



            csv_file.write("accountId,externalId,groupIDs,name,roleArn\n")



            for x in range(len(config_list)):

                if config_list[x].strip():

                    increment = 1

                    if config_list[x][config_list[x].find('=') + 1: config_list[x].find('=') + 2:] == ' ':

                        increment = 2



                    config_list[x] = config_list[x][config_list[x].find('=') + increment::]



            for x in range(len(id_list)):

                if id_list[x].strip():

                    id_list[x] = ''.join([i for i in id_list[x] if i.isdigit()])

                    col_e = "arn:aws:iam::" + id_list[x] + ":role/PrismaCloudReadOnlyRoleNEW"

                    acct_file.append(id_list[x] + "," + config_list[0] + "," + config_list[1] + "," + id_list[x] + "," + col_e)



            list_to_str = '\n'.join(map(str, acct_file))

            csv_file.write(list_to_str)

            csv_file.close()

            print("wrote file content to " + print_file_name)

    except IOError as e:

        print("I/O error({0}): {1}".format(e.errno, e.strerror))

    except:

        print("Unexpected error:", sys.exc_info()[0])





print_to_csv(read_file_ids, read_file_configs, print_file)
