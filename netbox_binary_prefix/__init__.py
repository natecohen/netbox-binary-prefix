from netbox.plugins import PluginConfig
from importlib.metadata import version

__version__ = version("netbox-binary-prefix")


class BinaryUnitsConfig(PluginConfig):
    name = "netbox_binary_prefix"
    verbose_name = "NetBox Binary Prefix"
    version = __version__
    description = "NetBox plugin to display disk and memory units with IEC binary prefixes"
    author = "Nate Cohen"
    author_email = "94263748+natecohen@users.noreply.github.com"
    min_version = "4.2.6"
    max_version = "4.5.99"

    def ready(self):
        super().ready()

        from utilities.templatetags import helpers

        def _humanize_megabytes_binary(mb, divisor=1000):
            if not mb:
                return ""

            is_binary = divisor == 1024
            suffix = "iB" if is_binary else "B"

            PB_SIZE = divisor**3
            TB_SIZE = divisor**2
            GB_SIZE = divisor

            if mb >= PB_SIZE:
                return f"{mb / PB_SIZE:.2f} P{suffix}"
            if mb >= TB_SIZE:
                return f"{mb / TB_SIZE:.2f} T{suffix}"
            if mb >= GB_SIZE:
                return f"{mb / GB_SIZE:.2f} G{suffix}"
            return f"{mb} M{suffix}"

        helpers._humanize_megabytes = _humanize_megabytes_binary


config = BinaryUnitsConfig
