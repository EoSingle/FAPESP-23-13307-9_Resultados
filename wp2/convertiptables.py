import pandas as pd
import re

# Função para extrair dados de uma linha de log
def parse_log_line(line):
    # Expressões regulares para extrair os campos
    regex = r'(?P<timestamp>\w{3} \d{2} \d{2}:\d{2}:\d{2}) (?P<hostname>\S+) \[\S+\]: IN=(?P<in_iface>\S+) OUT=(?P<out_iface>\S*) MAC=(?P<mac>\S+) SRC=(?P<src_ip>\S+) DST=(?P<dst_ip>\S+) LEN=(?P<len>\d+) TOS=(?P<tos>\S+) PREC=(?P<prec>\S+) TTL=(?P<ttl>\d+) ID=(?P<id>\d+) PROTO=(?P<proto>\S+) SPT=(?P<spt>\d+) DPT=(?P<dpt>\d+)( SEQ=(?P<seq>\d+))?( ACK=(?P<ack>\d+))?( WINDOW=(?P<window>\d+))?( SYN)?( URGP=(?P<urgp>\d+))?( MARK=(?P<mark>\d+))?'
    match = re.match(regex, line)
    
    if match:
        return match.groupdict()
    return None

# Lista para armazenar os logs processados
logs = []

path = './v5/na-server/ulogd_syslogemu.log'

# Ler o arquivo de logs linha por linha
with open(path, 'r') as file:
    for line in file:
        parsed_line = parse_log_line(line)
        if parsed_line:
            logs.append(parsed_line)

# Converter a lista de dicionários para um DataFrame do Pandas
df = pd.DataFrame(logs)

# Salvar em um arquivo CSV
df.to_csv('iptables_logs.csv', index=False)

#print(df)

