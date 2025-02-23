from typing import Any, Dict, Optional

from pydantic.fields import FieldInfo

from ninja import params_models

__all__ = ["Param", "Path", "Query", "Header", "Cookie", "Body", "Form", "File"]


class Param(FieldInfo):
    def __init__(
        self,
        default: Any,
        *,
        alias: str = None,
        title: str = None,
        description: str = None,
        gt: float = None,
        ge: float = None,
        lt: float = None,
        le: float = None,
        min_length: int = None,
        max_length: int = None,
        regex: str = None,
        example: Any = None,
        examples: Optional[Dict[str, Any]] = None,
        deprecated: bool = None,
        include_in_schema: bool = True,
        # param_name: str = None,
        # param_type: Any = None,
        **extra: Any,
    ):
        self.deprecated = deprecated
        # self.param_name: str = None
        # self.param_type: Any = None
        self.model_field: Optional[FieldInfo] = None
        json_schema_extra = {}
        if example:
            json_schema_extra["example"] = example
        if examples:
            json_schema_extra["examples"] = examples
        if deprecated:
            json_schema_extra["deprecated"] = deprecated
        if not include_in_schema:
            json_schema_extra["include_in_schema"] = include_in_schema
        if alias and not extra.get("validation_alias"):
            extra["validation_alias"] = alias
        if alias and not extra.get("serialization_alias"):
            extra["serialization_alias"] = alias
        super().__init__(
            default=default,
            alias=alias,
            title=title,
            description=description,
            gt=gt,
            ge=ge,
            lt=lt,
            le=le,
            min_length=min_length,
            max_length=max_length,
            regex=regex,
            json_schema_extra=json_schema_extra,
            **extra,
        )

    @classmethod
    def _param_source(cls) -> str:
        "Openapi param.in value or body type"
        return cls.__name__.lower()


class Path(Param):
    _model = params_models.PathModel


class Query(Param):
    _model = params_models.QueryModel


class Header(Param):
    _model = params_models.HeaderModel


class Cookie(Param):
    _model = params_models.CookieModel


class Body(Param):
    _model = params_models.BodyModel


class Form(Param):
    _model = params_models.FormModel


class File(Param):
    _model = params_models.FileModel


class _MultiPartBody(Param):
    _model = params_models._MultiPartBodyModel

    @classmethod
    def _param_source(cls) -> str:
        return "body"
