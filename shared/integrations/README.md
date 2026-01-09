# API Integrations

This folder contains optional integrations with external APIs. The Policy Council works out of the box with Claude Code's native capabilities, but can be extended with additional integrations for enhanced features.

## Default: Claude (Always Available)

The Policy Council runs entirely through Claude Code using the Task tool. No additional setup required.

**Capabilities:**
- Multi-agent orchestration via Task tool
- 6-agent parallel research
- Structured voting and deliberation
- Full 5-phase policy development workflow

## Optional: Gemini Integration

Enable Gemini for enhanced deep research capabilities (100+ sources).

**Setup:**
1. Set `GEMINI_API_KEY` environment variable
2. Configure `shared/integrations/gemini/config.yaml`
3. Use `/research --gemini` or `/deep-research` with Gemini mode

See `gemini/README.md` for detailed setup instructions.

## Future: OpenAI Integration

Placeholder for future OpenAI integration (legal analysis, etc.).

See `openai/README.md` for status.

---

## Configuration

The default integration settings are in `config.yaml`:

```yaml
default_model: claude
available_integrations:
  - claude    # Always available
  - gemini    # Optional, requires API key
  - openai    # Future placeholder
```

## Usage in Commands

Commands can specify which integration to use:

```bash
# Default (Claude)
/research AI policy frameworks

# With Gemini (if configured)
/research --gemini AI policy frameworks
/deep-research --model gemini AI taxation
```
