def create_savings_data_file(path):
    print('# Txt-savings-data.py is open')
    try:
        savings_data_file = open(path, 'r')
        savings_data_file.close()

        print("# data_file: TxtSavingsData is done")

    except:
        savings_data_file = open(path, 'a+')
        savings_data_file.close()

        print("# data_file: TxtSavingsData is created")

