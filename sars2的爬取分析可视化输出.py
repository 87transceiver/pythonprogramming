import requests
from bs4 import BeautifulSoup
from Bio import SeqIO
import matplotlib.pyplot as plt

# GISAID和NCBI的URL、API密钥等信息
gisaid_url = "https://www.gisaid.org/"
ncbi_url = "https://www.ncbi.nlm.nih.gov/"

# 发送HTTP请求获取数据并解析
def get_data(url):
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, "html.parser")
    return soup

# 从GISAID和NCBI获取数据并保存到本地文件
gisaid_data = get_data(gisaid_url)
ncbi_data = get_data(ncbi_url)

# 保存数据到本地文件
with open("gisaid_data.html", "w", encoding="utf-8") as file:
    file.write(gisaid_data.prettify())
with open("ncbi_data.html", "w", encoding="utf-8") as file:
    file.write(ncbi_data.prettify())

# 使用Biopython分析序列数据
sars2_sequence = SeqIO.read("sequence.fasta", "fasta")
sequence_length = len(sars2_sequence)

# 可视化分析结果
labels = ["Sequence Length"]
values = [sequence_length]

plt.bar(labels, values)
plt.ylabel("Value")
plt.title("SARS-CoV-2 Sequence Analysis")
plt.show()
