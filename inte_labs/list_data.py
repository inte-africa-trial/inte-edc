from edc_list_data import PreloadData


model_data = {
    "edc_lab.consignee": [
        {
            "name": "The INTE Trial",
            "contact_name": "Josphine Birungi",
            "address": "LSTM Uganda",
            "postal_code": "-",
            "city": "Entebbe",
            "state": None,
            "country": "Uganda",
            "telephone": "555-5555",
            "mobile": "555-5555",
            "fax": None,
            "email": "josephine.birungi@mrcuganda.org",
        }
    ]
}

unique_field_data = {"edc_lab.consignee": {"name": ("-", "-")}}

preload_data = PreloadData(
    list_data=None, model_data=model_data, unique_field_data=unique_field_data
)
