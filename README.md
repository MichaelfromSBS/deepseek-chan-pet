# 大肥鱼 · DeepSeek-chan

A blue-haired whale maid companion for Codex, inspired by the Chinese community character 大肥鱼 (DeepSeek-chan).

![DeepSeek-chan waving](preview/animations/waving.gif)
![A gentle little hop](preview/animations/jumping.gif)
![Rice break](preview/animations/failed.gif)

She waves with a small body sway, takes a gentle low hop, enjoys rice during setbacks, offers an empty bowl while waiting for input, and works on a laptop in her lap. The detailed chibi proportions and muted blue hair follow the approved character reference.

## Install in Codex

1. Download [deepseek-chan-v1.0.0.zip](releases/deepseek-chan-v1.0.0.zip).
2. Extract its `deepseek-chan` folder into your Codex home’s `pets` directory (on Windows, `%USERPROFILE%\.codex\pets\`). The result should be `pets/deepseek-chan/pet.json` alongside `spritesheet.webp`.
3. Open **Settings → Pets**, refresh the list, and select **大肥鱼 · DeepSeek-chan**. Use `/pet` to show the companion.

Back up an existing `deepseek-chan` folder before replacing it.

## Preview

Open [preview/index.html](preview/index.html) locally in a browser. It shows all nine animations with pause, background, and size controls. Individual GIFs are in [preview/animations](preview/animations), and the [contact sheet](preview/contact-sheet.png) shows every frame.

## Files

| Folder | Contents |
| --- | --- |
| `pet/deepseek-chan/` | Ready-to-install native package |
| `releases/` | Install ZIP and SHA-256 checksums |
| `preview/` | Browser preview, nine GIFs, contact sheet |
| `source/` | Approved design and selected generation prompts |
| `docs/` | Animation specification and credits |
| `scripts/` | Structural validation helper |

Release **1.0.0** uses the approved **artwork revision 3**. The transparent v1 atlas is 1536 × 1872 pixels, with 192 × 208 cells and 57 animation frames across nine states. The gentle jump is the final revision; the other eight states retain their approved artwork.

To check the package, install Pillow (`python -m pip install Pillow`) and run `python scripts/validate.py`. Exact frame counts and timing are recorded in [animation-spec.json](docs/animation-spec.json).

## Credits and use

This is a fan project with AI-assisted artwork and animation. It is not affiliated with DeepSeek or OpenAI. See [ATTRIBUTION.md](docs/ATTRIBUTION.md) for character credit and usage notes.
