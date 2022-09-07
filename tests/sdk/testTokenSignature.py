import starksign
from unittest import TestCase, main


starksign.environment = "sandbox"


class TestTokenSignature(TestCase):

    def test_success(self):
        token = "EzNahUcN"
        document = starksign.document.get("0d9bf711fb804c448332c05dbb8e563d")
        print(document)

        signersByContact = {signer.contact: signer for signer in document.signers}
        signer = signersByContact["developers@starkbank.com"]

        signature = starksign.document.sign(
            id=document.id,
            content=document.content,
            signer_id=signer.id,
            token=token,
        )

        print(signature)


if __name__ == '__main__':
    main()
