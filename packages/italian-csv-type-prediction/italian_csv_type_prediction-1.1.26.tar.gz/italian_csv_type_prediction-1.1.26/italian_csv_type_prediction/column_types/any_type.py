from typing import Dict, List

from .column_type_predictor import ColumnTypePredictor
from .single_type_column import (AddressType, BiologicalSexType, BooleanType,
                                 ItalianZIPCodeType, ItalianFiscalCodeType, CountryCodeType,
                                 CountryType, DateType,
                                 DocumentType, EMailType, FloatType,
                                 IntegerType, ItalianVATType, MunicipalityType,
                                 NameType, NaNType, PhoneNumberType, PlateType,
                                 ProvinceCodeType, RegionType, StringType,
                                 SurnameType, YearType, CadastreCodeType, TaxType
                                 )


class AnyTypePredictor:
    def __init__(self):
        self._predictors = [
            predictor()
            for predictor in (
                AddressType, ItalianZIPCodeType, ItalianFiscalCodeType, CountryCodeType,
                CountryType, DateType, EMailType, TaxType,
                FloatType, IntegerType, ItalianVATType, DocumentType,
                MunicipalityType, NameType, NaNType, PhoneNumberType,
                ProvinceCodeType, RegionType, StringType, SurnameType,
                YearType, BiologicalSexType, BooleanType, PlateType, CadastreCodeType
            )
        ]

    @property
    def supported_types(self):
        """Return list of currently supported types."""
        return [
            predictor.name
            for predictor in self._predictors
        ]

    @property
    def predictors(self) -> List[ColumnTypePredictor]:
        return self._predictors

    def predict(self, values: List, fiscal_codes: List[str] = (), ivas: List[str] = (), **kwargs) -> Dict[str, List[bool]]:
        """Return prediction from all available type."""
        return {
            predictor.name: predictor.validate(
                values,
                fiscal_codes=fiscal_codes,
                ivas=ivas,
                **kwargs
            )
            for predictor in self._predictors
        }
