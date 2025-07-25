# coding: utf-8

"""
    ca-rentri

    Servizio RENTRI CA

    The version of the OpenAPI document: 1.0.20250114-613
    Contact: techref@rentri.it
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from rentri_ca.api.csc_firma_remota_rentri_api import CSCFirmaRemotaRENTRIApi


class TestCSCFirmaRemotaRENTRIApi(unittest.TestCase):
    """CSCFirmaRemotaRENTRIApi unit test stubs"""

    def setUp(self) -> None:
        self.api = CSCFirmaRemotaRENTRIApi()

    def tearDown(self) -> None:
        pass

    def test_credentials_authorize_check_handle_get(self) -> None:
        """Test case for credentials_authorize_check_handle_get

        Verifica autorizzazione credenziali
        """
        pass

    def test_credentials_authorize_check_handle_get_0(self) -> None:
        """Test case for credentials_authorize_check_handle_get_0

        ⚠️[DEPRECATO] - utilizzare /credentials/authorize-check/{handle} - Verifica autorizzazione credenziali
        """
        pass

    def test_credentials_authorize_confirmation_put(self) -> None:
        """Test case for credentials_authorize_confirmation_put

        Imposta autorizzazione credenziali
        """
        pass

    def test_credentials_authorize_confirmation_put_0(self) -> None:
        """Test case for credentials_authorize_confirmation_put_0

        ⚠️[DEPRECATO] - utilizzare /credentials/authorize-confirmation - Imposta autorizzazione credenziali
        """
        pass

    def test_credentials_authorize_post(self) -> None:
        """Test case for credentials_authorize_post

        Autorizza credenziali
        """
        pass

    def test_credentials_info_get(self) -> None:
        """Test case for credentials_info_get

        Informazioni credenziali
        """
        pass

    def test_credentials_list_get(self) -> None:
        """Test case for credentials_list_get

        Elenco credenziali soggetto
        """
        pass

    def test_credentials_post(self) -> None:
        """Test case for credentials_post

        Crea/aggiorna credenziali
        """
        pass

    def test_info_get(self) -> None:
        """Test case for info_get

        Info servizio
        """
        pass

    def test_signatures_sign_hash_post(self) -> None:
        """Test case for signatures_sign_hash_post

        Firma hash
        """
        pass

    def test_signatures_sign_hash_post_0(self) -> None:
        """Test case for signatures_sign_hash_post_0

        ⚠️[DEPRECATO] - utilizzare /signatures/sign-hash - Firma hash
        """
        pass


if __name__ == '__main__':
    unittest.main()
