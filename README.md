# nomad-econversion-plugins

Schema packages for the eConversion NOMAD Oasis
([`nomad-oasis-econversion`](https://github.com/cates-tum/nomad-oasis-econversion)).

One shared plugin repo for the cluster. Each schema or parser is a separate
`nomad.plugin` entry point here. A plugin is split into its own repo only when
it needs an external maintainer, a divergent release cadence, or has grown
large.

## Entry points

| Entry point | Type | Section |
|---|---|---|
| `grill_attempt` | schema package | `GrillAttempt` (`schema_packages/grill.py`) |

## Layout

```
src/nomad_econversion_plugins/
└── schema_packages/
    ├── __init__.py   entry point instances
    └── grill.py      m_package + section classes
```

## Use from the distribution

In the distro's `pyproject.toml`:

```toml
[project.optional-dependencies]
plugins = [
  "nomad-econversion-plugins @ git+https://github.com/cates-tum/nomad-econversion-plugins.git@v0.1.0",
]
```

then `uv lock` and rebuild the image.

## Develop

```
pip install -e '.[dev]'   # needs nomad-lab
python -c "from nomad_econversion_plugins.schema_packages.grill import GrillAttempt; print(GrillAttempt.m_def.name)"
```
