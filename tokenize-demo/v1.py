# 简单词典
dictionary = {"我", "爱", "北京", "天安门", "中国", "天", "安门"}

def tokenize_mm(text):
    max_len = max(len(word) for word in dictionary)  # 找到词典中最长词的长度
    result = []
    i = 0

    while i < len(text):
        match = None
        # 从当前位置向右尝试匹配最长的词
        for j in range(min(max_len, len(text) - i), 0, -1):
            word = text[i:i + j]
            if word in dictionary:
                match = word
                break

        if match:  # 如果找到了匹配的词
            result.append(match)
            i += len(match)
        else:  # 如果没有匹配，单字切分
            result.append(text[i])
            i += 1

    return result

# 测试
text = "我爱北京天安门"
words = tokenize_mm(text)
print(" / ".join(words))
