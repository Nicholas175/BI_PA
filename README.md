# BI_PA

This repository contains a basic project structure for a Business Intelligence & Process Analysis pipeline.

The project follows the process:

1. **Raw Data** – data is collected from various public sources (e.g., satellite APIs, ISS, JWST).
2. **ETL** – extract, transform and load the data; includes harmonizing units and performing incremental loads.
3. **Data Warehouse** – a MySQL-based store for processed data.
4. **Reporting** – Python scripts for analysis and visualization.

Folder overview:

- `rawdata/` – sample location for raw data files.
- `etl/` – Python scripts for data ingestion and transformation.
- `dwh/` – SQL scripts to build and manage the MySQL data warehouse.
- `reporting/` – Python notebooks or scripts for reporting.

This serves as a minimal starting point for building the pipeline described above.
