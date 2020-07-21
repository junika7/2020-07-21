import sys

class FASTA:
    def __init__(self, file_name):
        self.file_name = file_name
        self.count = {}
        self.length = 0
    def count_base(self):
        with open(self.file_name, 'r') as handle:
            for line in handle:
                if line.startswith(">"):
                    continue
                line = line.strip()
                for s in line:
                    if s in self.count:
                        self.count[s] += 1
                    else:
                        self.count[s] = 1
    def __len__(self): #import tool > t = tool.FASTA("059.fasta") > t.count_base() >  len(t) 가능
        for k, v in self.count.items():
            self.lenght += v
        return self.length

class FASTQ:
    def __init__(self, file_name):
        self.file_name = file_name
        self.read_num = 0
    def count_read_num(self):
        cnt = 0
        with open(self.file_name, 'r') as handle:
            for line in handle:
                if cnt % 4 == 0:
                    header = line.strip()
                    self.read_num += 1
                elif cnt % 4 == 1:
                    seq = line.strip()
                elif cnt % 4 == 3:
                    qual = line.strip()
                cnt += 1


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"#usage: python {sys.argv[0]} [fasta]")
        sys.exit()
    file_name = sys.argv[1]
    t = FASTQ(file_name)
    t.count_read_num()
    print(t.read_num)