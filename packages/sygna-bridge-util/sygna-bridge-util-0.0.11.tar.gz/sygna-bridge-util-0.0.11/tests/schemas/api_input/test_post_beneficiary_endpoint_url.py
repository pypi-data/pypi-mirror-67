import pytest
from sygna_bridge_util.schemas import get_post_beneficiary_endpoint_url_schema
from jsonschema import validate, ValidationError, draft7_format_checker


def test_get_post_beneficiary_endpoint_url_schema():
    """should raise exception if get_post_beneficiary_endpoint_url_schema result is not expected"""
    __post_beneficiary_endpoint_url_schema = {
        "type": "object",
        "properties": {
            "vasp_code": {
                "type": "string",
                "minLength": 1
            },
            "beneficiary_endpoint_url": {
                "type": "string",
                "format": "uri"
            },
            "signature": {
                "type": "string",
                "minLength": 128,
                "maxLength": 128,
                "pattern": "^[0123456789A-Fa-f]+$"
            }
        },
        "required": [
            "vasp_code",
            "beneficiary_endpoint_url",
            "signature"
        ],
        "additionalProperties": False
    }
    assert __post_beneficiary_endpoint_url_schema == get_post_beneficiary_endpoint_url_schema()


def test_post_beneficiary_endpoint_url_schema():
    """should raise exception if data is mot match schema"""

    def assert_validate_result(instance: dict, expected_message: str) -> None:
        with pytest.raises(ValidationError) as exception:
            validate(instance=instance, schema=get_post_beneficiary_endpoint_url_schema(),
                     format_checker=draft7_format_checker)
        assert expected_message == str(exception.value.message)

    data = {}
    assert_validate_result(data, "'vasp_code' is a required property")

    data['vasp_code'] = 123
    assert_validate_result(data, "'beneficiary_endpoint_url' is a required property")

    data['beneficiary_endpoint_url'] = 123
    assert_validate_result(data, "'signature' is a required property")

    data['signature'] = 123
    assert_validate_result(data, "{0} is not of type 'string'".format(data['vasp_code']))

    data['vasp_code'] = ''
    assert_validate_result(data, "'{0}' is too short".format(data['vasp_code']))

    data['vasp_code'] = 'VASPUSNY1'
    assert_validate_result(data, "{0} is not of type 'string'".format(data['beneficiary_endpoint_url']))

    data['beneficiary_endpoint_url'] = '123'
    assert_validate_result(data, "'{0}' is not a 'uri'".format(data['beneficiary_endpoint_url']))

    data['beneficiary_endpoint_url'] = 'https://api.sygna.io/api/v1.1.0/bridge/'
    assert_validate_result(data, "{0} is not of type 'string'".format(data['signature']))

    data['signature'] = '123'
    assert_validate_result(data, "'{0}' is too short".format(data['signature']))

    data['signature'] = '6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52d' \
                        'db7875b4b6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b1'  # len = 129
    assert_validate_result(data, "'{0}' is too long".format(data['signature']))

    data['signature'] = 'ggg6b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52d' \
                        'db7875b4b6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b'  # len = 128
    assert_validate_result(data, "'{0}' does not match '^[0123456789A-Fa-f]+$'".format(data['signature']))

    data['signature'] = '6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52d' \
                        'db7875b4b6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b'  # len = 128

    try:
        validate(instance=data, schema=get_post_beneficiary_endpoint_url_schema(), format_checker=draft7_format_checker)
    except ValidationError:
        pytest.fail('Unexpected ValidationError')


if __name__ == '__main__':
    test_get_post_beneficiary_endpoint_url_schema()
    test_post_beneficiary_endpoint_url_schema()
