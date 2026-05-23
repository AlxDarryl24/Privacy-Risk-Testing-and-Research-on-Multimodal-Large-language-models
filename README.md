# Privacy Risk Testing and Research on Multimodal Large Language Models

This repository contains the implementation code and experimental materials for the thesis **"Privacy Risk Testing and Research on Multimodal Large Language Models"**.

The project evaluates privacy risks in multimodal large language models under black-box API settings using adapted versions of three benchmark-based frameworks:

- **PRISM**: multimodal user profile private attribute inference
- **MultiPriv**: vision-language privacy perception and reasoning
- **AP²**: audio-based private attribute profiling

The repository is designed to support reproducibility by providing scripts, prompts, sample data formats, configuration examples, result-processing templates, and documentation for the adapted baseline and enhanced evidence-based privacy evaluation pipelines.

## Repository Contents

```text
privacy-risk-mlmm-thesis/
├── README.md
├── requirements.txt
├── .gitignore
├── configs/
├── data/
├── prompts/
├── src/
├── results/
└── docs/
```

## Main Experiments

### 1. PRISM-style Attribute Inference
The PRISM experiment evaluates whether MLLMs can infer private attributes from synthetic multimodal user profiles. The implementation includes text-only and multimodal settings.

### 2. MultiPriv Vision-Language Privacy Reasoning
The MultiPriv experiment evaluates privacy perception and reasoning in vision-language models using image-based tasks and bilingual prompts.

### 3. AP²-style Audio Private Attribute Profiling
The AP² experiment evaluates whether models can infer private attributes from speech and audio cues. The enhanced version uses audio captioning, transcription, guidance, forensic validation, review, and consolidation.

## Enhanced Evidence-Based Evaluation

The enhanced method is designed to reduce unsupported guessing by requiring the model to extract evidence, apply structured reasoning, control uncertainty, and return `unknown` when the input does not provide sufficient support.

## Installation

Create a Python environment and install dependencies:

```bash
pip install -r requirements.txt
```

## API Configuration

Copy the example configuration file:

```bash
cp configs/model_config.example.yaml configs/model_config.yaml
```

Then edit `configs/model_config.yaml` and add your own API model names and environment variable names. Do **not** upload real API keys.

Recommended method:

```bash
cp .env.example .env
```

Then place your real API keys in `.env`. The `.env` file is ignored by Git.

## Data Policy

This repository does not include private API keys, restricted datasets, or large raw multimedia files. Only sample data formats are included. Users who want to reproduce the full experiments should prepare the corresponding benchmark datasets and configure their own API credentials.

## Reproducibility Notes

The repository includes:

- prompt templates
- sample data formats
- placeholder execution scripts
- scoring templates
- result table folders
- documentation for reproducing the experiment pipeline

The actual full datasets and raw multimedia files should be stored locally and excluded from GitHub if redistribution is not permitted.

## Thesis Citation

If using this repository, please cite the thesis:

Alexander Darryl Kristiawan. *Privacy Risk Testing and Research on Multimodal Large Language Models*. Beijing Institute of Technology, 2026.
