#!/usr/bin/env python3
"""
Mapper: Transforma linhas de texto em pares (palavra, 1)
"""
import sys
import re

# Lista simples de stopwords em português (artigos, preposições, conectivos)
STOPWORDS = {
    'o', 'a', 'os', 'as', 'um', 'uma', 'uns', 'umas',
    'de', 'da', 'do', 'das', 'dos', 'em', 'no', 'na', 'nos', 'nas',
    'por', 'para', 'com', 'e', 'que', 'se', 'me', 'te', 'lhe', 'é'
}

def mapper():
    """
    Lê linhas do stdin e emite pares (palavra, 1)
    """
    for line in sys.stdin:
        # Remove espaços em branco e converte para minúsculas
        line = line.strip().lower()
        
        # Remove pontuação e divide em palavras
        words = re.findall(r'\b\w+\b', line)
        
        # Emite cada palavra com contagem 1
        for word in words:
            # Ignora stopwords
            if word in STOPWORDS:
                continue
            # Formato: palavra\t1
            print(f"{word}\t1")

if __name__ == "__main__":
    mapper()
