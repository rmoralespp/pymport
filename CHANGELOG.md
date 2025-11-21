## Releases

- **Added:** Add **pre-commit** hook support

### v0.0.5 (2025-11-13)

- **Fixed:** Avoid always logs warnings when using the `--quiet` option

### v0.0.4 (2025-11-12)

- **Added:** Log unknown passed files.
- **Change:** Limit the minimum Python version to 3.12 because several features of `pathlib` used are introduced in this version.
- **Change:** Update README.md with `# noqa` instructions for ignoring unused imports.

### v0.0.3 (2025-10-30)

- **Added:** Option `--ignore` to exclude specified directories from linting.
- **Added:** Quiet mode with `--quiet` option to reduce output verbosity.

### v0.0.2 (2025-10-23)

- **Added:** Include PyPI badge in **README.md** and update **features** section.
- **Added:** Print success message when no issues are found.
- **Fixed:** Ruff `warning: `RUF025` has been remapped to `C420`.

### v0.0.1 (2025-10-23)

- **Added:** Entrypoint for using the tool as a **CLI** app.
- **Added:** **CI/CD** pipeline configuration.
- **Added:** Basic functionality for checking unused imports.
- **Added:** Initial project setup and structure.
