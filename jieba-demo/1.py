import jieba


title = '中国船舶及海洋工程设计研究院(中国船舶工业集团公司第七0八研究所)'
a_seg_list = jieba.cut_for_search(title)
print(" ".join(a_seg_list))