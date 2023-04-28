from typing import *

class Numbers():
    def __init__(self, first_number: str, second_number: str) -> None:
        if '.' in first_number and '.' in second_number:
            self.__first_number = self.translate_float_to_binary(
                first_number)
            self.__second_number = self.translate_float_to_binary(
                second_number)
        else:
            self.__first_number_in_dicrect_code = self.translate_int_to_binary_direct_code(
                int(first_number))
            self.__second_number_in_dicrect_code = self.translate_int_to_binary_direct_code(
                int(second_number))
            self.__first_number_in_reverse_code = \
                self.translate_int_to_binary_reverse_code(
                    self.__first_number_in_dicrect_code)
            self.__second_number_in_reverse_code = \
                self.translate_int_to_binary_reverse_code(
                    self.__second_number_in_dicrect_code)
            self.__first_number_in_additional_code = \
                self.translate_int_to_binary_additional_code(
                    self.__first_number_in_reverse_code)
            self.__second_number_in_additional_code = \
                self.translate_int_to_binary_additional_code(
                    self.__second_number_in_reverse_code)

    @property
    def numbers(self) -> str:
        return self.create_message()

    def create_message(self) -> str:

        def convert_list_in_strlist(numbers: List[int]):
            return ''.join(map(str, numbers))

        first_direct_number = convert_list_in_strlist(
            self.__first_number_in_dicrect_code)
        second_direct_number = convert_list_in_strlist(
            self.__second_number_in_dicrect_code)
        first_reverse_number = convert_list_in_strlist(
            self.__first_number_in_reverse_code)
        second_reverse_number = convert_list_in_strlist(
            self.__second_number_in_reverse_code)
        first_additional_number = convert_list_in_strlist(
            self.__first_number_in_additional_code)
        second_additional_number = convert_list_in_strlist(
            self.__second_number_in_additional_code)

        return f'First number: {first_direct_number}\
                \nSecond number: {second_direct_number}\
                \nFirst reverse number: {first_reverse_number}\
                \nSecond reverse number: {second_reverse_number}\
                \nFirst additional number: {first_additional_number}\
                \nSecond additional number: {second_additional_number}'

    def insert_zero_for_byte(self, number_in_binary: List[int], number: int, not_sign: bool = False):
        if len(number_in_binary) % 8 == 0 and not not_sign:
            number_in_binary += [0 for i in range(0, 8)]
        while len(number_in_binary) % 8 != 0:
            number_in_binary.append(0)
        if number < 0 and not not_sign:
            number_in_binary[-1] = 1
        return list(reversed(number_in_binary))
    
    def translate_int_to_binary_direct_code(self, number: int,  not_sign: bool = False) -> List[int]:

        remains_from_divisions = 0
        remainder_of_number = abs(number)
        binary_number = []

        while remainder_of_number != 0 and remainder_of_number != 1:
            remains_from_divisions = remainder_of_number % 2
            remainder_of_number //= 2
            binary_number.append(remains_from_divisions)
        binary_number.append(remainder_of_number)

        return self.insert_zero_for_byte(binary_number, number, not_sign)

    def translate_int_to_binary_reverse_code(
            self, numbers_in_direct_code: List[int]) -> List[int]:

        numbers_in_reverse_code = numbers_in_direct_code.copy()

        if numbers_in_reverse_code[0] == 1:
            numbers_in_reverse_code[1:] = [
                1 * (i == False) for i in numbers_in_reverse_code[1:]]

        return numbers_in_reverse_code

    def translate_int_to_binary_additional_code(
            self, numbers_in_reverse_code: List[int]) -> List[int]:
        numbers_in_additional_code = numbers_in_reverse_code.copy()
        if numbers_in_additional_code[0] != 0:
            for i in range(len(numbers_in_additional_code) - 1, -1, -1):
                if numbers_in_additional_code[i] != 1:
                    numbers_in_additional_code[i] = 1
                    break
                numbers_in_additional_code[i] = 0

        return numbers_in_additional_code

    def add_two_numbers(self) -> int:
        temp_first_number, temp_second_number = self.align_numbers_in_reverse(
            self.__first_number_in_additional_code, self.__second_number_in_additional_code)

        return self.translate_additional_code_to_number(self.addition_of_numbers(temp_first_number, temp_second_number))

    def negative(self, number) -> List[int]:
        return number + [1]
    
    def addition_of_numbers(
            self,
            temp_first_number: List[int],
            temp_second_number: List[int],
            option_division: bool = False,
            option_for_one_in_direct_code: bool = False):
        
        output, temp_counter = [0] * len(temp_first_number), 0
        for items in enumerate(zip(temp_first_number, temp_second_number)):
            output[items[0]] = items[1][0] + items[1][1]
            if temp_counter == 0 and output[items[0]] == 2:
                output[items[0]] = 0
                temp_counter += 1
            elif temp_counter == 1 and output[items[0]] == 1:
                output[items[0]] = 0
            elif temp_counter == 1 and output[items[0]] == 2:
                output[items[0]] = 1
            elif temp_counter == 1 and output[items[0]] == 0:
                output[items[0]] = 1
                temp_counter = 0
        if option_division == False and option_for_one_in_direct_code == False:
            if self.__first_number_in_additional_code[0] == 1 and self.__second_number_in_additional_code[0] == 1 \
                    and temp_counter == 1 and output[-1] == 0:
                output = self.negative(output)
            if self.__first_number_in_additional_code[0] == 0 and self.__second_number_in_additional_code[0] == 0 \
                    and output[-1] == 1:
                output = output + [0]
        elif option_for_one_in_direct_code:
            if temp_counter == 1:
                output[-1] = 0
                output = output + [1]
        output[:] = list(reversed(output))
        return output

    def translate_additional_code_to_number(
            self, number_in_additional_code: List[int]) -> int:
        output_number = number_in_additional_code[0] * \
            (-(2**(len(number_in_additional_code) - 1)))

        for i in range(1, len(number_in_additional_code)):
            output_number += (number_in_additional_code[i] * (
                2**(len(number_in_additional_code) - i - 1)))

        return output_number

    def product(self) -> int:
        temp_first_number, temp_second_number = self.align_numbers_in_reverse(
            [0] + self.__first_number_in_dicrect_code[1:], [0] + self.__second_number_in_dicrect_code[1:])
        temp_first_number = list(reversed(temp_first_number))
        temp_second_number = list(reversed(temp_second_number))
        return self.translate_additional_code_to_number(self.product_numbers(temp_first_number, temp_second_number))

    def get_sign(self) -> int:
        sign = 0
        if (self.__first_number_in_dicrect_code[0] == 0 and self.__second_number_in_dicrect_code[0] == 1) or (
                self.__first_number_in_dicrect_code[0] == 1 and self.__second_number_in_dicrect_code[0] == 0):
            sign = 1
        return sign

    def product_numbers(self, temp_first_number: List[int], temp_second_number: List[int]) -> int:

        sign = self.get_sign()
        temp_sum_of_two_numbers = [0] * len(temp_first_number)
        counter = 1

        if temp_first_number[-1] == 1:
            output = temp_second_number.copy()
        else:
            output = [0] * len(temp_first_number)

        for i in range(len(temp_first_number) - 2, -1, -1):
            for j in range(len(temp_second_number) - 1, -1, -1):
                temp_sum_of_two_numbers[j] = temp_first_number[i] * temp_second_number[j]

            output = self.addition_of_numbers(
                list(reversed([0] + output)),
                list(reversed(temp_sum_of_two_numbers + counter * [0])))
            counter += 1
        output[0] = sign

        return self.translate_int_to_binary_additional_code(
            self.translate_int_to_binary_reverse_code(output))
    
    def align_size(self, first_number: List[int], second_number: List[int]):
        if not self.more_than(first_number, second_number):
            return (first_number, second_number)
        index = 0
        for i in range(0, len(first_number)):
            if first_number[i] == 1:
                index = len(first_number) - i
                first_number[:] = first_number[i:]
                break
        if len(first_number) <= len(second_number):
            second_number[:] = [second_number[0 - i - 1]
                                for i in range(0, index)]
            second_number = list(reversed(second_number))
        else:
            second_number = [0] * (len(first_number) - len(second_number)) + second_number
        return (first_number, second_number)
    
    def more_than(self, first_number: List[int], second_number: List[int]) -> bool:
            if len(first_number) > len(second_number):
                return True
            elif len(first_number) < len(second_number):
                return False
            for i in range(0, len(first_number)):
                if first_number[i] > second_number[i]:
                    return True
                elif first_number[i] < second_number[i]:
                    return False
            return True

    def check_zero(self, first_number: List[int], second_number: List[int]):
        if not any(first_number) or not any(second_number):
            raise Exception('Division on zero.')
    
    def division_numbers(self) -> int:
        sign = self.get_sign()
        temp_fist_number = [0] + self.__first_number_in_dicrect_code.copy()[1:]
        temp_second_number = [0] + self.__second_number_in_dicrect_code.copy()[1:]
        temp_fist_number, temp_second_number = self.align_size(temp_fist_number, temp_second_number)
        positive_second_number = temp_second_number.copy()
        result = [0] * len(temp_fist_number)
        temp_second_number = self.translate_int_to_binary_additional_code(
            self.translate_int_to_binary_reverse_code([1] + temp_second_number))

        self. check_zero(temp_fist_number, temp_second_number)
        
        while self.more_than(temp_fist_number, positive_second_number):
            temp_fist_number = self.addition_of_numbers(
                list(
                    reversed(temp_fist_number)), list(reversed(temp_second_number)), option_division=True)
            result = self.addition_of_numbers(
                list(
                    reversed(result)), list(reversed([0] * len(result) + [1])), option_for_one_in_direct_code=True)
        return  self.translate_additional_code_to_number(self.translate_int_to_binary_additional_code(
            self.translate_int_to_binary_reverse_code([sign] + result)))

    def align_numbers_in_reverse(self, first_number: List[int], second_number: List[int]) -> Tuple[List[int],List[int]]:
        output_size = max(len(first_number), len(second_number))

        temp_first_number = list(reversed([first_number[0]] +
                                          (output_size - len(first_number)) *
                                          [first_number[0]] +
                                          first_number.copy()[1:]))
        temp_second_number = list(reversed([second_number[0]] +
                                           (output_size - len(second_number)) *
                                           [second_number[0]] +
                                           second_number.copy()[1:]))

        return (temp_first_number, temp_second_number)
    
    def delete_zero(self, number: List[int]) -> List[int]:
        for i in range(0,len(number)):
            if number[i] == 1:
                number[:] = number[i:]
                return number
        return [0]
    
    def normilaze(self, float_number: List[int]) -> Tuple[int,List[int]]:
        index = 127
        for i in range(0,len(float_number)):
            if float_number[i] == 1:
                index = i+1
                float_number[i] = 0
                break
        return (index, float_number)

    def translate_float_to_binary(self, float_number: str) -> List[List[int]]:
        int_part = int(float_number[:float_number.find('.')])
        int_part_in_binary = self.translate_int_to_binary_direct_code(int_part)
        number_floating_point = [[],[],[]]
        number_floating_point[0] = [int_part_in_binary[0]]
        int_part_in_binary = self.delete_zero(int_part_in_binary)
        if int_part_in_binary != [0]:
            number_floating_point[1] = self.translate_int_to_binary_direct_code((len(int_part_in_binary)-1)+127, not_sign = True)
            float_part = float('0.'+float_number[float_number.find('.')+1:])
            float_part_in_binary = self.translate_float_part_of_number_in_direct_code(float_part,23 - len(int_part_in_binary[1:]))
            number_floating_point[2] = int_part_in_binary[1:]+float_part_in_binary+[0]*(23-len(int_part_in_binary[1:]+float_part_in_binary))
        else:
            float_part = float('0.'+float_number[float_number.find('.')+1:])
            float_part_in_binary = self.translate_float_part_of_number_in_direct_code(float_part,23)
            index, float_part_in_binary = self.normilaze(float_part_in_binary)   
            number_floating_point[1] = self.translate_int_to_binary_direct_code((-index)+127, not_sign = True)
            number_floating_point[2] = float_part_in_binary[index:]+[0]*(23-len(float_part_in_binary[index:]))

        return number_floating_point
    
    def move(self, number: List[object], difference):
        number.remove(',')
        number = [0]*difference + number
        number.insert(1,',')
        return number
    
    def align_exponents(self) -> Tuple[List[int],List[int],int]:
        first_number_exponents = self.translate_additional_code_to_number([0]*8+self.__first_number[1])-127
        second_number_exponents = self.translate_additional_code_to_number([0]*8+self.__second_number[1])-127
        exponent = max(first_number_exponents, second_number_exponents)
        first_number = [1*any(self.__first_number[1]),',']+self.__first_number[2]
        second_number = [1*any(self.__second_number[1]),',']+self.__second_number[2]
        if first_number_exponents != exponent:
            difference = exponent-first_number_exponents
            first_number = self.move(first_number,difference)
        else:
            difference = exponent-second_number_exponents
            second_number = self.move(second_number,difference)
        first_number += [0]*(len(second_number)-len(first_number))
        second_number += [0]*(len(first_number)-len(second_number)) 
        if first_number[0] == 1:
            first_number = self.move(first_number,1)
            second_number = self.move(second_number,1)
        if second_number[0] == 1:
            second_number = self.move(second_number,1)
            first_number = self.move(first_number,1)
        return (first_number, second_number, exponent)
    
    def addition_floating_number(self) -> float:
        first_number, second_number, exponent = self.align_exponents()
        first_number.remove(',')
        second_number.remove(',')
        result = self.addition_of_numbers_floating_point(first_number,second_number)
        if exponent >= 0:
                result.insert((exponent+2), ',')
        else:
            result = [0]*abs(exponent+1) + result
            result.insert((abs(exponent)-(len(result)-len(first_number))), ',')
            
        return self.translate_floating_point_number(result)
    
    def addition_of_numbers_floating_point(self, first_number: List[int], second_number: List[int]) -> List[int]:
        output = self.addition_of_numbers(list(reversed(first_number)),
                                        list(reversed(second_number)),
                                        option_division=True,
                                        option_for_one_in_direct_code=True)
        return output
            
    def translate_floating_point_number(self, number: List[int]) -> str:
        int_part_of_number = self.translate_additional_code_to_number([0]+number[:number.index(',')])
        float_part_of_number = self.translate_float_part_of_number(number[number.index(',')+1:])
        return str(int_part_of_number+float_part_of_number)
    
    def translate_float_part_of_number(self, float_part: List[int]) -> float:
        result = 0
        for i in range(1, len(float_part)+1):
            result+=2**(-i)*float_part[i-1]
        return result
    
    def translate_float_part_of_number_in_direct_code(self, float_number: List[int], mantiss_size: int) -> List[int]:
        temp_float_number_part = float_number
        number_precision = mantiss_size
        result = []
        while len(result)<number_precision and temp_float_number_part != 1.0:
            temp_float_number_part = temp_float_number_part*2
            result.append(int(str(temp_float_number_part)[0]))
            if temp_float_number_part > 1:
                temp_float_number_part -= 1
        return result