import requests

GRAPH_URL = "https://graph.facebook.com/v2.6"
ACCESS_TOKEN = "EAAEgVyIQhtMBABtGmAMZCYudLDK8uJmFEl4A8tWn6sZCX2HU1VR1RIivSx6lmeqEr7cEpuVX64NY7BhaxlZB2TDzYCzZBEsgMC4sKztHE9MPsIvHDOTFCPIMFQs1TZA10R4BauQOo1Ji1Nv6VL9KHVJviBbKgOTcfvlbecqh3GQJELAjR1f85"

def send_text_message(id, text):
    url = "{0}/me/messages?access_token={1}".format(GRAPH_URL, ACCESS_TOKEN)
    payload = {
        "recipient": {"id": id},
        "message": {"text": text}
    }
    response = requests.post(url, json=payload)

    if response.status_code != 200:
        print("Unable to send message: " + response.text)
    return response


"""
def send_image_url(id, img_url):
    pass
def send_button_message(id, text, buttons):
    pass
"""
