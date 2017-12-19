import sys
import re
import MeCab

book_name = sys.argv[1]
wakati_name = book_name + ".wakati"

parts = ["名詞", "動詞", "形容詞", "副詞", "未知語"]

# 青空文庫のフォーマット
repl = ""
regex_ruby = r"《.+?》"
regex_ruby_head = "｜"
regex_note = r"［＃.+?］"

tagger = MeCab.Tagger("-Ochasen")

reader = open(book_name, "r")
writer = open(wakati_name, "w")

for line in reader:
    line = re.sub(regex_ruby, repl, line)
    line = re.sub(regex_note, repl, line)
    node = tagger.parseToNode(line)

    while node:
        feature = node.feature.split(",")
        if feature[0] in parts:
            if feature[6] == "*":  # 未知語はそのまま出したい
                writer.write(node.surface + " ")
            else:
                writer.write(feature[6] + " ")
        node = node.next
    writer.write("\n")

writer.close()
reader.close()

