import base64

with open("m_device_align.png",mode="rb") as file:
    data = base64.b64encode(file.read()).decode()
    print(data)
