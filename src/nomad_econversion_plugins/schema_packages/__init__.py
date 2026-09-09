from nomad.config.models.plugins import SchemaPackageEntryPoint


class GrillAttemptEntryPoint(SchemaPackageEntryPoint):
    def load(self):
        from nomad_econversion_plugins.schema_packages.grill import m_package

        return m_package


grill_attempt = GrillAttemptEntryPoint(
    name="Grill attempt schema",
    description="ELN schema for one grilling attempt on the grilling bench.",
)
