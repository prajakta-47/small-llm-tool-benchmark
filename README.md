# Ultra Small Language Models Benchmarking for Tool-Calling Judgment

A lightweight benchmarking framework for evaluating small language models (LLMs) on tool-calling judgment, reasoning, and AI-agent workflows using Ollama and Python.

This project benchmarks how effectively compact LLMs:

* select the correct tool,
* avoid unnecessary tool calls,
* execute sequential workflows,
* perform conditional reasoning,
* and handle multi-step AI-agent tasks.

---

# Models Evaluated

| Model           | Parameters |
| --------------- | ---------- |
| phi4-mini       | 3.8B       |
| qwen3           | 0.6B       |
| qwen3           | 4B         |
| qwen2.5         | 1.5B       |
| lfm2.5-thinking | 1.2B       |

---

# Features

* Automated AI-agent benchmarking
* Local LLM inference using Ollama
* Tool-calling evaluation
* Multi-model comparison
* Prompt engineering framework
* Sequential reasoning evaluation
* Conditional workflow testing
* Lightweight CPU-compatible execution

---

# Benchmark Categories

The benchmark prompts are divided into multiple categories:

| Category                | Purpose                                |
| ----------------------- | -------------------------------------- |
| Direct Tool Usage       | Tests correct tool selection           |
| Tool Avoidance          | Tests unnecessary tool-call avoidance  |
| Conditional Reasoning   | Tests logical decision making          |
| Multi-tool Calling      | Tests sequential workflows             |
| Adversarial Prompts     | Tests ambiguity handling               |
| Comparative Reasoning   | Tests analytical reasoning             |
| Sequential Instructions | Tests ordered execution                |
| Tool Awareness          | Tests understanding of available tools |

---

# Tools Used

The following simulated tools were exposed to the models:

| Tool              | Description                    |
| ----------------- | ------------------------------ |
| get_machine_state | Retrieve machine/server status |
| get_weather       | Retrieve weather information   |
| validate_switch   | Verify switch status           |
| setup_meeting     | Schedule meetings              |
| get_population    | Retrieve population statistics |

---

# Project Workflow

```text id="gb2jlwm"
Prompt
   ↓
Model Inference
   ↓
Tool Call Detection
   ↓
Tool Execution
   ↓
Final Response
   ↓
Evaluation & Scoring
```

---

# Installation

## 1. Install Ollama

[Ollama Official Website](https://ollama.com?utm_source=chatgpt.com)

---

## 2. Install Python Dependencies

```bash id="9jlwmc"
pip install ollama
```

---

## 3. Pull Required Models

```bash id="9qv0w8"
ollama pull phi4-mini:3.8b
ollama pull qwen3:0.6b
ollama pull qwen3:4b
ollama pull qwen2.5:1.5b
ollama pull lfm2.5-thinking:1.2b
```

---

# Running the Benchmark

## Start Ollama

```bash id="8wjlwm"
ollama serve
```

---

## Run Benchmark Script

```bash id="jlwm12"
python benchmark.py
```

---

# Experimental Setup

| Component      | Details                       |
| -------------- | ----------------------------- |
| Framework      | Ollama                        |
| Language       | Python                        |
| Hardware       | CPU-based local system        |
| Inference Type | Local inference               |
| Benchmark Type | Automated AI-agent evaluation |

---

# Evaluation Metrics

| Metric               | Description                         |
| -------------------- | ----------------------------------- |
| Action Score         | Correct tool usage                  |
| Restraint Score      | Avoidance of unnecessary tool calls |
| Wrong Tool Calls     | Incorrect tool usage                |
| Wrong-Tool-Avoidance | Ability to avoid incorrect tools    |
| Agent Score          | Overall AI-agent capability         |

---

# Final Benchmark Results

| Model                | Action Score | Restraint Score | Wrong-Tool-Avoidance | Agent Score |
| -------------------- | ------------ | --------------- | -------------------- | ----------- |
| qwen3:4b             | 1.0          | 0.5             | 1.0                  | 0.85        |
| qwen2.5:1.5b         | 0.8          | 0.5             | 1.0                  | 0.77        |
| qwen3:0.6b           | 0.7          | 0.5             | 1.0                  | 0.73        |
| lfm2.5-thinking:1.2b | 0.7          | 0.5             | 1.0                  | 0.73        |
| phi4-mini:3.8b       | 0.3          | 1.0             | 1.0                  | 0.72        |

---

# Key Observations

* Larger models performed better on sequential workflows.
* Lightweight models demonstrated strong local inference capability.
* Tool-restraint significantly improved reliability.
* Small LLMs are increasingly practical for local AI-agent systems.

---

# Folder Structure

```text id="jlwmfs"
.
├── benchmark.py
├── README.md
├── screenshots/
├── outputs/
├── report/
└── requirements.txt
```

---


# References

* Ollama Documentation
* Open-source Tool Calling Benchmarks
* Reddit Tool Calling Benchmark Discussions
* Local LLM Research Papers

---


AI-agent benchmarking project focused on lightweight local language models and tool-calling evaluation.
