# -*- coding: utf-8 -*- 
from modules.token import Token
from abc import abstractmethod

class Compiler:

    @abstractmethod
    def lexer(string):
        string += '$'
        tokens = []

        index = 0
        while string[index] != '$':
            while string[index] == ' ':
                index += 1

            if string[index] == '+':
                index += 1
                tokens.append(Token('PLUS', '+'))

            elif string[index] == '*':
                index += 1
                tokens.append(Token('TIMES', '*'))

            elif string[index].isdigit():
                number = ''
                while string[index].isdigit():
                    number += string[index]
                    index += 1

                if string[index] == '.':
                    
                    number += string[index]
                    index += 1

                    while string[index].isdigit():
                        number += string[index]
                        index+=1
                    
                tokens.append(Token('NUMBER', number))

        tokens.append(Token('END', '$'))

        # find all tokens in 'string' and place them as Token objects in 'tokens'
        return tokens