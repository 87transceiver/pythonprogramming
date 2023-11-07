import requests
from Bio import SeqIO
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML
import matplotlib.pyplot as plt

# 定义爬取NCBI上的随机基因组信息函数
def fetch_random_genome():
    url = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi'
    params = {
        'db': 'nucleotide',
        'term': 'random',
        'rettype': 'fasta',
        'retmode': 'text',
        'retmax': 10  # 设置返回的随机序列数量
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.text
    else:
        print("Failed to fetch random genome information.")
        return None

# 定义进行blast分析的函数
def blast_analysis(genome_sequence):
    result_handle = NCBIWWW.qblast('blastn', 'nt', genome_sequence)
    blast_records = NCBIXML.parse(result_handle)
    return blast_records

# 定义可视化blast结果的函数
def visualize_blast_results(blast_records):
    hits_count = 0
    for blast_record in blast_records:
        for alignment in blast_record.alignments:
            hits_count += 1

    # 绘制柱状图
    plt.bar(['Hits'], [hits_count])
    plt.xlabel('Hits')
    plt.ylabel('Count')
    plt.title('BLAST Hits Count')
    plt.show()

if __name__ == "__main__":
    # 爬取随机基因组信息
    genome_data = fetch_random_genome()

    # 进行blast分析
    blast_records = blast_analysis(genome_data)

    # 可视化blast结果
    visualize_blast_results(blast_records)
