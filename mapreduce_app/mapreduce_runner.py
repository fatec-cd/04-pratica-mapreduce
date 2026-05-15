#!/usr/bin/env python3
"""
MapReduce Runner: Orquestra o pipeline Map-Reduce em Python puro
"""
import sys
import re
import argparse
from pathlib import Path
from collections import defaultdict

# Lista simples de stopwords em português (artigos, preposições, conectivos)
STOPWORDS = {
    'o', 'a', 'os', 'as', 'um', 'uma', 'uns', 'umas',
    'de', 'da', 'do', 'das', 'dos', 'em', 'no', 'na', 'nos', 'nas',
    'por', 'para', 'com', 'e', 'que', 'se', 'me', 'te', 'lhe', 'é'
}


def run_map_phase(input_file):
    """
    Fase Map: le o arquivo de entrada e emite pares (palavra, 1).
    Retorna uma lista de tuplas (palavra, contagem).
    """
    pairs = []
    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip().lower()
            words = re.findall(r'\b\w+\b', line)
            for word in words:
                if word in STOPWORDS:
                    continue
                pairs.append((word, 1))
    return pairs


def run_shuffle_sort(pairs):
    """
    Fase Shuffle & Sort: ordena os pares pela chave (palavra).
    """
    return sorted(pairs, key=lambda x: x[0])


def run_reduce_phase(sorted_pairs):
    """
    Fase Reduce: soma as contagens de cada palavra.
    Retorna um dicionario {palavra: contagem}.
    """
    word_counts = defaultdict(int)
    for word, count in sorted_pairs:
        word_counts[word] += count
    return dict(word_counts)


def run_mapreduce(input_file, output_file):
    """
    Executa o pipeline MapReduce completo.

    Args:
        input_file: caminho do arquivo de entrada
        output_file: caminho do arquivo de saida
    """
    print("Iniciando processamento MapReduce...")
    print(f"Input:  {input_file}")
    print(f"Output: {output_file}")

    if not Path(input_file).exists():
        print(f"Erro: arquivo '{input_file}' nao encontrado.")
        sys.exit(1)

    print("\nFase 1: MAP - processando palavras...")
    pairs = run_map_phase(input_file)

    print("Fase 2: SHUFFLE & SORT - ordenando dados...")
    sorted_pairs = run_shuffle_sort(pairs)

    print("Fase 3: REDUCE - agregando resultados...")
    word_counts = run_reduce_phase(sorted_pairs)

    with open(output_file, 'w', encoding='utf-8') as f:
        for word in sorted(word_counts.keys()):
            f.write(f"{word}\t{word_counts[word]}\n")

    print(f"\nProcessamento concluido. Resultados em: {output_file}")
    print(f"Total de palavras unicas: {len(word_counts)}")

    print("\nTop 10 palavras mais frequentes:")
    top10 = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    for i, (word, count) in enumerate(top10, 1):
        print(f"  {i:2}. {word}: {count}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='MapReduce Word Count')
    parser.add_argument('--input', default='data/input.txt',
                        help='Arquivo de entrada')
    parser.add_argument('--output', default='data/output.txt',
                        help='Arquivo de saida')

    args = parser.parse_args()
    run_mapreduce(args.input, args.output)
