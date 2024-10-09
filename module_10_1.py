from time import sleep, time
from threading import Thread

def write_words(word_count, file_name):
    counter = 1
    with open(file_name, 'w+', encoding = 'utf-8') as file:
        for words in range(word_count):
            cursor_pos = file.tell()
            file.write(f'Какое-то слово N {counter}\n')
            counter += 1
            sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')

time_start = time()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
time_end = time()
time_res = round((time_end - time_start), 3)
print(f'Время работы функции: {time_res} секунды')

time_start = time()
thr_first = Thread(target=write_words, args=(10, 'example5.txt'))
thr_second = Thread(target=write_words, args=(30, 'example6.txt'))
thr_third = Thread(target=write_words, args=(200, 'example7.txt'))
thr_four = Thread(target=write_words, args=(100, 'example8.txt'))

thr_first.start()
thr_second.start()
thr_third.start()
thr_four.start()

thr_first.join()
thr_second.join()
thr_third.join()
thr_four.join()
time_end = time()
time_res = round((time_end - time_start), 3)
print(f'Время работы потоков: {time_res} секунды')