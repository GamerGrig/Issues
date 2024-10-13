from time import sleep
from datetime import datetime
from threading import Thread

start_time = datetime.now()


def wite_words(word_count, file_name):
    for i in range(1, word_count + 1):
        text = f'Какое-то слово № {i}'
        with open(f'{file_name}.txt', 'a', encoding='utf-8') as file:
            file.write(text + '\n')
        sleep(0.1)
    print(f'Завершилась запись в файл {file_name}.txt')


wite_words(10, 'example1')
wite_words(30, 'example2')
wite_words(200, 'example3')
wite_words(100, 'example4')

end_time = datetime.now()
res_time = end_time - start_time
print(f'Работа потоков', res_time)

start_time = datetime.now()

thr_first = Thread(target=wite_words, args=(10, 'example5'))
thr_second = Thread(target=wite_words, args=(30, 'example6'))
thr_third = Thread(target=wite_words, args=(200, 'example7'))
thr_four = Thread(target=wite_words, args=(100, 'example8'))

# запуск потоков
thr_first.start()
thr_second.start()
thr_third.start()
thr_four.start()

# обязательно дождаться окончания отработки потока
thr_first.join()
thr_second.join()
thr_third.join()
thr_four.join()

end_time = datetime.now()
res_time = end_time - start_time
print(f'Работа потоков', res_time)