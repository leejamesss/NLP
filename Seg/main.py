import jieba
from collections import defaultdict

# 定义停用词列表
stopwords = ['被', '并', '的', '给', '今天', '据', '了', '年', '其', '前天',
             '让', '上', '是', '说', '要', '也', '一本', '一个', '已', '用',
             '于', '在', '至今', '最', '昨天']

# 定义文献数据的列表
docs = [
    '埃隆·马斯克在中国谈论“智能联网汽车”特斯拉首席执行官埃隆马斯克会见中国的高级部长，讨论了电动汽车和“智能联网”汽车的发展以及汽车制造商在这个共产主义国家的业务扩张。',
    '秦刚会晤特斯拉首席执行官马斯克2023年5月30日，国务委员兼外长秦刚在北京会见特斯拉首席执行官马斯克；马斯克表示特斯拉公司反对“脱钩断链”，愿继续拓展在华业务。  ',
    '马斯克访北京 多部长接待 “马中”关系引华盛顿质疑特斯拉电动汽车制造商马斯克在中美关系紧张之际访问中国，受到北京高规格接待：外交部长，工业信息部长，商务部长纷纷出场接待。法新社说，他与中国之间强有力的经济关系在华盛顿引起了质疑。',
    '中国称马斯克反对美中脱钩中国外交部称，特斯拉CEO马斯克向中国官员表示，该公司反对全球前两大经济体“脱钩断链”。这次会议是在马斯克抵达中国后不久举行的，目前中美两国处于地缘政治紧张局势加剧状态。',
    '商务部部长王文涛会见特斯拉公司首席执行官马斯克5月31日，商务部部长王文涛会见特斯拉公司首席执行官马斯克。双方就中美经贸合作、特斯拉在华发展等议题进行了广泛、深入的交流。'
]

# 分词、统计词频和建立倒排索引
inverted_index = defaultdict(list)
for i, doc in enumerate(docs):
    # 分词并去除停用词
    words = [word for word in jieba.cut(doc) if word not in stopwords]
    # 统计词频
    word_counts = defaultdict(int)
    for word in words:
        word_counts[word] += 1
    # 建立倒排索引
    for word, count in word_counts.items():
        inverted_index[word].append((i, count))

# 打印结果
for word, doc_counts in inverted_index.items():
    print(f"{word}:\t{doc_counts}")
