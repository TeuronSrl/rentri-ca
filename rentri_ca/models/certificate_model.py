# coding: utf-8

"""
    ca-rentri

    Servizio RENTRI CA

    The version of the OpenAPI document: 1.0.20250114-613
    Contact: techref@rentri.it
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class CertificateModel(BaseModel):
    """
    CertificateModel
    """ # noqa: E501
    certificato: Optional[StrictStr] = None
    subject: Optional[StrictStr] = None
    data_rilascio: Optional[datetime] = Field(default=None, description="Formato ISO 8601 UTC")
    data_scadenza: Optional[datetime] = Field(default=None, description="Formato ISO 8601 UTC")
    __properties: ClassVar[List[str]] = ["certificato", "subject", "data_rilascio", "data_scadenza"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of CertificateModel from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if certificato (nullable) is None
        # and model_fields_set contains the field
        if self.certificato is None and "certificato" in self.model_fields_set:
            _dict['certificato'] = None

        # set to None if subject (nullable) is None
        # and model_fields_set contains the field
        if self.subject is None and "subject" in self.model_fields_set:
            _dict['subject'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CertificateModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "certificato": obj.get("certificato"),
            "subject": obj.get("subject"),
            "data_rilascio": obj.get("data_rilascio"),
            "data_scadenza": obj.get("data_scadenza")
        })
        return _obj


