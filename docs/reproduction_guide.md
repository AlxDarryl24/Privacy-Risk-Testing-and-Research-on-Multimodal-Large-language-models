# Reproduction Guide

## Step 1: Install dependencies

```bash
pip install -r requirements.txt
```

## Step 2: Prepare datasets

Place full datasets locally under:

```text
data/raw/prism/
data/raw/multipriv/
data/raw/ap2/
```

Do not upload restricted or private raw data to GitHub.

## Step 3: Configure API keys

Copy `.env.example` to `.env` and add your real API keys.

```bash
cp .env.example .env
```

## Step 4: Run experiments

Replace placeholder scripts in `src/` with the actual implementation code. Then run the relevant scripts, for example:

```bash
python src/prism/run_prism_baseline.py
python src/prism/score_prism.py
```

## Step 5: Generate results

Save final tables to `results/tables/` and figures to `results/figures/`.
