# Local-Only Policy

This project is configured for laptop-local development only.

## Rules

- Do not publish to GitHub or any remote by default.
- Keep data, drafts, and artifacts local unless explicitly approved for release.
- Treat `publish_to_github.sh` as blocked unless `ALLOW_REMOTE_PUBLISH=1` is intentionally set.

## Intentional Override

If and only if you decide to publish:

```bash
ALLOW_REMOTE_PUBLISH=1 ./publish_to_github.sh <owner> <repo> [public|private]
```
