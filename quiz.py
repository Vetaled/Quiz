import sys


def open_file(file_name, mode):
    '''Открывает файл'''
    try:
        the_file = open(file_name, mode)
    except:
        print("Невозможно открыть данный файл.Работа программы завершиться.")
        input("\n\nНажмите Enter , чтобы выйти.")
        sys.exit()
    else:
        return the_file


def next_line(the_file):
    """Возвращает в отформатированном виде очередную строку игрового файла"""
    line = the_file.readline()
    line = line.replace("/", "\n")
    return line


def next_block(the_file):
    """Возвращает очередной блок данных из игрового файла"""
    category = next_line(the_file)
    question = next_line(the_file)
    answer = []
    for i in range(4):
        answer.append(next_line(the_file))
    correct = next_line(the_file)[0]
    explanation = next_line(the_file)
    return category, question, answer, correct, explanation


def welcome(title):
    """Приветствие"""
    print("\t\tНаверное, ты хочешь поиграть в викторину!?\n")
    print("\t\t", title, "\n")


def main():
    quiz_file = open_file("quiz.txt", "r")
    title = next_line(quiz_file)
    welcome(title)
    score = 0
    category, question, answer, correct, explanation = next_block(quiz_file)
    while category:
        print(category)
        print(question)
        for i in range(4):
            print("\t", i + 1, "-", answer[i])
        answer = input("Ваш ответ: ")
        if answer == correct:
            print("\nДа!", end=" ")
            score += 1
        else:
            print("\nНет!", end=" ")
        print(explanation)
        print("Счет: %d \n" % score)
        try:
            category, question, answer, correct, explanation = next_block(quiz_file)
        except:
            break
    quiz_file.close()
    print("Это был последний вопрос.")
    print("Score = %d" % score)


main()
input("\n\nНажмите  Enter, чтобы выйти из программы.")
