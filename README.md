# The World — 24 November 2026, in One Image

[![news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/h05meigames2/news-24nov26-frontpage-r2/rank.svg)](https://make.fun/bounty/news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/h05meigames2/news-24nov26-frontpage-r2/reward.svg)](https://make.fun/bounty/news-image-20261124)

[Bounty: news-image-20261124](https://make.fun/bounty/news-image-20261124)

A program that sums up Tuesday 24 November 2026's world news in a single
1024×1024 front-page-style image, drawn deterministically with Python PIL —
no network calls, no downloaded assets, no randomness.

## The day's biggest stories

- **Lead:** factory fire in Banten, Indonesia — at least 24 killed, around
  30 workers missing as rescuers search the ruins.
- **War in Europe:** Russian drone and missile strikes hit Ukraine's Kyiv
  region; a Russian cargo ship burns in the Gulf of Finland after a drone
  attack; a Russian corvette is reported destroyed in Benghazi, Libya.
- **Climate:** COP31 in Antalya, Türkiye, ends without agreement on
  fossil-fuel language.
- **Europe:** thousands march in Lisbon against the rising cost of living.
- **Diplomacy:** India and Nepal open the Saryu-Kamala Express rail link.
- **Sport:** Carlos Alcaraz wins the ATP Finals; Max Verstappen wins the
  Las Vegas Grand Prix; Rishabh Pant hits 128 in Wellington.

## Run it

```bash
python3 main.py
```

This writes the image to `/output/entry.png` (1024×1024 PNG).

## Layout

- `main.py` — entrypoint; runs the generator and writes `/output/entry.png`.
- `gen_image.py` — the front-page renderer (masthead, lead story, columns,
  footer strip), built from scratch with PIL.
