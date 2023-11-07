import requests
from datetime import date
from Bio import SeqIO

def fetch_genome_data():
    # 设置Github仓库API的URL
    url = 'https://api.github.com/repos/{owner}/{repo}/contents/{path}'

    owner = 'pangu-language'
    repo = 'COVID-19'

    # 获取新冠病毒基因组数据路径
    data_path = 'genomes/ncov/2019-ncov-sequences.fasta'
    
    response = requests.get(url.format(owner=owner, repo=repo, path=data_path))

    if response.status_code == 200:
        # 获取仓库中的数据
        data = response.json()

        # 解析数据并下载基因组信息
        genome_data = requests.get(data['download_url']).text

        return genome_data

    else:
        print("Failed to fetch genome data from Github.")
        return None

def analyze_genome_data(genome_data):
    # 在这里你可以使用biopython进行基因组信息的分析
    # 例如使用Bio.SeqIO读取基因组数据，进行序列分析等

    # 以读取FASTA文件为例
    for record in SeqIO.parse(genome_data, 'fasta'):
        print(record.id)
        print(record.seq)

if __name__ == "__main__":
    # 爬取新冠病毒基因组数据
    genome_data = fetch_genome_data()

    if genome_data:
        # 进行基因组数据分析
        analyze_genome_data(genome_data)
