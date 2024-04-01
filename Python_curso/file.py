# import main
# from test.folder import test_file
from bank_account_variables import money_slips

# print(main.accounts_list)
# main.clear()
# print('qualquer coisa')
# print(test_file.variavel)
import os

# # BASE_PATH = os.path.dirname(os.path.abspath(__file__))
# # # print(BASE_PATH)
# # file = open(BASE_PATH + '/_file_test.dat', 'r')
# # print(file.read())
# # # file.write('school of net')
# # file.close()


# # file = open(BASE_PATH + '/_file_test.dat', 'r')
# # print(file.read())
# # file.close()

# import os

# # Obtém o caminho absoluto do arquivo atual
BASE_PATH = os.path.dirname(os.path.abspath(__file__))
print(BASE_PATH)

# # Abre o arquivo atual para leitura
# with open(__file__, 'r') as file:
#     # Lê o conteúdo do arquivo e o imprime
#     print(file.read())
#     file.close()

def open_file_bank(mode):
    return open(BASE_PATH + '/_bank_file.dat', mode)


def write_money_slips(file):
    for money_bill, value in money_slips.items():
        file.write(money_bill+ '='+ str(value) + ';')