import jieba

text = "我爱北京天安门，我是天才"
words = jieba.cut(text)  # 默认是精确模式
print(" / ".join(words))
