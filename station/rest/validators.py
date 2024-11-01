from pydantic import ValidationInfo, field_validator


class NotEmptyLinesAndColorsValidatorMixin:
    # noinspection PyNestedDecorators
    @field_validator("lines", "colors")
    @classmethod
    def validate_lines_and_colors(cls, v: list, info: ValidationInfo):
        assert len(v) != 0, f"Empty {info.field_name} is not acceptable."
        return v
