# Gemini Integration (Optional)

The Gemini integration enables enhanced deep research capabilities using Google's Gemini API with grounding.

## Features

- **Deep Research** with 100+ sources
- **Grounding** with Google Search for real-time information
- **Slide generation** for presentations

## Setup

### 1. Get Gemini API Key

1. Go to [Google AI Studio](https://aistudio.google.com/)
2. Create an API key
3. Set the environment variable:
   ```bash
   export GEMINI_API_KEY=your-api-key
   ```

### 2. Configure Integration

Edit `config.yaml` in this folder:

```yaml
enabled: true
api_key_env: GEMINI_API_KEY
model: gemini-2.0-flash-exp  # or gemini-1.5-pro
```

### 3. Enable in Main Config

Edit `shared/integrations/config.yaml`:

```yaml
integrations:
  gemini:
    enabled: true
```

## Usage

```bash
# Explicit Gemini usage
/research --gemini AI policy frameworks
/deep-research --model gemini AI taxation

# Deep research defaults to Gemini if configured
/deep-research Algorithmic accountability
```

## Workflows

### Deep Research Workflow

See `deep_research.md` for the full deep research workflow using Gemini.

### Slide Generation

See `slides.md` for generating presentation slides from policy documents.

## Costs

Gemini API usage incurs costs. Monitor your usage at Google AI Studio.

## Troubleshooting

| Issue | Solution |
|-------|----------|
| API key not found | Ensure `GEMINI_API_KEY` is set in environment |
| Rate limits | Reduce concurrent requests or upgrade quota |
| Grounding errors | Check Google Search API status |
