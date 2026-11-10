# Metro Manila Rooftop Solar: slides

A single-page slide deck (title, problem, live dashboard, solution) analysing whether rooftop solar can
loosen Metro Manila's dependence on fossil fuel, Middle East oil and Meralco. Static site, no build step on Vercel.

## What is deployed
`public/index.html` only. It is self-contained (no external scripts, fonts or map tiles) and embeds the
interactive dashboard inside slide 3.

## Deploy to Vercel
**CLI**
```
npm i -g vercel
vercel          # first run links the project, accept the defaults
vercel --prod
```
**Git**: push this folder to GitHub, then Import Project in Vercel. Framework preset: Other.
`vercel.json` already sets the output directory to `public` and disables the build.

## Rebuild after editing
Edit the templates in `src/` (`slides_template.html`, `dashboard_template.html`), then run:
```
python3 src/build.py
```
This regenerates `public/index.html` from the templates, `src/data.json` (aggregated roof data) and `src/city.svg`.

## Presenting
Arrow keys / space to move, `F` for fullscreen, `#3` in the URL opens slide 3. Print to PDF gives one slide per page
(visit slide 3 first so the dashboard loads).

## Data and caveats
- Only aggregated figures (`src/data.json`, about 15 KB) are published. The row-level CSVs are excluded by
  `.gitignore` and `.vercelignore`. Confirm the source dataset's licence before publishing anything derived from it.
- Results are modelled technical potential. Metro Manila demand is derived (Meralco 2025 sales x an assumed 60% share),
  and coal share, oil share, tariff and emission factor are unverified placeholders. They are editable in the dashboard.
