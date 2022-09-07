import starksign
from unittest import TestCase, main


starksign.environment = "sandbox"


class TestServerSignature(TestCase):

    def test_success(self):
        signature_request = starksign.signaturerequest.parse(
            content="{\"documentId\": \"0d9bf711fb804c448332c05dbb8e563d\", \"privateKey\": \"\\n-----BEGIN EC PRIVATE KEY-----\\nMHQCAQEEIDLbDgqXe6FT/dGJHBZEGFf3w18nq/PfjdooqIB+YUBooAcGBSuBBAAK\\noUQDQgAEubA3Ij8VEXH0z6XvlYe6LOSYKrlAxnhYMSFAHRQq/Gszpt1JeTbPuM16\\nXUC+hXwiiZi9Ep7vLSo4dcP3vngSlA==\\n-----END EC PRIVATE KEY-----\\n\", \"signerId\": \"6713235394789376\"}",
            signature="MEUCIB1Q2aU3y/9ObiIB7oBEI/jk7vnGhdIwz6ygSmKzbPm9AiEAoQd0z88nSt9Fy19Az2SiRRjsUDwYJyTsv1cRDWinzL8=",
        )
        print(signature_request)

        document = starksign.document.get(signature_request.document_id)
        print(document)

        signature = starksign.document.sign(
            id=document.id,
            content=document.content,
            signer_id=signature_request.signer_id,
            private_key=signature_request.private_key,
        )
        print(signature)


if __name__ == '__main__':
    main()
