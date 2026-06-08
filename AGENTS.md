# Agent Instructions

This is a static browser project.

The browser project also needs access to the huxley2 departure board API. Start it from the `huxley2/Huxley2` directory with:

```sh
docker compose up -d
```

When Codex needs to view or verify the project output in the in-app browser, run a local dev server from the project root with:

```sh
python3 -m http.server 8000
```

Then open:

```text
http://localhost:8000/
```
