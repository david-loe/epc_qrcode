from segno import helpers
import frappe


@frappe.whitelist()
def gen_epcqrcode(
    name,
    iban,
    amount,
    text=None,
    reference=None,
    bic=None,
    purpose=None,
    encoding=None,
    scale=3,
    dark="#000",
    light="#fff",
):
    qrcode = helpers.make_epc_qr(
        name=name, iban=iban, amount=amount, text=text, reference=reference, bic=bic, purpose=purpose, encoding=encoding
    )
    return qrcode.png_data_uri(scale=scale, dark=dark, light=light)
