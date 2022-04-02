def hangman(word):
    wrong = 0
    stages = ["",
            "_______        ",
            "|              ",
            "|       |      ",
            "|       o      ",
            "|      /|\     ",
            "|      / \     ",
            "|              "]
    rletters = list(word) # 文字を一文字ずつにリスト化
    board = ["_"] * len(word) # 文字数を_で表す
    win = False # 初期値は負け
    print("ハングマンへようこそ")

    while wrong < len(stages) -1: # stagesの長さを確認　何回間違ってよいか
        print("\n") # 見やすいように改行
        msg = "１字を予想してね: " # 入力の指示
        char = input(msg)
        if char in rletters: #　入力が一文字でも合っていたらTrue
            cind = rletters.index(char)# 入力値が正解の何番目かを確認
            board[cind] = char # 正解した場所の_　を正解に更新
            rletters[cind] = '$' # 回答の正解した箇所を＄に変更　同じ文字が合った場合の対処
        else: # Falseの場合
            wrong += 1 # wrongを一つ増やす
        print(" ".join(board)) #　見やすいように一文字あけて現状を表示
        e = wrong + 1 # eを更新　なぜ？
        print("\n".join(stages[0:e])) # 見やすいように一文字あけてstagesを表示
        if "_" not in board: # boardに_つまり、すべて正解した場合
            print("あなたの勝ち！")
            print(" " .join(board))
            win = True # 勝ちに変更
            break
    if not win: # 間違って良い回数を超えた場合、つまり負け
        # print("\n".join(stages[0:wrong+1]))
        print("\n".join(stages[0:e])) # e使ってやれよ
        print("あなたの負け！正解は{}.".format(word))

import random

r = random.randint(1,5)
answer_list = ["cat","apple","dog","banana","orange"]
answer = answer_list[r]
hangman(answer)