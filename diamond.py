class Diamond():
    def print_diamond(self, character):
        if character == 'A':
            return 'A'
        
        start_char = ord('A')
        i = start_char
        target_char = ord(character)
        line = ''
        front_space = ' '*(target_char - i)
        middle_space = 1
        
        while i <= target_char:
            if i == start_char:
                line += ' '*(target_char - i) + chr(i) + '\n'
            else:
                line += ' '*(target_char - i) + chr(i) + ' '*(middle_space) + chr(i) + '\n'
                middle_space += 2
            i += 1

        i = target_char - 1
        middle_space -= 4

        while i >= start_char:
            if i == start_char:
                line += ' '*(target_char - i) + chr(i)
            else:
                line += ' '*(target_char - i) + chr(i) + ' '*(middle_space) + chr(i) + '\n'
                middle_space -= 2
            i -= 1



        return line