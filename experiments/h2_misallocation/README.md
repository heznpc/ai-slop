# H2: Research Misallocation (Bibliometric Test)

Pre-registered experiment testing Hypothesis 2 from the Perspectives paper:

> *The number of published detection studies per format is inversely correlated with the production-detection asymmetry of that format.*

## Status

| | |
|---|---|
| Pre-registration | `protocol.md` (locked 2026-05-21) |
| Decision log | `../../planning/decisions.md` (2026-05-21 entry) |
| Paper cross-refs | `papers/perspectives/paper/main.tex` H2 paragraph; `papers/framework/paper/main.tex` §4.2 |

## Layout

```
h2_misallocation/
├── README.md               You are here
├── protocol.md             Locked methodology (single source of truth)
├── run.py                  Executes the pre-registered protocol end-to-end
├── results/
│   ├── raw/                Cached Semantic Scholar JSON, one per query
│   ├── paper_counts.csv    Per-format final tally
│   ├── stats.json          Spearman ρ, p, bootstrap CI
│   ├── run_metadata.json   Snapshot date, API call count, version header
│   └── limitations.md      Any deviations or failure-mode notes
```

## Run

```bash
python3 run.py
```

Requires only the Python standard library plus `scipy`, `numpy`, `pandas`, `requests`. No paid API keys. No GPU.

## Interpreting the result

Per `protocol.md`:
- $\rho < 0, p < 0.05$ → consistent with H2 (Research Misallocation)
- $\rho \ge 0$ or $p \ge 0.05$ → H2 is **not supported by this test** at $\alpha=0.05$ one-sided

The result is one bibliometric snapshot from one database under one keyword set. Limitations are in `protocol.md` ("What this protocol does NOT do").
