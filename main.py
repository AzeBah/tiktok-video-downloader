import requests



tiktokVideoLink = input("enter video link to download : ")

response = requests.get(
    tiktokVideoLink,
    headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"}
)

position = response.text.index("contentUrl")
position = response.text.index(":", position)
position = response.text.index('"', position)
position += 1
secondPos = response.text.index('"', position)
contentUrl = response.text[position:secondPos]




response = requests.get(
    contentUrl,
)

f = open("tiktokVideo.mp4" , "wb")
f.write(response.content)
f.close()