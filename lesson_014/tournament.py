from bowling import get_score


class Tournament:
    def __init__(self, initial_file, result_file):
        self.initial_file = initial_file
        self.result_file = result_file
        self.winner = []
        self.name_count_game = {}
        self.name_count_win = {}

    def writing(self):
        result_file = open(self.result_file, mode='a+', encoding='utf-8')
        with open(self.initial_file, mode='r', encoding='utf-8') as file:
            for line in file:
                line = line.strip('\n')
                try:
                    if '\t' in line:
                        line = line.split('\t')
                        name = line[0]
                        scope = line[1]
                        digit_scope = get_score(scope)
                        new_line = f'{name}\t{scope}\t{digit_scope}'
                        result_file.write(f'{new_line}\n')
                        self.winner_info(name, digit_scope)
                        self.count_game(name)
                    elif 'winner is' in line:
                        winner_line = f'winner is {self.winner[0]}'
                        result_file.write(f'{winner_line}\n')
                        self.count_win(self.winner[0])
                        self.winner.clear()
                    else:
                        result_file.write(f'{line}\n')
                except ValueError as exc:
                    new_line = f'{name}\t{scope}\t{exc.args}'
                    result_file.write(f'{new_line}\n')
                except IndexError:
                    new_line = f'{name}\t{scope}\t(Не верное кол-во фреймов.)'
                    result_file.write(f'{new_line}\n')
        result_file.close()

    def winner_info(self, name, total_score):
        if not self.winner:
            self.winner.append(name)
            self.winner.append(total_score)
        elif self.winner[1] < total_score:
            self.winner.clear()
            self.winner.append(name)
            self.winner.append(total_score)

    def count_game(self, name):
        if name in self.name_count_game:
            self.name_count_game[name] += 1
        else:
            self.name_count_game[name] = 1

    def count_win(self, name):
        if name in self.name_count_win:
            self.name_count_win[name] += 1
        else:
            self.name_count_win[name] = 1
