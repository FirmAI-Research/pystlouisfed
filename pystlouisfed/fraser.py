import logging
from typing import NoReturn
from typing import Optional

from sickle import Sickle
from sickle.iterator import BaseOAIIterator
from sickle.models import Record

logger = logging.getLogger(__name__)


class FRASER:
    """
    FRASER is a digital library of U.S. economic, financial, and banking history—particularly the history of the Federal Reserve System.

    Providing economic information and data to the public is an important mission for the St. Louis Fed started by former St. Louis Fed Research Director Homer Jones in 1958.
    FRASER began as a data preservation and accessibility project of the Federal Reserve Bank of St. Louis in 2004 and now provides access to data and policy documents from the Federal Reserve System and many other institutions.

    https://fraser.stlouisfed.org/
    https://research.stlouisfed.org/docs/api/fraser/
    """

    def __init__(self) -> NoReturn:
        self._sickle = Sickle("https://fraser.stlouisfed.org/oai")

    def list_records(self, ignore_deleted: bool = False, set: Optional[str] = None) -> BaseOAIIterator:
        """
        :param ignore_deleted: bool, 
        :param set: Optional[str], This parameter specifies the setSpec value and limits the records that are retrieved to only those in the specified set. Ignore this parameter to return all records.
        :return: :py:class:`sickle.iterator.BaseOAIIterator`
         
        Description
        -----------
        | https://research.stlouisfed.org/docs/api/fraser/listRecords.html
        | This request returns title records from the FRASER repository.
        | A resumptionToken can be used to retrieve all records using multiple requests.
        | Additional information about an individual title, including the title's child records, can be retrieved using the GetRecord request.

        API Request
        -----------
        https://fraser.stlouisfed.org/oai/?verb=ListRecords&metadataPrefix=mods&resumptionToken=1469299598:0

        Example
        -------
        .. code-block:: python
        
           from pystlouisfed import FRASER

           for record in FRASER().list_records():
               print(record.get_metadata())
        """  # noinspection

        return self._sickle.ListRecords(metadataPrefix="mods", ignore_deleted=ignore_deleted, set=set)

    def list_sets(self) -> BaseOAIIterator:
        """
        :return: :py:class:`sickle.iterator.BaseOAIIterator`
        
        Description
        -----------
        | https://research.stlouisfed.org/docs/api/fraser/listSets.html
        | This request returns the set structure for records in the FRASER repository.
        | A resumptionToken can be used to retrieve the complete set structure using multiple requests.

        API Request
        -----------
        https://fraser.stlouisfed.org/oai/?verb=ListSets&resumptionToken=1478707638:0

        Example
        -------
        .. code-block:: python
        
           from pystlouisfed import FRASER

           for set in FRASER().list_sets():
               print(set)
        """  # noinspection

        return self._sickle.ListSets()

    def list_identifiers(self, ignore_deleted: bool = False, set: Optional[str] = None) -> BaseOAIIterator:
        """
        :param ignore_deleted: bool
        :param set: str, This parameter specifies the setSpec value and limits the records that are retrieved to only those in the specified set Ignore this parameter to return all records.
        :return: :py:class:`sickle.iterator.BaseOAIIterator`
        
        Description
        -----------
        | https://research.stlouisfed.org/docs/api/fraser/listIdentifiers.htm
        | This request returns headers for records in the FRASER repository.
        | A resumptionToken can be used to retrieve all records using multiple requests.

        API Request
        -----------
        https://fraser.stlouisfed.org/oai/?verb=ListIdentifiers&resumptionToken=1469300451:0

        Example
        -------
        .. code-block:: python
        
           from pystlouisfed import FRASER

           for header in FRASER().list_identifiers():
               print(header.identifier)
        """  # noinspection

        return self._sickle.ListIdentifiers(metadataPrefix="mods", ignore_deleted=ignore_deleted, set=set)

    def get_record(self, identifier: str) -> Record:
        """
        :param identifier: str
        :return: :py:class:`sickle.models.Record`
        
        Description
        -----------
        | https://research.stlouisfed.org/docs/api/fraser/getRecord.html
        | This request returns a single record from the FRASER repository.

        API Request
        -----------
        https://fraser.stlouisfed.org/oai/?verb=GetRecord&identifier=oai:fraser.stlouisfed.org:title:176     

        Example
        -------
        .. code-block:: python
        
           from pystlouisfed import FRASER

            RASER().get_record(identifier='oai:fraser.stlouisfed.org:title:176')
        """  # noinspection

        return self._sickle.GetRecord(identifier=identifier, metadataPrefix="mods")