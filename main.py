import pafy



print('You wanna download ')
print('1 - one video ')
print('2 - all playlist  ')

i = int(input())

if 1 > i > 2:
    print('1 or 2 !!')

elif i == 1:

    link = input("enter video url: ")
    strm = pafy.new(str(link)).streams

    i = 0
    for index in strm:
        print(str(i) + "-" + str(index))
        i = i + 1

    qlt = input("choose video quality: ")
    quality = int(qlt)
    if strm[quality].download():
        print('done')

else:
    link = input("enter playlist url: ")
    test = pafy.get_playlist(link)
    all_videos = test['items']

    strm = pafy.new(str(all_videos[0]['pafy'].watchv_url)).streams

    i = 0
    for index in strm:
        print(str(i) + "-" + str(index))
        i = i + 1

    qlt = input("choose video quality: ")
    quality = int(qlt)

    i = 0
    link = ""
    for item in all_videos:
        link = item['pafy'].watchv_url
        strms = pafy.new(link).streams
        if strms[quality].download():
            i = i + 1

    print("done")
