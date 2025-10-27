# NetBox Binary Prefix

A simple NetBox plugin that patches the display of disk and memory sizes to use proper IEC binary prefixes (KiB, MiB, GiB, etc.) instead of the default decimal ones (KB, MB, GB).

## Compatibility

| NetBox Version | Plugin Version |
|----------------|----------------|
| 4.2            | 1.0.0          |
| 4.3            | 1.0.0          |
| 4.4            | 1.0.0          |


## Installation

Install the plugin from PyPI:

```bash
pip install netbox-binary-prefix
```

or by adding to your `local_requirements.txt` or `plugin_requirements.txt` (netbox-docker):

```bash
netbox-binary-prefix
```

Enable the plugin in `/opt/netbox/netbox/netbox/configuration.py`,
 or if you use netbox-docker, your `/configuration/plugins.py` file :

```python
PLUGINS = [
    "netbox_binary_prefix",
]
```

## Usage

Once installed and enabled, the plugin will automatically patch the `_humanize_megabytes` helper function to display sizes with binary units.

This functionality is dependent on the `DISK_BASE_UNIT` and `RAM_BASE_UNIT` configuration variables being set to `1024` as [documented here](https://netboxlabs.com/docs/netbox/configuration/miscellaneous/#disk_base_unit).