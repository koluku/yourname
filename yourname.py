import random
import time

def read_dummy():
    dummy_txt = open('dummyname.txt', 'rt')
    dummy_name = dummy_txt.readlines()
    dummy_txt.close()
    return dummy_name

if __name__ == '__main__':
    print('あなたの名前を入力してください。')
    your_name = input('>>> ')
    time.sleep(0.5)
    print('あなたは今この瞬間に自分の名前を忘れてしまいました！')
    print('--------------')
    name_list = read_dummy()
    name_list.append(your_name)
    random.shuffle(name_list)
    time.sleep(3)
    print('ずっとあなたを探していたの。')
    time.sleep(3)
    print('「でも僕自身の名前が思い出せないんだ」')
    time.sleep(3)
    for i in range(len(name_list)):
        print(name_list[i].strip())
        if your_name != name_list[i].strip():
            print('「いや、多分違うと思う」')
            time.sleep(0.5)
        else:
            print('「あぁそれだ！　その名前だ！　ありがとう！」')
            print('{}回目の質問によりあなたの名前が思い出されました。'.format(i))
            break
