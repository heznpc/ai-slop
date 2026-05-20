# H2 Run Limitations

Snapshot: 2026-05-20T18:18:00.653575+00:00
Data source: OpenAlex Works API (polite pool, mailto=wantcongz@gmail.com)

- API call count: 80
- Failed queries: 0

## Formats with at least one query whose reported_total exceeded the 5000-result page-paginated cap

- **video** — actual count for those queries may be undercounted; first 5000 results retrieved per query and deduped across queries.

Rank ordering of formats by deduped_count is preserved as long as capped formats are the higher-count ones, which is the direction H2 predicts.

## Spot-check

5 random sample titles per format are recorded in `spot_check.json` to verify queries returned topical results, not noise.
