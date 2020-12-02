# -*- coding: utf-8 -*-


# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью в МНОГОПРОЦЕССНОМ стиле
#
# Бумаги с нулевой волатильностью вывести отдельно.
# Результаты вывести на консоль в виде:
#   Максимальная волатильность:
#       ТИКЕР1 - ХХХ.ХХ %
#       ТИКЕР2 - ХХХ.ХХ %
#       ТИКЕР3 - ХХХ.ХХ %
#   Минимальная волатильность:
#       ТИКЕР4 - ХХХ.ХХ %
#       ТИКЕР5 - ХХХ.ХХ %
#       ТИКЕР6 - ХХХ.ХХ %
#   Нулевая волатильность:
#       ТИКЕР7, ТИКЕР8, ТИКЕР9, ТИКЕР10, ТИКЕР11, ТИКЕР12
# Волатильности указывать в порядке убывания. Тикеры с нулевой волатильностью упорядочить по имени.
#
from utilites import time_track, show_result, generate_filenames

#
from utilites import time_track, show_result, generate_filenames

import multiprocessing
from queue import Empty


class Ticker(multiprocessing.Process):

    def __init__(self, ticket_folder, collector=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ticket_folder = ticket_folder
        self.name_ticket = ''
        self.volatility = 0
        self.collector = collector
        self.for_get = {}

    def run(self):
        self.calculate(self.open())

    def open(self):
        price_scope = []
        with open(self.ticket_folder, mode='r') as open_ticker:
            for element in open_ticker:
                scattered_element = element.split(',')
                self.name_ticket = scattered_element[0]
                if scattered_element[2] != 'PRICE':
                    price_scope.append(float(scattered_element[2]))
            return price_scope

    def calculate(self, unsorted):
        unsorted.sort()
        half_sum = (unsorted[0] + unsorted[-1]) / 2
        self.volatility = ((unsorted[-1] - unsorted[0]) / half_sum) * 100
        self.for_get[self.name_ticket] = self.volatility
        # TODO сюда лучше положить словарь с ключами dict(name_ticket= self.name_ticket, volatility= self.volatility)
        # TODO это чтобы потом не делать лишний фор при вытаскивания значений
        return self.collector.put(self.for_get)


@time_track
def main(folder):
    zero_tickers = []
    value_key = {}
    sorted_place = []
    tickers = []
    collector = multiprocessing.Queue()

    for last_folder in generate_filenames(folder):
        tickers.append(Ticker(last_folder, collector=collector))
    for ticker in tickers:
        ticker.start()

    while True:
        try:
            collect = collector.get(True, 1)
            # TODO тут можно обойтись без цикла
            for key in collect:
                value = collect[key]
                # TODO тут сразу сравнивать if collect['volatility']  == 0
                if value == 0:
                    zero_tickers.append(key)
                else:
                    value_key[value] = key
                    sorted_place.append(value)
                    sorted_place.sort()
        except Empty:
            # TODO эту часть можно записать в виде списковой сборки и применив функцию not any()
            for ticker in tickers:
                if not ticker.is_alive():
                    break
            # TODO этот break сработает в любом случае, а нам нужно только верхним брейком как то выйти из while
            break

    for ticker in tickers:
        ticker.join()
    show_result(sorted_place, value_key, zero_tickers)


# Core 4 по 1.4Hz - Функция работала 1.9725 секунд(ы)
# Core 4 по 2.4Hz - Функция работала 3.2383 секунд(ы)
path = "trades/"
if __name__ == '__main__':
    main(folder=path)
