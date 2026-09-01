# Scores

- `without_charts/`: informative `?[]` chart transcriptions are removed symmetrically before scoring.
- `with_charts/`: informative chart transcription quality is included in the text-information module.

Each mode contains a CSV/JSON leaderboard and one directory per parser. Every parser directory contains a ten-document summary plus reproducible Markdown and JSON reports for 001–010. The `chart_score` leaderboard field is averaged only over Gold documents that contain informative chart objects (001–004); `text_score` is the score actually used by the selected mode.
