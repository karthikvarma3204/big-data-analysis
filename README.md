# Sales Data Exploration with Dask

A learning exercise using Dask DataFrame to read CSV sales records and calculate summary statistics, missing-value counts, category-level average sales, and category frequency.

## Run
```bash
python -m pip install -r requirements.txt
python big_data_analysis.py
```

The script reads `sales_data_sample (1).csv`, which is included in this repository, and writes `processed_sales_data.csv`. The original analysis summary is in `insights (1).txt`.

**Note:** The existing insight file reports one million records; the included sample CSV is much smaller. The insight figures should therefore be treated as a previous illustrative run, not as reproducible statistics for the repository's bundled sample.

This is an educational Dask exercise, not a distributed production workload.
