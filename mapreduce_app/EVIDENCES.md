# Evidências da Atividade MapReduce

Resumo das execuções realizadas no repositório.

## Ambiente
- Python: `python3 --version` -> `Python 3.12.1`

## Comandos principais executados

```bash
python3 mapreduce_app/mapreduce_runner.py --input mapreduce_app/data/input.txt --output mapreduce_app/data/output.txt
cd mapreduce_app && python3 benchmark.py
# dentro de mapreduce_app
python3 mapreduce_runner.py --input data/livro.txt --output data/livro_output.txt
sort -t$'\t' -k2 -nr data/livro_output.txt | head -20
grep -E $'^(capitú|bentinho|amor|ciume)\t' data/livro_output.txt

# Opcional (stopwords):
python3 mapreduce_runner.py --input data/livro.txt --output data/livro_sem_stopwords_output.txt
sort -t$'\t' -k2 -nr data/livro_sem_stopwords_output.txt | head -20
```

## Resultados importantes

- Arquivo de saída (exemplo pequeno): `mapreduce_app/data/output.txt`
- Benchmark (resumo):
  - 1 MB — 0.20s — 4.90 MB/s
  - 5 MB — 0.82s — 6.11 MB/s
  - 10 MB — 1.74s — 5.74 MB/s
- Processamento de `livro.txt` (sem filtro): arquivo gerado `mapreduce_app/data/livro_output.txt`
  - Total de palavras únicas: 9589
  - Top 10 (mais frequentes): `a`(2671), `que`(2663), `e`(2215), `de`(1975), `o`(1879), `não`(1532), `me`(1034), `se`(857), `um`(793), `é`/`os`(713)
- Contagens específicas (grep):
  - `capitú` — 345
  - `bentinho` — 57
  - `amor` — 20
  - `ciume` — 4

## Resultado com remoção de stopwords (opcional)
- Arquivo gerado: `mapreduce_app/data/livro_sem_stopwords_output.txt`
- Top 10 (após remover stopwords): `não`(1532), `mas`(609), `era`(554), `eu`(531), `ao`(374), `como`(373), `capitú`(345), `minha`(342), `mais`(340), `ou`(277)

## Arquivos gerados
- mapreduce_app/data/output.txt
- mapreduce_app/data/benchmark_1mb.txt
- mapreduce_app/data/benchmark_5mb.txt
- mapreduce_app/data/benchmark_10mb.txt
- mapreduce_app/data/benchmark_1mb_output.txt
- mapreduce_app/data/benchmark_5mb_output.txt
- mapreduce_app/data/benchmark_10mb_output.txt
- mapreduce_app/data/livro_output.txt
- mapreduce_app/data/livro_sem_stopwords_output.txt

## Como capturar as evidências (screenshots)
1. No Codespaces, abra o Terminal e execute os comandos listados acima.
2. Faça screenshots do terminal mostrando cada saída importante (`python3 --version`, execução do `mapreduce_runner.py`, saída do `benchmark.py`, top 20 com `sort`).
3. Abra os arquivos de saída no editor e capture a janela do editor para `mapreduce_app/data/output.txt` e `mapreduce_app/data/livro_output.txt`.

## Próximos passos sugeridos
- Comitar alterações (já feitas no código para stopwords) e empurrar para seu fork:

```bash
git add mapreduce_app/mapper.py mapreduce_app/mapreduce_runner.py mapreduce_app/EVIDENCES.md
git commit -m "adiciona stopwords e relatório de evidências"
git push
```

---
Relatório gerado automaticamente pelo agente de execução local.
