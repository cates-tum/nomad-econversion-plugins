"""Grill attempt ELN schema.

Python port of examples/grill-attempt/grill_attempt.archive.yaml in the
nomad-oasis-econversion distribution. One grilling attempt on the grilling
bench, collapsed from the Nexus grill_red_meat / grill_poultry / grill_fish
schemas plus base_recipe_attempt.
"""

from nomad.datamodel.data import EntryData
from nomad.datamodel.metainfo.annotations import ELNAnnotation, ELNComponentEnum
from nomad.datamodel.metainfo.eln import ELNMeasurement
from nomad.metainfo import MEnum, Quantity, SchemaPackage, Section

m_package = SchemaPackage()


class GrillAttempt(ELNMeasurement, EntryData):
    m_def = Section(
        a_eln=ELNAnnotation(
            hide=[
                'lab_id',
                'location',
                'method',
                'tags',
                'steps',
                'samples',
                'instruments',
                'measurement_identifiers',
            ],
        ),
    )

    cuisine = Quantity(
        type=str,
        a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
    )
    protein_class = Quantity(
        type=MEnum('red_meat', 'poultry', 'fish', 'vegetable'),
        a_eln=ELNAnnotation(component=ELNComponentEnum.EnumEditQuantity),
    )
    cut = Quantity(
        type=str,
        description='e.g. ribeye, thigh, fillet. Free text, protein dependent.',
        a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
    )
    heat_source = Quantity(
        type=MEnum('grill', 'pan', 'oven'),
        a_eln=ELNAnnotation(component=ELNComponentEnum.RadioEnumEditQuantity),
    )
    grill_temp = Quantity(
        type=float,
        unit='celsius',
        description='Grill surface temperature.',
        a_eln=ELNAnnotation(
            component=ELNComponentEnum.NumberEditQuantity,
            defaultDisplayUnit='celsius',
        ),
    )
    cook_time = Quantity(
        type=float,
        unit='minute',
        a_eln=ELNAnnotation(
            component=ELNComponentEnum.NumberEditQuantity,
            defaultDisplayUnit='minute',
        ),
    )
    internal_temp = Quantity(
        type=float,
        unit='celsius',
        description='Final internal temperature.',
        a_eln=ELNAnnotation(
            component=ELNComponentEnum.NumberEditQuantity,
            defaultDisplayUnit='celsius',
        ),
    )
    usda_safe_min = Quantity(
        type=float,
        unit='celsius',
        description=(
            'USDA minimum safe internal temperature for this protein class '
            '(red meat 63, poultry 74, fish 63).'
        ),
        a_eln=ELNAnnotation(
            component=ELNComponentEnum.NumberEditQuantity,
            defaultDisplayUnit='celsius',
        ),
    )
    rested_min = Quantity(
        type=float,
        unit='minute',
        description='Rest time after cooking.',
        a_eln=ELNAnnotation(
            component=ELNComponentEnum.NumberEditQuantity,
            defaultDisplayUnit='minute',
        ),
    )
    doneness = Quantity(
        type=MEnum(
            'rare',
            'medium_rare',
            'medium',
            'medium_well',
            'well_done',
            'not_applicable',
        ),
        a_eln=ELNAnnotation(component=ELNComponentEnum.EnumEditQuantity),
    )
    char_level = Quantity(
        type=float,
        description='Char level, 0 to 100.',
        a_eln=ELNAnnotation(component=ELNComponentEnum.NumberEditQuantity),
    )
    juiciness_score = Quantity(
        type=float,
        description='Juiciness, 0 to 100.',
        a_eln=ELNAnnotation(component=ELNComponentEnum.NumberEditQuantity),
    )
    outcome = Quantity(
        type=MEnum('undercooked', 'perfect', 'overcooked'),
        a_eln=ELNAnnotation(component=ELNComponentEnum.RadioEnumEditQuantity),
    )


m_package.__init_metainfo__()
