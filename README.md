# llm-playground

## Requirements
```shell
brew install uv
```

## Install
```shell
cd llm-playground
cp .env.example .env
uv sync
```

## LiteLLM proxy server
```shell
uv run --env-file.env litellm --config litellm/config.yaml --detailed_debug
```
