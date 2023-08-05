import re

class validdocbr(object):
    def cpf(self, cpf):
        common_error = ["00000000000", 
                        "1111111111", 
                        "22222222222", 
                        "33333333333", 
                        "44444444444", 
                        "55555555555", 
                        "66666666666", 
                        "77777777777", 
                        "88888888888", 
                        "99999999999"]
        cpf_string = re.sub('[^A-Za-z0-9]', "", cpf).strip()
        valid = True

        if cpf_string in common_error: 
            valid = False

        if cpf_string == "": 
            valid = False

        try:
            float(cpf_string)
        except ValueError:
            valid = False

        if valid:
            check_count = 10
            dig_1 = 0
            sum_1 = 0
            for n in cpf_string[0:9]:
                sum_1 += (int(n) * check_count)
                check_count -= 1    

            dig = 11 - (sum_1 % 11)

            if dig >= 10:
                dig_1 = 0
            else:
                dig_1 = dig

            if dig_1 != int(cpf_string[9]):
                valid = False

        if valid:
            check_count = 11
            dig_2 = 0
            sum_2 = 0

            for n in cpf_string[0:10]:
                sum_2 += (int(n) * check_count)
                check_count -= 1

            dig = 11 - (sum_2 % 11)

            if dig >= 10:
                dig_2 = 0
            else:
                dig_2 = dig

            if dig_2 != int(cpf_string[10]):
                valid = False
        return valid

    def cnpj(self, cnpj):
        common_error = ["00000000000000", 
                        "1111111111111", 
                        "22222222222222", 
                        "33333333333333", 
                        "44444444444444", 
                        "55555555555555", 
                        "66666666666666", 
                        "77777777777777", 
                        "88888888888888", 
                        "99999999999999"]


        cnpj_string = re.sub('[^A-Za-z0-9]', "", cnpj).strip()
        valid = True


        if cnpj_string in common_error: 
            valid = False

        if cnpj_string == "": 
            valid = False

        try:
            float(cnpj_string)
        except ValueError:
            valid = False
        
        if valid:
            cnpj_to_validate = cnpj_string[0:12]
            cnpj_to_validate_invert = cnpj_to_validate[::-1]
            cycle = [2, 3, 4, 5, 6, 7, 8, 9]
            max_lenght = len(cycle)
            tick = 0
            sum_1 = 0
            dig_1 = 0

            for num in cnpj_to_validate_invert:
                int_num = int(num)
                relative_number = int_num * cycle[tick]
                sum_1 += relative_number
                    
                if tick == max_lenght - 1:
                    tick = 0
                else:
                    tick += 1

            dig = 11 - (sum_1 % 11)

            if dig >= 10:
                dig_1 = 0
            else:
                dig_1 = dig

            if dig_1 != int(cnpj_string[12]):
                valid = False

        if valid:
            cnpj_to_validate = cnpj_string[0:13]
            cnpj_to_validate_invert = cnpj_to_validate[::-1]
            cycle = [2, 3, 4, 5, 6, 7, 8, 9]
            max_lenght = len(cycle)
            tick = 0
            sum_2 = 0
            dig_2 = 0

            for num in cnpj_to_validate_invert:
                int_num = int(num)
                relative_number = int_num * cycle[tick]
                sum_2 += relative_number
                
                if tick == max_lenght - 1:
                    tick = 0
                else:
                    tick += 1

            dig = 11 - (sum_2 % 11)

            if dig >= 10:
                dig_2 = 0
            else:
                dig_2 = dig

            if dig_2 != int(cnpj_string[13]):
                valid = False
        
        return valid